/* Enrutador por hash. Cada vista declara su módulo (SD4), sus RF (SD3) y sus actores,
   de modo que la matriz de trazabilidad y el mapa del sitio se generan del mismo registro. */
(function (L) {
  L.routes = [];

  L.route = (path, def) => {
    const keys = [];
    const re = path === '*' ? /(?!)/ : new RegExp('^' + path.replace(/:([a-z]+)/gi, (_, k) => { keys.push(k); return '([^/]+)'; }) + '$');
    L.routes.push({ path, re, keys, layout: 'app', rf: [], actors: [], ...def });
  };

  L.go = (path) => {
    if (location.hash === '#' + path) L.router.resolve();
    else location.hash = path;
  };

  const parse = () => {
    const raw = decodeURIComponent(location.hash.replace(/^#/, '')) || '/';
    const [path, qs] = raw.split('?');
    const query = Object.fromEntries(new URLSearchParams(qs || ''));
    for (const r of L.routes) {
      const m = path.match(r.re);
      if (m) return { route: r, params: Object.fromEntries(r.keys.map((k, i) => [k, m[i + 1]])), query, path };
    }
    return { route: L.routes.find((r) => r.path === '*'), params: {}, query, path };
  };

  L.titleOf = (r, params = {}) => (typeof r.title === 'function' ? r.title(params) : r.title);
  L.findRoute = (path) => L.routes.find((r) => r.re.test(path));

  // Cadena de rastro de navegación a partir del campo parent
  L.crumbs = (r, params, path) => {
    const chain = [{ label: L.titleOf(r, params), path }];
    let p = typeof r.parent === 'function' ? r.parent(params) : r.parent;
    let guard = 0;
    while (p && guard++ < 6) {
      const pr = L.findRoute(p);
      if (!pr) break;
      chain.unshift({ label: L.titleOf(pr, {}), path: p });
      p = typeof pr.parent === 'function' ? pr.parent({}) : pr.parent;
    }
    return chain;
  };

  L.router = {
    current: null,
    resolve() {
      const { route, params, query, path } = parse();
      // Direct link with a demo profile (e.g. #/flujo?perfil=evaluador): opens the screen already signed in
      // with that profile and skips the welcome tour. Only profiles without a second factor, so 2FA stays demonstrable.
      const linked = query.perfil && L.profile(query.perfil);
      if (route.layout === 'app' && linked && !linked.mfa && L.session()?.profile !== linked.id) {
        L.signIn(linked.id);
        L.setSession({ ...L.session(), first: false });
        L.store.set('seen.' + linked.id, true);
      }
      const s = L.session();
      if (route.layout === 'app' && !s) {
        L.store.set('next', path);
        L.go('/ingresar');
        return;
      }
      L.runLeave();
      L.router.current = { route, params, query, path };
      L.render(route, params, query, path);
    }
  };

  window.addEventListener('hashchange', () => L.router.resolve());
})(window.LFX = window.LFX || {});
