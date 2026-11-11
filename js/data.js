/* Datos simulados de Distribuidora Puelche S.A. (Caso 02 Logística).
   Cifras base tomadas del caso (cap. 2 y 7); el resto se genera de forma determinista. */
(function (L) {
  let seed = 20261113;
  const rnd = () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296);
  const pick = (a) => a[Math.floor(rnd() * a.length)];
  const int = (a, b) => Math.floor(a + rnd() * (b - a + 1));
  const rutBody = () => String(int(76000000, 77999999));
  const mkRut = (b = rutBody()) => L.rut.format(b + L.rut.dv(b));
  const today = new Date(2026, 10, 13, 9, 30);
  const day = (d, h = 9, m = 0) => { const x = new Date(today); x.setDate(x.getDate() + d); x.setHours(h, m, 0, 0); return x.toISOString(); };

  const D = {};
  D.today = today;
  D.empresa = { nombre: 'Distribuidora Puelche S.A.', sede: 'Talca', cobertura: "O'Higgins a La Araucanía", clientes: 14200, sku: 8400, skuFrio: 1100, proveedores: 180, entregasDia: 1400, entregasPeak: 2600, camionesPropios: 42, camionesContratados: 54 };

  D.sitios = [
    { id: 'CD-TAL', nombre: 'CD Talca', tipo: 'Centro de distribución', ocupacion: 81, zonas: { seco: 84, refrigerado: 77, congelado: 72 } },
    { id: 'CD-CON', nombre: 'CD Concepción', tipo: 'Centro de distribución', ocupacion: 74, zonas: { seco: 76, refrigerado: 71, congelado: 66 } },
    { id: 'XD-CUR', nombre: 'Plataforma Curicó', tipo: 'Cross-docking', ocupacion: 58 },
    { id: 'XD-CHI', nombre: 'Plataforma Chillán', tipo: 'Cross-docking', ocupacion: 63 },
    { id: 'XD-LAN', nombre: 'Plataforma Los Ángeles', tipo: 'Cross-docking', ocupacion: 49 }
  ];

  /* ---------- Perfiles (SD3, Anexo 3.A.12a; personas del caso, cap. 8) ---------- */
  D.profiles = [
    { id: 'evaluador', grupo: 'Evaluación', actor: 'Comisión evaluadora (todos los actores)', name: 'Comisión evaluadora', role: 'Acceso completo de demostración', iface: 'Todas las interfaces', mfa: false, all: true, home: ['kpis', 'flujo', 'alertas', 'rutas', 'tareas', 'calidad'] },
    { id: 'gerente-ops', grupo: 'Oficina y gerencia', actor: 'Gerente de Operaciones', name: 'Nelson Quinteros Aravena', role: 'Gerente de Operaciones y Logística', iface: 'Consola operacional', mfa: true, home: ['kpis', 'rutas', 'alertas', 'ocupacion', 'tareas', 'telemetria'], menu: ['/inicio', '/tablero', '/bandeja', '/pedidos', '/flujo', '/rutas', '/despacho/asignaciones', '/preparacion', '/inventario', '/devoluciones', '/analitica', '/telemetria', '/admin/roles'] },
    { id: 'planificador', grupo: 'Oficina y gerencia', actor: 'Planificador de Rutas', name: 'Hugo Maldonado Sepúlveda', role: 'Planificador de Rutas', iface: 'Consola de planificación', mfa: true, home: ['rutas', 'kpis', 'telemetria', 'tareas'], menu: ['/inicio', '/tablero', '/bandeja', '/rutas', '/pedidos', '/flujo', '/telemetria', '/clientes', '/analitica'] },
    { id: 'preventista', grupo: 'Terreno', actor: 'Preventista', name: 'Sandra Riffo Alarcón', role: 'Preventista · zona Curicó', iface: 'App de preventa', mfa: false, field: true, home: ['agenda', 'tareas', 'alertas'], menu: ['/inicio', '/terreno/preventa', '/pedidos', '/flujo', '/clientes', '/bandeja'] },
    { id: 'conductor', grupo: 'Terreno', actor: 'Conductor propio', name: 'Jonathan Curihual Paillán', role: 'Conductor repartidor · ruta Cauquenes', iface: 'App de reparto', mfa: false, field: true, home: ['ruta-dia', 'tareas'], menu: ['/inicio', '/terreno', '/devoluciones', '/rendicion', '/bandeja'] },
    { id: 'preparador', grupo: 'Bodega y calidad', actor: 'Preparador', name: 'Matías Lagos Contreras', role: 'Preparador · turno noche CD Talca', iface: 'App de bodega en terminal portátil', mfa: false, field: true, home: ['mision', 'tareas'], menu: ['/inicio', '/preparacion', '/flujo', '/recepcion', '/bandeja'] },
    { id: 'bodega', grupo: 'Bodega y calidad', actor: 'Jefa de Bodega', name: 'Ximena Bravo Cortés', role: 'Jefa de Bodega · CD Talca', iface: 'Consola de bodega', mfa: true, home: ['ocupacion', 'tareas', 'alertas', 'kpis'], menu: ['/inicio', '/tablero', '/bandeja', '/recepcion', '/inventario', '/preparacion', '/devoluciones', '/flujo'] },
    { id: 'calidad', grupo: 'Bodega y calidad', actor: 'Jefa de Calidad', name: 'Katherine Ñanco Millán', role: 'Jefa de Calidad y Aseguramiento', iface: 'Consola de Calidad', mfa: true, home: ['calidad', 'telemetria', 'alertas', 'tareas'], menu: ['/inicio', '/tablero', '/bandeja', '/calidad', '/telemetria', '/inventario', '/devoluciones', '/analitica'] },
    { id: 'comercial', grupo: 'Oficina y gerencia', actor: 'Gerente Comercial', name: 'Rubén Salinas Fuentealba', role: 'Gerente Comercial', iface: 'Consola comercial y tableros', mfa: true, home: ['kpis', 'clientes', 'alertas', 'tareas'], menu: ['/inicio', '/tablero', '/bandeja', '/clientes', '/pedidos', '/canal-moderno', '/analitica', '/admin/parametros'] },
    { id: 'finanzas', grupo: 'Oficina y gerencia', actor: 'Gerente de Finanzas', name: 'Patricio Vergara Undurraga', role: 'Gerente de Administración y Finanzas', iface: 'Consola financiera y tableros', mfa: true, home: ['kpis', 'rendicion', 'tareas', 'alertas'], menu: ['/inicio', '/tablero', '/bandeja', '/rendicion', '/flujo', '/clientes', '/devoluciones', '/analitica', '/admin/parametros'] },
    { id: 'ti', grupo: 'Oficina y gerencia', actor: 'Jefe de TI', name: 'Eduardo Kaufmann Vial', role: 'Jefe de Tecnologías de Información', iface: 'Consola de administración', mfa: true, home: ['admin', 'alertas', 'tareas'], menu: ['/inicio', '/tablero', '/bandeja', '/admin/usuarios', '/admin/roles', '/admin/parametros', '/admin/flujos', '/admin/integraciones', '/admin/auditoria', '/analitica'] },
    { id: 'cliente', grupo: 'Externos', actor: 'Cliente del canal tradicional', name: 'Rosa Fuentes Lagos', role: 'Cliente · Almacén Doña Rosa (canal tradicional)', iface: 'Portal de clientes', mfa: true, home: ['mis-pedidos', 'cuenta', 'tareas'], menu: ['/inicio', '/portal/pedido', '/portal/entregas', '/portal/cuenta', '/bandeja'] },
    { id: 'conductor-ext', grupo: 'Terreno', actor: 'Conductor externo', name: 'Óscar Vidal Rebolledo', role: 'Conductor externo · Transportes Maule Ltda.', iface: 'App de reparto con credencial de turno', mfa: false, field: true, home: ['ruta-dia', 'tareas'], menu: ['/inicio', '/terreno', '/devoluciones', '/rendicion', '/bandeja'] },
    { id: 'cliente-moderno', grupo: 'Externos', actor: 'Cliente del canal moderno', name: 'Paula Herrera Soto', role: 'Cliente · Supermercado Regional Maule (canal moderno)', iface: 'Portal de clientes; EDI de la cadena', mfa: true, home: ['mis-pedidos', 'cuenta', 'tareas'], menu: ['/inicio', '/portal/pedido', '/portal/entregas', '/portal/cuenta', '/bandeja'] },
    { id: 'transportista', grupo: 'Externos', actor: 'Empresa transportista', name: 'Marcela Pino Lagos', role: 'Representante · Transportes Maule Ltda.', iface: 'Portal de transportistas', mfa: true, home: ['transp', 'tareas'], menu: ['/inicio', '/portal/transportista', '/bandeja'] },
    { id: 'proveedor', grupo: 'Externos', actor: 'Proveedor', name: 'Luis Parra Rojas', role: 'Representante · Lácteos del Sur S.A.', iface: 'Portal de proveedores', mfa: true, home: ['prov', 'tareas'], menu: ['/inicio', '/portal/proveedor', '/bandeja'] }
  ];

  /* ---------- Productos ---------- */
  const prods = [
    ['Arroz grado 1 · 1 kg', 'Abarrotes', 'Seco', 1290], ['Aceite maravilla · 1 L', 'Abarrotes', 'Seco', 2490], ['Azúcar granulada · 1 kg', 'Abarrotes', 'Seco', 1190],
    ['Fideos spaghetti 5 · 400 g', 'Abarrotes', 'Seco', 890], ['Harina sin polvos · 1 kg', 'Abarrotes', 'Seco', 1050], ['Té en bolsitas · 100 u', 'Abarrotes', 'Seco', 2790],
    ['Bebida cola · 3 L', 'Bebidas', 'Seco', 2690], ['Agua mineral · 1,6 L', 'Bebidas', 'Seco', 890], ['Jugo néctar durazno · 1,5 L', 'Bebidas', 'Seco', 1490],
    ['Leche entera · 1 L', 'Lácteos', 'Refrigerado', 1150], ['Yogur batido frutilla · 125 g', 'Lácteos', 'Refrigerado', 390], ['Queso gauda laminado · 250 g', 'Lácteos', 'Refrigerado', 3290],
    ['Mantequilla con sal · 250 g', 'Lácteos', 'Refrigerado', 2690], ['Jamón de pavo · 250 g', 'Cecinas', 'Refrigerado', 2390], ['Vienesas · 20 u', 'Cecinas', 'Refrigerado', 2990],
    ['Helado vainilla · 1 L', 'Congelados', 'Congelado', 3490], ['Papas prefritas · 1 kg', 'Congelados', 'Congelado', 2790], ['Hamburguesas de vacuno · 4 u', 'Congelados', 'Congelado', 3990],
    ['Detergente líquido · 3 L', 'Limpieza', 'Seco', 6990], ['Papel higiénico · 12 rollos', 'Limpieza', 'Seco', 5490], ['Lavalozas · 750 ml', 'Limpieza', 'Seco', 1790],
    ['Galletas de chocolate · 3 u', 'Confites', 'Seco', 990], ['Chocolate de leche · 100 g', 'Confites', 'Seco', 1290], ['Café instantáneo · 170 g', 'Abarrotes', 'Seco', 4990]
  ];
  D.productos = prods.map((p, i) => ({
    sku: `SKU-${String(10230 + i * 17)}`,
    gtin: `78${String(int(10000000000, 99999999999))}`,
    nombre: p[0], categoria: p[1], temp: p[2], precio: p[3],
    stock: int(120, 4800), reservado: int(10, 400), transito: int(0, 300),
    trazable: p[2] !== 'Seco' || i % 3 === 0
  }));
  // Reservations cannot exceed physical stock: available stock is never negative (RNG-02)
  D.productos.forEach((p) => { p.reservado = Math.min(p.reservado, Math.floor(p.stock * 0.4)); });
  // One lot per product so that order lines, returns and Quality share the same lot ids
  const LOTE_FIJO = { 9: 'L2611-47', 10: 'L2611-52', 15: 'L2610-88', 13: 'L2611-03', 11: 'L2611-21', 17: 'L2610-64' };
  D.productos.forEach((p, i) => { p.lote = LOTE_FIJO[i] || `L2612-${String(10 + i * 3).padStart(2, '0')}`; p.loteVence = { 9: 28, 10: 19, 15: 240, 13: 24, 11: 46, 17: 150 }[i] ?? 60 + (i * 7) % 90; });
  // Price exceptions per client or chain, configured by Comercial (RF-03.11)
  D.excepcionesPrecio = [
    { id: 'EP-104', alcance: 'Cadena', destino: 'Supermercado Regional Maule', sku: D.productos[6].sku, producto: D.productos[6].nombre, tipo: 'Precio fijo', valor: 2490, vigencia: '01-11-2026 a 31-12-2026', aprobado: 'Rubén Salinas Fuentealba', estado: 'Vigente' },
    { id: 'EP-103', alcance: 'Cliente', destino: 'Hotel Plaza Talca', sku: D.productos[11].sku, producto: D.productos[11].nombre, tipo: 'Descuento', valor: 6, vigencia: '15-10-2026 a 15-01-2027', aprobado: 'Rubén Salinas Fuentealba', estado: 'Vigente' }
  ];

  /* ---------- Clientes (contraparte externa, RT-12.12) ---------- */
  const nombres = ['Almacén Doña Rosa', 'Minimarket El Roble', 'Supermercado La Esquina', 'Almacén San Expedito', 'Botillería Los Aromos', 'Minimarket Santa Elena', 'Almacén Las Rosas', 'Distribuidora Don Lucho', 'Almacén El Copihue', 'Minimarket Vista Hermosa', 'Restaurante El Fogón', 'Casino Agroindustrial Maule', 'Hotel Plaza Talca', 'Almacén La Palmera', 'Minimarket Lircay', 'Almacén Doña Inés', 'Panadería La Espiga', 'Almacén El Quillay', 'Minimarket Piduco', 'Supermercado Regional Maule · Local 12', 'Supermercado Regional Maule · Local 7', 'Almacén Las Camelias', 'Almacén Rayito de Sol', 'Fuente de soda El Paso', 'Minimarket Los Castaños', 'Almacén Tres Esquinas', 'Almacén El Maitén', 'Colegio San Agustín · Casino', 'Almacén Doña Juanita', 'Minimarket Florida', 'Almacén Los Laureles', 'Supermercado Regional Maule · Local 3', 'Almacén Santa Rita', 'Minimarket Cordillera', 'Almacén El Sauce', 'Restaurante Mar y Tierra', 'Almacén Doña Berta', 'Minimarket Villa Alegre', 'Almacén El Trébol', 'Almacén Empedrado Centro', 'Minimarket Linares Sur', 'Almacén Constitución Puerto', 'Almacén Doña Marta', 'Minimarket Parral Centro', 'Almacén El Boldo', 'Almacén San Clemente', 'Cafetería Universitaria', 'Almacén Los Niches'];
  const comunas = ['Talca', 'Curicó', 'Linares', 'Cauquenes', 'Constitución', 'San Javier', 'Molina', 'Parral', 'Chillán', 'Concepción', 'Los Ángeles', 'Empedrado', 'San Clemente', 'Villa Alegre', 'Rancagua', 'Temuco'];
  const contactos = ['Rosa Fuentes', 'Luis Parra', 'Carmen Soto', 'Jorge Muñoz', 'Patricia Rojas', 'Héctor Díaz', 'Marcela Pino', 'Luciano Vera', 'Gloria Henríquez', 'Raúl Sepúlveda', 'Ana Morales', 'Pedro Castro'];
  const prevs = ['Sandra Riffo', 'Cristián Mella', 'Valeria Opazo', 'Francisco Yáñez', 'Daniela Bustos'];
  D.clientes = nombres.map((n, i) => {
    const canal = /Supermercado/.test(n) ? 'Moderno' : /Restaurante|Casino|Hotel|Fuente|Cafetería|Panadería/.test(n) ? 'Food service' : 'Tradicional';
    const credito = canal === 'Moderno' ? int(18, 40) * 1e6 : canal === 'Food service' ? int(3, 9) * 1e6 : int(4, 18) * 1e5;
    const deuda = Math.round(credito * (rnd() * 0.7));
    const vencida = i % 7 === 3 ? Math.round(deuda * 0.4) : i % 5 === 1 ? Math.round(deuda * 0.1) : 0;
    const otif = Math.round((76 + rnd() * 22) * 10) / 10;
    return {
      id: `CL-${String(10021 + i * 37)}`,
      nombre: n, canal, rut: mkRut(),
      comuna: i === 0 ? 'Cauquenes' : pick(comunas),
      direccion: `${pick(['Av. Lircay', 'Calle 1 Sur', 'Los Aromos', 'Av. San Miguel', 'Camino a Duao', 'Pasaje Los Robles', 'Av. Libertador', 'Calle Prat', 'Calle Chacabuco'])} ${int(100, 2900)}`,
      contacto: i === 0 ? 'Rosa Fuentes Lagos' : pick(contactos), telefono: `+56 9 ${int(5000, 9999)} ${int(1000, 9999)}`,
      correo: `contacto${i + 1}@${n.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z]+/g, '').slice(0, 14)}.cl`,
      preventista: i === 0 ? 'Sandra Riffo' : pick(prevs),
      ventana: pick(['08:00–11:00', '09:00–12:00', '10:00–13:00', '14:00–17:00', '15:00–18:00']),
      dias: pick(['Lun · Mié · Vie', 'Mar · Jue', 'Lun a Vie', 'Lun · Jue']),
      credito, deuda, vencida, otif,
      pago: Math.round((70 + rnd() * 30)), devol: Math.round(rnd() * 60) / 10,
      envases: { canastillos: int(0, 48), pallets: canal === 'Moderno' ? int(2, 18) : int(0, 3) },
      ventaMes: canal === 'Moderno' ? int(18, 60) * 1e6 : canal === 'Food service' ? int(2, 9) * 1e6 : int(4, 30) * 1e5,
      costoServir: Math.round((canal === 'Moderno' ? 3 : canal === 'Food service' ? 6 : 9 + rnd() * 9) * 10) / 10,
      estado: vencida > 0 && i % 7 === 3 ? 'Bloqueado' : 'Activo',
      desde: 1998 + (i % 26)
    };
  });
  D.clientes.forEach((c) => (c.rating = Math.round(((c.otif / 100) * 2 + (c.pago / 100) * 2 + (1 - c.devol / 10)) * 10) / 10));

  /* ---------- Pedidos y sus estados (proceso principal) ---------- */
  D.estadosPedido = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Retenido', 'Planificado', 'En picking', 'Cargado', 'En ruta', 'Entregado', 'Parcial', 'Fallido', 'Reprogramado', 'Rendido'];
  D.estadoKind = { 'Capturado sin conexión': 'warning', 'Pendiente de validación': 'info', Confirmado: 'info', Retenido: 'danger', Planificado: 'info', 'En picking': 'accent', Cargado: 'accent', 'En ruta': 'accent', Entregado: 'success', Parcial: 'warning', Fallido: 'danger', Reprogramado: 'warning', Rendido: 'success' };
  const estPeso = ['Entregado', 'Entregado', 'Entregado', 'Rendido', 'Rendido', 'En ruta', 'En ruta', 'Cargado', 'En picking', 'Planificado', 'Confirmado', 'Pendiente de validación', 'Capturado sin conexión', 'Parcial', 'Fallido', 'Retenido', 'Reprogramado'];
  D.pedidos = Array.from({ length: 64 }, (_, i) => {
    const cli = D.clientes[i % D.clientes.length];
    const lineas = Array.from({ length: int(3, 7) }, () => { const p = pick(D.productos); const q = int(2, 36); int(2600, 2699); int(10, 99); int(20, 180); return { sku: p.sku, nombre: p.nombre, temp: p.temp, cant: q, precio: p.precio, lote: p.lote, vence: day(p.loteVence) }; });
    const total = lineas.reduce((a, l) => a + l.cant * l.precio, 0);
    const estado = i === 0 ? 'Capturado sin conexión' : estPeso[i % estPeso.length];
    return {
      id: `PV-${260000 + 4821 - i * 7}`, cliente: cli.id, clienteNombre: cli.nombre, canal: cli.canal, comuna: cli.comuna,
      preventista: cli.preventista, creado: day(-Math.floor(i / 9), 9 + (i % 8), (i * 7) % 60), entrega: day(1 - Math.floor(i / 9) + (i % 2)),
      ventana: cli.ventana, lineas, total, estado, ruta: `R-${String(1 + (i % 12)).padStart(2, '0')}`, origen: cli.canal === 'Moderno' ? 'EDI' : i % 6 === 0 ? 'Portal' : 'Preventa'
    };
  });

  // Agreed list price changed after some orders were taken (RF-03.11, RF-03.12)
  D.cambiosLista = [{ sku: D.productos[2].sku, nuevo: 1290, desde: '12-11-2026' }, { sku: D.productos[9].sku, nuevo: 1190, desde: '12-11-2026' }];
  D.cambiosLista.forEach((c) => { const pr = D.productos.find((x) => x.sku === c.sku); c.anterior = pr.precio; c.nombre = pr.nombre; pr.precio = c.nuevo; });
  // Orders not yet invoiced whose agreed price differs from the current list (RF-03.12)
  D.porFacturar = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Retenido', 'Planificado', 'En picking', 'Cargado', 'En ruta', 'Reprogramado'];
  L.difPrecio = (o) => { if (o.precioCorregido || !D.porFacturar.includes(o.estado)) return null; const lineas = o.lineas.filter((l) => { const pr = D.productos.find((x) => x.sku === l.sku); return pr && pr.precio !== l.precio; }); if (!lineas.length) return null; const lista = o.lineas.reduce((a, l) => a + l.cant * D.productos.find((x) => x.sku === l.sku).precio, 0); return { lineas, lista, diferencia: lista - o.total }; };

  /* ---------- Flota y rutas (M4, M6, M12) ---------- */
  const conductores = ['Jonathan Curihual', 'Manuel Gatica', 'Rodrigo Poblete', 'Iván Leiva', 'Carlos Navarrete', 'Felipe Arriagada', 'Mauricio Toro', 'Claudio Fuentes', 'Óscar Vidal', 'Andrés Cáceres', 'Sergio Lagos', 'Esteban Medina'];
  const zonasRuta = ['Cauquenes', 'Talca Norte', 'Talca Sur', 'Curicó', 'Linares', 'Constitución', 'San Javier', 'Molina', 'Parral', 'Chillán', 'Concepción', 'Los Ángeles'];
  D.rutas = zonasRuta.map((z, i) => ({
    id: `R-${String(i + 1).padStart(2, '0')}`, zona: z, conductor: conductores[i], externo: i % 3 === 2,
    transportista: i % 3 === 2 ? pick(['Transportes Maule Ltda.', 'Fletes del Sur SpA', 'TransAndes Carga']) : 'Flota propia',
    camion: `${pick(['KXTR', 'LBHP', 'JZWS', 'PFGD', 'RTKC'])}-${int(10, 99)}`, frio: i % 2 === 0,
    paradas: int(14, 34), hechas: 0, ocupacion: int(58, 96), km: int(80, 260), estado: '', otif: Math.round((78 + rnd() * 20) * 10) / 10,
    salida: ((m) => { const t = 330 + m * 2; return `${String(Math.floor(t / 60)).padStart(2, '0')}:${String(t % 60).padStart(2, '0')}`; })(int(0, 45)), eta: '', desvio: i === 6
  }));
  const PLATES = ['KXTR-21', 'LBHP-34', 'JZWS-62', 'PFGD-51', 'RTKC-13', 'KXTR-47', 'LBHP-86', 'JZWS-29', 'KXTR-98', 'PFGD-73', 'RTKC-58', 'LBHP-15'];
  D.rutas.forEach((r, i) => { r.camion = PLATES[i]; });
  D.rutas.forEach((r, i) => { r.hechas = Math.min(r.paradas, Math.round(r.paradas * [0.45, 0.8, 0.6, 1, 0.3, 0.55, 0.7, 0.2, 0.9, 0.5, 0.65, 0.4][i])); r.estado = r.hechas === r.paradas ? 'Completada' : r.hechas > 0 ? 'En ruta' : 'Por salir'; r.eta = `${14 + (i % 4)}:${String(int(0, 59)).padStart(2, '0')}`; });

  // Paradas de la ruta del conductor (R-01 Cauquenes) para la vista de terreno
  const STOP_ORD = [1, 5, 9, 13, 17, 21];
  const STOP_CLI = [[0, 'Cauquenes'], [4, 'Cauquenes'], [8, 'Cauquenes'], [16, 'Cauquenes'], [21, 'Cauquenes'], [39, 'Empedrado']];
  STOP_CLI.forEach(([ci, com]) => { D.clientes[ci].comuna = com; });
  STOP_ORD.forEach((k, j) => { const c = D.clientes[STOP_CLI[j][0]], o = D.pedidos[k]; Object.assign(o, { cliente: c.id, clienteNombre: c.nombre, canal: c.canal, comuna: c.comuna, preventista: c.preventista, ventana: c.ventana }); });

  // Route is assigned by delivery zone of the client; order status follows the status of its route
  const zonaRuta = { Cauquenes: 0, Empedrado: 0, Talca: 1, 'San Clemente': 1, Curicó: 3, Rancagua: 3, Linares: 4, 'Villa Alegre': 4, Constitución: 5, 'San Javier': 6, Molina: 7, Parral: 8, Chillán: 9, Concepción: 10, 'Los Ángeles': 11, Temuco: 11 };
  const preRuta = ['Capturado sin conexión', 'Pendiente de validación', 'Confirmado', 'Retenido'];
  const cnt = {};
  D.pedidos.forEach((p, i) => {
    if (preRuta.includes(p.estado)) { p.ruta = ''; return; }
    let zi = zonaRuta[p.comuna] ?? 1;
    if (p.comuna === 'Talca' && (i >> 1) % 2) zi = 2;
    const r = D.rutas[zi]; p.ruta = r.id;
    const k = (cnt[r.id] = (cnt[r.id] || 0) + 1) - 1;
    if (STOP_ORD.includes(i)) p.estado = 'En ruta';
    else if (r.estado === 'Completada') p.estado = ['Entregado', 'Rendido', 'Parcial', 'Entregado'][k % 4];
    else if (r.estado === 'En ruta') p.estado = ['En ruta', 'En ruta', 'Entregado', 'En ruta', 'Parcial', 'Fallido'][k % 6];
    else p.estado = ['Planificado', 'En picking', 'Cargado'][k % 3];
  });

  D.paradas = [
    { id: 'E-1', cliente: D.clientes[0].id, nombre: 'Almacén Doña Rosa', dir: 'Av. Prat 512, Cauquenes', ventana: '09:00–09:30', estado: 'Pendiente', pedido: D.pedidos[1].id, bultos: 14, monto: 186400, contado: true, frio: true },
    { id: 'E-2', cliente: D.clientes[4].id, nombre: 'Botillería Los Aromos', dir: 'Los Aromos 1180, Cauquenes', ventana: '09:30–10:00', estado: 'Pendiente', pedido: D.pedidos[5].id, bultos: 8, monto: 94300, contado: true },
    { id: 'E-3', cliente: D.clientes[8].id, nombre: 'Almacén El Copihue', dir: 'Calle Victoria 233, Cauquenes', ventana: '10:00–10:30', estado: 'Pendiente', pedido: D.pedidos[9].id, bultos: 11, monto: 132900, contado: false },
    { id: 'E-4', cliente: D.clientes[16].id, nombre: 'Panadería La Espiga', dir: 'Av. Balmaceda 77, Cauquenes', ventana: '10:30–11:00', estado: 'Pendiente', pedido: D.pedidos[13].id, bultos: 6, monto: 58700, contado: true, frio: true },
    { id: 'E-5', cliente: D.clientes[21].id, nombre: 'Almacén Las Camelias', dir: 'Camino a Chanco km 3', ventana: '11:30–12:00', estado: 'Pendiente', pedido: D.pedidos[17].id, bultos: 9, monto: 101200, contado: false },
    { id: 'E-6', cliente: D.clientes[39].id, nombre: 'Almacén Empedrado Centro', dir: 'Calle Errázuriz 40, Empedrado', ventana: '13:00–13:30', estado: 'Pendiente', pedido: D.pedidos[21].id, bultos: 5, monto: 45200, contado: true }
  ];
  // Amount to collect at each stop is the total of its order, so cash payments reconcile exactly
  D.paradas.forEach((st) => { st.monto = D.pedidos.find((o) => o.id === st.pedido).total; });

  /* ---------- Devoluciones y envases (M8, proceso secundario) ---------- */
  D.motivosDevolucion = ['Producto dañado en tránsito', 'Vencimiento próximo', 'Error de preparación', 'Rechazo por cadena de frío', 'Sobrestock del cliente', 'Envase defectuoso'];
  D.estadosDev = ['Registrada en ruta', 'Recepcionada en andén', 'En evaluación', 'Aprobada', 'Rechazada', 'Nota de crédito emitida'];
  D.devoluciones = Array.from({ length: 26 }, (_, i) => {
    const p = D.pedidos[(i * 3) % D.pedidos.length];
    pick(D.productos);
    const ln = p.lineas[i % p.lineas.length];
    const prod = D.productos.find((x) => x.sku === ln.sku);
    const est = ['Registrada en ruta', 'Recepcionada en andén', 'En evaluación', 'En evaluación', 'Aprobada', 'Nota de crédito emitida', 'Rechazada'][i % 7];
    return { id: `DV-${String(5530 - i * 3)}`, pedido: p.id, cliente: p.cliente, clienteNombre: p.clienteNombre, sku: prod.sku, producto: prod.nombre, temp: prod.temp, cant: Math.min(ln.cant, int(1, 24)), lote: (int(0, 1), int(0, 1), ln.lote), motivo: pick(D.motivosDevolucion), estado: est, fecha: day(-Math.floor(i / 3), 10 + (i % 7)), conductor: pick(conductores), monto: int(4, 120) * 1000, destino: est === 'Aprobada' || est === 'Nota de crédito emitida' ? pick(['Reingreso a stock', 'Merma', 'Devolución a proveedor']) : '' };
  });

  // Cost to serve = base components + returns and waste of the client (RF-08.07).
  // Share of the returned amount that becomes cost, by destination.
  D.costoDestino = { Merma: 1, 'Devolución a proveedor': 0.25, 'Venta con descuento': 0.4, 'Reingreso a stock': 0.15, '': 0.15 };
  // Waste registered in inventory (SKU, lot, quantity, origin); waste found on a client's shelf adds to their cost to serve (RF-08.05)
  D.mermas = [];
  L.costoDevol = (c) => { const ds = D.devoluciones.filter((d) => d.cliente === c.id && d.estado !== 'Rechazada'); const mm = D.mermas.filter((m) => m.cliente === c.id); const monto = ds.reduce((a, d) => a + d.monto * (D.costoDestino[d.destino] ?? 0.15), 0) + mm.reduce((a, m) => a + m.monto, 0); return { n: ds.length + mm.length, mermas: ds.filter((d) => d.destino === 'Merma').length + mm.length, monto: Math.round(monto), pct: Math.round((monto / c.ventaMes) * 1000) / 10 }; };
  D.clientes.forEach((c) => { c.costoBase = Math.round(c.costoServir * 0.86 * 10) / 10; Object.defineProperty(c, 'costoServir', { enumerable: true, configurable: true, get: () => Math.round((c.costoBase + L.costoDevol(c).pct) * 10) / 10 }); });

  /* ---------- Lotes y calidad (M9) ---------- */
  D.lotes = [
    { id: 'L2611-47', sku: D.productos[9].sku, producto: 'Leche entera · 1 L', proveedor: 'Lácteos del Sur S.A.', recepcion: day(-12), vence: day(28), unidades: 14400, clientes: 312, estado: 'Liberado', temp: 'Refrigerado' },
    { id: 'L2611-52', sku: D.productos[10].sku, producto: 'Yogur batido frutilla · 125 g', proveedor: 'Lácteos del Sur S.A.', recepcion: day(-9), vence: day(19), unidades: 28800, clientes: 486, estado: 'Retenido', temp: 'Refrigerado' },
    { id: 'L2610-88', sku: D.productos[15].sku, producto: 'Helado vainilla · 1 L', proveedor: 'Heladería Andina Ltda.', recepcion: day(-20), vence: day(240), unidades: 3600, clientes: 141, estado: 'Liberado', temp: 'Congelado' },
    { id: 'L2611-03', sku: D.productos[13].sku, producto: 'Jamón de pavo · 250 g', proveedor: 'Cecinas Centinela', recepcion: day(-6), vence: day(24), unidades: 6200, clientes: 208, estado: 'En evaluación', temp: 'Refrigerado' },
    { id: 'L2611-21', sku: D.productos[11].sku, producto: 'Queso gauda laminado · 250 g', proveedor: 'Lácteos del Sur S.A.', recepcion: day(-4), vence: day(46), unidades: 5400, clientes: 156, estado: 'Liberado', temp: 'Refrigerado' },
    { id: 'L2610-64', sku: D.productos[17].sku, producto: 'Hamburguesas de vacuno · 4 u', proveedor: 'Frigorífico Ñuble', recepcion: day(-25), vence: day(150), unidades: 4800, clientes: 97, estado: 'Liberado', temp: 'Congelado' }
  ];

  // Lots for the remaining products, so every lot referenced by an order exists in Quality
  const provCat = { Abarrotes: 'Molinos del Maule', Bebidas: 'Bebidas Andinas', Lácteos: 'Lácteos del Sur S.A.', Cecinas: 'Cecinas Centinela', Congelados: 'Frigorífico Ñuble', Limpieza: 'Limpieza Total Ltda.', Confites: 'Molinos del Maule' };
  D.productos.forEach((p, i) => { if (D.lotes.some((l) => l.id === p.lote)) return; D.lotes.push({ id: p.lote, sku: p.sku, producto: p.nombre, proveedor: provCat[p.categoria], recepcion: day(-(3 + (i * 5) % 20)), vence: day(p.loteVence), unidades: 2400 + (i * 613) % 9000, clientes: 40 + (i * 29) % 300, estado: 'Liberado', temp: p.temp }); });

  /* ---------- Telemetría y cadena de frío (M12) ---------- */
  D.camiones = D.rutas.filter((r) => r.frio).map((r, i) => ({ ruta: r.id, camion: r.camion, conductor: r.conductor, temp: [3.4, 4.1, -19.6, 8.6, 2.8, -21.2][i], setpoint: [4, 4, -18, 4, 4, -18][i], estado: i === 3 ? 'Excursión crítica' : i === 1 ? 'Advertencia' : 'Normal', señal: i === 4 ? 'Satélite' : 'Móvil', lat: 0, lng: 0 }));

  /* ---------- Usuarios, roles y auditoría (administración) ---------- */
  D.roles = [
    { id: 'preventista', nombre: 'Preventista', usuarios: 62, modulos: ['M3'], desc: 'Captura de pedidos y cobranza en terreno.' },
    { id: 'conductor', nombre: 'Conductor (tripulación propia y peoneta)', usuarios: 84, modulos: ['M6', 'M7', 'M8'], desc: 'Entrega, POD, cobro, devoluciones y envases.' },
    { id: 'preparador', nombre: 'Preparador', usuarios: 180, modulos: ['M5', 'M1'], desc: 'Misiones de picking y recepción autorizada.' },
    { id: 'bodega', nombre: 'Jefatura de Bodega', usuarios: 4, modulos: ['M1', 'M2', 'M5', 'M8'], desc: 'Supervisión de bodega e inventario.' },
    { id: 'calidad', nombre: 'Calidad', usuarios: 3, modulos: ['M9'], desc: 'Parámetros térmicos, bloqueo y retiro.' },
    { id: 'planificador', nombre: 'Planificación de rutas', usuarios: 3, modulos: ['M4', 'M12'], desc: 'Generación y corrección de rutas.' },
    { id: 'finanzas', nombre: 'Finanzas y tesorería', usuarios: 6, modulos: ['M7', 'M10'], desc: 'Rendición, crédito y costo de servir.' },
    { id: 'comercial', nombre: 'Comercial', usuarios: 5, modulos: ['M3', 'M7', 'M10', 'M11'], desc: 'Reglas comerciales y canal moderno.' },
    { id: 'gerente-ops', nombre: 'Gerencia de Operaciones', usuarios: 2, modulos: ['M2', 'M4', 'M5', 'M6', 'M10', 'M12'], desc: 'Supervisión de despacho y excepciones; aprueba asignaciones de turno.' },
    { id: 'conductor-ext', nombre: 'Conductor externo', usuarios: 160, modulos: ['M6', 'M7', 'M8'], desc: 'Identidad personal ligada a empresa y turno; alta con OTP del jefe de flota.', externo: 'OTP del jefe de flota; despacho aprueba la asignación' },
    { id: 'cliente', nombre: 'Cliente canal tradicional', usuarios: 11600, modulos: ['M3', 'M6', 'M7'], desc: 'Portal opcional (Etapa 2); solo sus datos.', externo: 'Cuenta activada por el preventista con código SMS' },
    { id: 'cliente-moderno', nombre: 'Cliente canal moderno', usuarios: 500, modulos: ['M11', 'M3'], desc: 'Portal y conector EDI con sesión humana y técnica separadas (Etapa 2).', externo: 'Registro con RUT habilitado (RF-12.25)' },
    { id: 'transportista', nombre: 'Empresa transportista', usuarios: 10, modulos: ['M4', 'M6', 'M12'], desc: 'Portal por representante autorizado (Etapa 2).', externo: 'Representante autorizado' },
    { id: 'proveedor', nombre: 'Proveedor', usuarios: 180, modulos: ['M1'], desc: 'Consulta de órdenes y recepciones, solo lectura (Etapa 2).', externo: 'Representante autorizado' },
    { id: 'admin', nombre: 'Administración TI', usuarios: 4, modulos: ['Base'], desc: 'Identidad, parámetros y auditoría.' }
  ];
  D.permisos = ['Consultar', 'Crear', 'Modificar', 'Aprobar', 'Exportar', 'Administrar'];
  D.matriz = {
    preventista: [1, 1, 1, 0, 0, 0], conductor: [1, 1, 1, 0, 0, 0], preparador: [1, 1, 0, 0, 0, 0], bodega: [1, 1, 1, 1, 1, 0], calidad: [1, 1, 1, 1, 1, 0],
    planificador: [1, 1, 1, 1, 1, 0], finanzas: [1, 0, 1, 1, 1, 0], comercial: [1, 1, 1, 1, 1, 0], 'gerente-ops': [1, 1, 1, 1, 1, 0], 'conductor-ext': [1, 1, 1, 0, 0, 0], cliente: [1, 1, 0, 0, 0, 0], 'cliente-moderno': [1, 1, 0, 0, 0, 0], transportista: [1, 1, 1, 0, 0, 0], proveedor: [1, 0, 0, 0, 0, 0], admin: [1, 1, 1, 1, 1, 1]
  };
  const personas = [['Sandra Riffo Alarcón', 'preventista'], ['Jonathan Curihual Paillán', 'conductor'], ['Matías Lagos Contreras', 'preparador'], ['Ximena Bravo Cortés', 'bodega'], ['Katherine Ñanco Millán', 'calidad'], ['Hugo Maldonado Sepúlveda', 'planificador'], ['Patricio Vergara Undurraga', 'finanzas'], ['Rubén Salinas Fuentealba', 'comercial'], ['Nelson Quinteros Aravena', 'gerente-ops'], ['Eduardo Kaufmann Vial', 'admin'], ['Cristián Mella Rojas', 'preventista'], ['Valeria Opazo Silva', 'preventista'], ['Manuel Gatica Ibáñez', 'conductor'], ['Rodrigo Poblete Aguilar', 'conductor'], ['Camila Fuentes Barra', 'finanzas'], ['Tomás Jara Valdés', 'planificador'], ['Daniela Bustos Leal', 'preventista'], ['Iván Leiva Moraga', 'conductor'], ['Paula Henríquez Soto', 'bodega'], ['Gonzalo Vidal Peña', 'preparador'], ['Lorena Cáceres Mora', 'calidad']];
  D.usuarios = personas.map(([n, r], i) => ({ id: `U-${1001 + i}`, nombre: n, rol: r, correo: n.split(' ')[0].toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '') + '.' + n.split(' ')[1].toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '') + '@puelche.cl', sitio: pick(['CD Talca', 'CD Concepción', 'Plataforma Curicó', 'Plataforma Chillán']), estado: i === 14 ? 'Suspendido' : i === 20 ? 'Pendiente' : 'Activo', mfa: ['bodega', 'calidad', 'planificador', 'finanzas', 'comercial', 'gerente-ops', 'cliente', 'cliente-moderno', 'transportista', 'proveedor', 'admin'].includes(r), ultimo: day(-int(0, 6), int(7, 20), int(0, 59)) }));

  const ops = [['Consulta', 'Lote', 'Trazabilidad del lote L2611-47 y clientes afectados · finalidad: simulacro de retiro'], ['Consulta', 'Cliente', 'Comportamiento de pago de Almacén Doña Rosa · finalidad: evaluación de crédito'], ['Consulta', 'Geolocalización', 'Posición del conductor de R-03 · finalidad: control de desvío'], ['Modificación', 'Parámetro', 'Umbral de bloqueo de crédito: 10 % → 12 %'], ['Creación', 'Usuario', 'Alta de conductor externo con OTP'], ['Aprobación', 'Ruta', 'Ruta R-04 aprobada con 3 correcciones'], ['Modificación', 'Pedido', 'Precio acordado conservado tras cambio de lista'], ['Eliminación', 'Sesión', 'Cierre de sesión forzado por inactividad'], ['Aprobación', 'Devolución', 'Destino «Reingreso a stock» aprobado'], ['Creación', 'Lote', 'Bloqueo preventivo por excursión térmica'], ['Exportación', 'Auditoría', 'Exportación CSV filtrada por período'], ['Modificación', 'Rol', 'Permiso «Aprobar» agregado a Jefatura de Bodega'], ['Creación', 'Rendición', 'Descuadre tipificado: vuelto mal entregado']];
  D.auditoria = Array.from({ length: 48 }, (_, i) => { const o = ops[i % ops.length]; const act = D.usuarios.filter((x) => x.estado === 'Activo'); const u = act[(i * 5) % act.length]; return { id: `AU-${90412 - i}`, fecha: day(-Math.floor(i / 6), 8 + (i % 11), (i * 13) % 60), persona: u.nombre, operacion: o[0], entidad: o[1], detalle: o[2], ip: `10.20.${int(1, 9)}.${int(10, 250)}`, origen: pick(['Consola web', 'App móvil', 'API', 'Portal de clientes']) }; });

  D.parametros = [
    { grupo: 'Crédito y cobranza', items: [{ id: 'cred-umbral', label: 'Umbral de bloqueo sobre límite de crédito', valor: 10, unidad: '%', rf: 'RF-03.09' }, { id: 'efectivo-max', label: 'Límite de efectivo a bordo por camión', valor: 800000, unidad: '$', rf: 'RF-06.05' }, { id: 'mora-dias', label: 'Días de mora para bloqueo', valor: 30, unidad: 'días', rf: 'RF-07.05' }] },
    { grupo: 'Cadena de frío', items: [{ id: 'frio-ref', label: 'Desviación crítica sobre la consigna en refrigerados', valor: 2, unidad: '°C por 15 min', rf: 'RF-09.05, RF-09.10' }, { id: 'anden-max', label: 'Tiempo máximo fuera de frío en andén', valor: 25, unidad: 'min', rf: 'RF-09.11' }] },
    { grupo: 'Rutas y entregas', items: [{ id: 'ventana', label: 'Ventana informada al cliente', valor: 30, unidad: 'min', rf: 'RF-04.06' }, { id: 'ocup-min', label: 'Ocupación mínima de camión al salir', valor: 70, unidad: '%', rf: 'RNG-14' }, { id: 'corte', label: 'Hora de corte para promesa 24 h', valor: '14:00', unidad: 'h', rf: 'RNG-15' }, { id: 'desvio', label: 'Alerta de desvío de ruta', valor: 3, unidad: 'km', rf: 'RF-14.03' }] },
    { grupo: 'Vida útil y FEFO', items: [{ id: 'vida-umbral', label: 'Alerta cuando la vida útil remanente baja de', valor: 30, unidad: 'días', rf: 'RF-02.09' }] },
    { grupo: 'Lectura de temperatura por tipo de producto', items: [{ id: 'lec-ref-cam', label: 'Refrigerados · cámara', valor: 5, unidad: 'min', rf: 'RF-09.03' }, { id: 'lec-con-cam', label: 'Congelados · cámara', valor: 5, unidad: 'min', rf: 'RF-09.03' }, { id: 'lec-ref-tru', label: 'Refrigerados · camión', valor: 15, unidad: 'min', rf: 'RF-09.04' }, { id: 'lec-con-tru', label: 'Congelados · camión', valor: 10, unidad: 'min', rf: 'RF-09.04' }] },
    { grupo: 'Sugerencias de preventa', items: [{ id: 'sug-hist', label: 'Peso del historial de compra', valor: 60, unidad: '%', rf: 'RF-03.14' }, { id: 'sug-promo', label: 'Peso de las promociones vigentes', valor: 40, unidad: '%', rf: 'RF-03.14' }, { id: 'sug-max', label: 'Sugerencias por cliente', valor: 3, unidad: 'productos', rf: 'RF-03.14' }] },
    { grupo: 'Envases retornables', items: [{ id: 'env-umbral', label: 'Saldo máximo de canastillos por cliente', valor: 40, unidad: 'u', rf: 'RF-08.04' }] },
    { grupo: 'Sesión y seguridad', items: [{ id: 'inact', label: 'Cierre por inactividad en portales y consolas no administrativas', valor: 30, unidad: 'min', rf: 'RF-12.29' }, { id: 'inact-admin', label: 'Cierre por inactividad en la sesión administrativa', valor: 15, unidad: 'min', rf: 'RF-15.01' }, { id: 'otp', label: 'Asignación firmada de reparto (máximo desde su emisión; vence 30 min tras el fin de ruta, sin renovación offline)', valor: 16, unidad: 'h', rf: 'RF-06.08' }] }
  ];

  /* ---------- Indicadores 2025 del caso (cap. 7) y serie simulada ---------- */
  D.kpis = [
    { id: 'otif', label: 'OTIF', value: 86.1, base: 82.4, meta: 95, unit: '%', good: 'up', rf: 'RF-11.03', desc: 'Pedidos completos y a tiempo sobre pedidos comprometidos.' },
    { id: 'fill', label: 'Fill rate', value: 93.2, base: 91.3, meta: 97, unit: '%', good: 'up', rf: 'RF-11.04', desc: 'Unidades entregadas sobre unidades pedidas.' },
    { id: 'reentregas', label: 'Reentregas', value: 3.1, base: 4.2, meta: 1, unit: '%', good: 'down', rf: 'RF-06.04', desc: 'Entregas que requieren una segunda visita.' },
    { id: 'ocupacion', label: 'Ocupación de camiones', value: 74, base: 68, meta: 85, unit: '%', good: 'up', rf: 'RF-11.05', desc: 'Volumen o peso utilizado por viaje despachado.' },
    { id: 'quiebre', label: 'Quiebre en preventa', value: 5.4, base: 7.8, meta: 2, unit: '%', good: 'down', rf: 'RF-03.01', desc: 'Líneas sin stock al momento de tomar el pedido.' },
    { id: 'descuadre', label: 'Descuadre mensual', value: 2.9, base: 4.2, meta: 0.5, unit: 'M$', good: 'down', rf: 'RF-07.03', desc: 'Diferencias de rendición sin causal tipificada.' }
  ];
  D.meses = ['Dic', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov'];
  D.serie = {
    otif: [81.6, 82.1, 82.9, 80.4, 82.7, 83.5, 84.0, 84.6, 85.1, 79.8, 85.4, 86.1],
    fill: [90.8, 91.0, 91.6, 90.2, 91.9, 92.1, 92.4, 92.7, 93.0, 90.5, 93.1, 93.2],
    reentregas: [4.4, 4.3, 4.1, 4.9, 4.0, 3.8, 3.6, 3.5, 3.3, 4.6, 3.2, 3.1],
    ocupacion: [66, 67, 69, 64, 68, 70, 71, 72, 73, 81, 73, 74],
    quiebre: [8.1, 7.9, 7.6, 8.4, 7.2, 6.9, 6.5, 6.2, 5.9, 7.1, 5.6, 5.4],
    descuadre: [4.4, 4.1, 3.9, 4.6, 3.8, 3.6, 3.5, 3.3, 3.2, 3.9, 3.0, 2.9],
    entregas: [29800, 27100, 25900, 31200, 30100, 30900, 29400, 30300, 31800, 52600, 33400, 34100]
  };
  D.causasRechazo = [{ label: 'Local cerrado', value: 41 }, { label: 'Faltante en preparación', value: 23 }, { label: 'Producto dañado', value: 14 }, { label: 'Fuera de ventana', value: 11 }, { label: 'Cadena de frío', value: 6 }, { label: 'Documento', value: 5 }];

  /* ---------- Bandeja de tareas (RF-17.07) y notificaciones ---------- */
  const ret = D.pedidos.find((p) => p.estado === 'Retenido');
  D.pedidoRetenido = ret.id;
  // Pedido con diferencia entre el importe a facturar y el precio pactado (RF-03.12)
  const difs = D.pedidos.filter((p) => L.difPrecio(p));
  const dif = difs[0] || D.pedidos[3];
  D.pedidoDifPrecio = dif.id;
  D.tareas = [
    { id: 'T-1', titulo: 'Autorizar pedido retenido por crédito', ref: ret.id, tipo: 'Aprobación', plazo: 'Hoy 12:00', prioridad: 'Alta', ruta: '/pedidos/' + ret.id, perfiles: ['finanzas', 'comercial', 'evaluador', 'gerente-ops'] },
    { id: 'T-2', titulo: 'Aprobar destino de devolución', ref: 'DV-5527', tipo: 'Aprobación', plazo: 'Hoy 17:00', prioridad: 'Media', ruta: '/devoluciones/DV-5527', perfiles: ['bodega', 'finanzas', 'evaluador', 'gerente-ops'] },
    { id: 'T-3', titulo: 'Resolver excursión crítica camión ' + D.camiones[3].camion, ref: D.camiones[3].ruta, tipo: 'Incidente', plazo: 'Ahora', prioridad: 'Crítica', ruta: '/telemetria', perfiles: ['calidad', 'evaluador', 'gerente-ops', 'planificador'] },
    { id: 'T-4', titulo: 'Revisar ruta propuesta para mañana', ref: 'Plan 14-11', tipo: 'Revisión', plazo: 'Hoy 16:00', prioridad: 'Alta', ruta: '/rutas', perfiles: ['planificador', 'evaluador', 'gerente-ops'] },
    { id: 'T-5', titulo: 'Tipificar descuadre de rendición', ref: 'Su ruta', tipo: 'Tarea', plazo: 'Hoy 19:00', prioridad: 'Media', ruta: '/rendicion', perfiles: ['finanzas', 'conductor', 'conductor-ext', 'evaluador'] },
    { id: 'T-6', titulo: 'Aprobar cambio de parámetro (segundo perfil)', ref: 'Umbral de crédito', tipo: 'Aprobación', plazo: 'Mañana', prioridad: 'Media', ruta: '/admin/parametros', perfiles: ['ti', 'evaluador'] },
    { id: 'T-7', titulo: 'Visitar Almacén Doña Rosa: saldo de envases sobre umbral', ref: 'CL-10021', tipo: 'Alerta', plazo: 'Esta semana', prioridad: 'Baja', ruta: '/clientes/CL-10021', perfiles: ['preventista', 'evaluador', 'comercial'] },
    { id: 'T-8', titulo: 'Confirmar recepción OC-88412 con lote faltante', ref: 'OC-88412', tipo: 'Tarea', plazo: 'Hoy 11:00', prioridad: 'Alta', ruta: '/recepcion', perfiles: ['bodega', 'preparador', 'evaluador'] },
    { id: 'T-9', titulo: 'Resolver 3 pedidos EDI en excepción', ref: 'Bandeja EDI', tipo: 'Excepción', plazo: 'Hoy 13:00', prioridad: 'Alta', ruta: '/canal-moderno', perfiles: ['comercial', 'evaluador'] },
    { id: 'T-10', titulo: 'Entrega reprogramada: confirme su ventana', ref: 'PV-264821', tipo: 'Aviso', plazo: 'Mañana 09:00', prioridad: 'Media', ruta: '/portal/entregas', perfiles: ['cliente', 'cliente-moderno'] },
    { id: 'T-11', titulo: 'Iniciar ruta R-01 Cauquenes (6 entregas)', ref: 'R-01', tipo: 'Tarea', plazo: 'Hoy 07:30', prioridad: 'Alta', ruta: '/terreno', perfiles: ['conductor', 'conductor-ext'] },
    { id: 'T-12', titulo: 'Misión M-3302: 42 líneas en zona refrigerada', ref: 'M-3302', tipo: 'Tarea', plazo: 'Turno noche', prioridad: 'Alta', ruta: '/preparacion', perfiles: ['preparador', 'bodega'] },
    { id: 'T-13', titulo: 'Confirmar conductor y vehículo de 3 rutas de mañana', ref: 'Despacho 14-11', tipo: 'Tarea', plazo: 'Hoy 18:00', prioridad: 'Alta', ruta: '/portal/transportista', perfiles: ['transportista', 'evaluador'] },
    { id: 'T-15', titulo: `Corregir diferencia de precio en ${difs.length} pedido(s) antes de facturar`, ref: dif.id, tipo: 'Alerta', plazo: 'Antes del cierre', prioridad: 'Alta', ruta: '/pedidos?precio=dif', perfiles: ['comercial', 'evaluador', 'finanzas'] },
    { id: 'T-16', titulo: 'Aprobar asignación conductor–vehículo–turno de 3 rutas de mañana', ref: 'Despacho 14-11', tipo: 'Aprobación', plazo: 'Hoy 18:30', prioridad: 'Alta', ruta: '/despacho/asignaciones', perfiles: ['gerente-ops', 'evaluador'] },
    { id: 'T-14', titulo: 'Revisar recepción de OC-88412 con 2 discrepancias', ref: 'OC-88412', tipo: 'Revisión', plazo: 'Mañana', prioridad: 'Media', ruta: '/portal/proveedor', perfiles: ['proveedor', 'evaluador'] }
  ];
  D.plan = { rutas: D.rutas.length, entregas: D.rutas.reduce((a, r) => a + r.paradas + 2, 0) };
  D.notificaciones = [
    { t: 'Excursión crítica en camión ' + D.camiones[3].camion, d: 'Lote retenido automáticamente. Calidad debe decidir.', kind: 'danger', ruta: '/telemetria', hace: 'hace 4 min' },
    { t: 'Ruta R-07 con desvío de 3,4 km', d: 'Molina · conductor Mauricio Toro · alerta al centro de control (Gerente de Operaciones)', kind: 'warning', ruta: '/telemetria', hace: 'hace 12 min' },
    { t: `Pedido ${ret.id} retenido por crédito`, d: 'Excede el límite en 14 %', kind: 'warning', ruta: '/pedidos/' + ret.id, hace: 'hace 25 min' },
    { t: 'Rutas de mañana generadas en 11 min', d: `${D.plan.rutas} rutas · ${L.fmt.n(D.plan.entregas)} entregas`, kind: 'success', ruta: '/rutas', hace: 'hace 1 h' },
    { t: 'Sincronización completa de 62 preventistas', d: '1.118 pedidos sin duplicados', kind: 'info', ruta: '/pedidos', hace: 'hace 2 h' }
  ];

  /* ---------- Canal moderno (M11) y recepción (M1) ---------- */
  D.edi = Array.from({ length: 12 }, (_, i) => ({ id: `EDI-${77120 + i}`, cadena: pick(['Supermercado Regional Maule', 'Cadena Sur Express', 'HiperCentro']), local: `Local ${int(1, 18)}`, lineas: int(12, 80), estado: i % 4 === 1 ? 'Excepción' : i % 4 === 3 ? 'Confirmado' : i % 4 === 2 ? 'Registrado' : 'Validado', causa: i % 4 === 1 ? pick(['Código GTIN no resuelto', 'Precio fuera de contrato', 'Local no registrado']) : '', recibido: day(0, 6 + (i % 6), (i * 11) % 60), ventana: pick(['07:00–07:30', '07:30–08:00', '08:00–08:30']) }));
  D.ocs = Array.from({ length: 8 }, (_, i) => ({ id: `OC-${88412 - i * 3}`, proveedor: pick(['Lácteos del Sur S.A.', 'Molinos del Maule', 'Bebidas Andinas', 'Cecinas Centinela', 'Frigorífico Ñuble', 'Limpieza Total Ltda.']), lineas: int(4, 22), estado: i === 0 ? 'En recepción' : i < 3 ? 'Programada' : 'Cerrada', anden: `Andén ${int(1, 8)}`, hora: `${String(6 + i).padStart(2, '0')}:00`, discrepancias: i === 4 ? 2 : 0 }));

  // Past deliveries of Almacén Doña Rosa, so her portal shows POD, tax documents and shipment temperature (RF-12.16, RF-12.17, RF-09.04).
  // Marked hist: they belong to earlier days and do not appear in today's route.
  [['PV-264790', -1, 'Rendido', 'Preventa'], ['PV-264733', -4, 'Entregado', 'Portal'], ['PV-264690', -8, 'Parcial', 'Preventa']].forEach(([id, d, estado, origen], k) => {
    const cli = D.clientes[0];
    const lineas = [[9, 24], [0, 20], [10, 36 - k * 6], [15, 6]].map(([pi, cant]) => { const p = D.productos[pi]; return { sku: p.sku, nombre: p.nombre, temp: p.temp, cant, precio: p.precio, lote: p.lote, vence: day(p.loteVence) }; });
    D.pedidos.push({ id, cliente: cli.id, clienteNombre: cli.nombre, canal: cli.canal, comuna: cli.comuna, preventista: cli.preventista, creado: day(d - 1, 11), entrega: day(d), ventana: cli.ventana, lineas, total: lineas.reduce((a, l) => a + l.cant * l.precio, 0), estado, ruta: 'R-01', origen, hist: true });
  });
  L.data = D;
  L.findClient = (id) => D.clientes.find((c) => c.id === id);
  L.findOrder = (id) => D.pedidos.find((p) => p.id === id);
  L.profile = (id) => D.profiles.find((p) => p.id === id);
})(window.LFX = window.LFX || {});
