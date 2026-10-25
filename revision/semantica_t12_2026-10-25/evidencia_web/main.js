(function () {
  "use strict";

  var prefersReducedMotion =
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Header: estado al hacer scroll ---------- */
  var header = document.querySelector("[data-header]");
  var setHeaderState = function () {
    if (header) header.classList.toggle("scrolled", window.scrollY > 12);
  };
  window.addEventListener("scroll", setHeaderState, { passive: true });
  setHeaderState();

  /* ---------- Menú móvil ---------- */
  var menuBtn = document.getElementById("menu-btn");
  var mainNav = document.getElementById("main-nav");

  var closeMenu = function () {
    mainNav.classList.remove("open");
    menuBtn.setAttribute("aria-expanded", "false");
    menuBtn.setAttribute("aria-label", "Abrir menú");
    document.body.style.overflow = "";
  };
  var toggleMenu = function () {
    var open = mainNav.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    menuBtn.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    document.body.style.overflow = open ? "hidden" : "";
    if (open) {
      var firstLink = mainNav.querySelector("a");
      if (firstLink) firstLink.focus();
    }
  };

  if (menuBtn && mainNav) {
    menuBtn.addEventListener("click", toggleMenu);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && mainNav.classList.contains("open")) closeMenu();
    });
    mainNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 900 && mainNav.classList.contains("open")) {
        closeMenu();
      }
    });
  }

  /* ---------- Aparición progresiva con stagger ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    revealEls.forEach(function (el) {
      var siblings = Array.prototype.slice
        .call(el.parentNode.children)
        .filter(function (n) {
          return n.classList && n.classList.contains("reveal");
        });
      var idx = siblings.indexOf(el);
      if (!prefersReducedMotion) {
        el.style.transitionDelay = Math.min(idx * 90, 450) + "ms";
      }
    });
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  /* ---------- Contadores de datos duros ---------- */
  var counters = document.querySelectorAll("[data-count]");
  var animateCount = function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0;
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 900;
    var start = null;
    var step = function (ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(target * eased).toLocaleString("es-CL") + suffix;
      if (progress < 1) window.requestAnimationFrame(step);
    };
    window.requestAnimationFrame(step);
  };

  if ("IntersectionObserver" in window) {
    var countObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            if (prefersReducedMotion) {
              var target = parseInt(entry.target.getAttribute("data-count"), 10) || 0;
              entry.target.textContent =
                target.toLocaleString("es-CL") + (entry.target.getAttribute("data-suffix") || "");
            } else {
              animateCount(entry.target);
            }
            countObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.6 }
    );
    counters.forEach(function (el) {
      countObserver.observe(el);
    });
  } else {
    counters.forEach(function (el) {
      el.textContent =
        (el.getAttribute("data-count") || "0") +
        (el.getAttribute("data-suffix") || "");
    });
  }

  /* ---------- Año dinámico ---------- */
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Validación de formularios ---------- */
  var MESSAGES = {
    nombre: function () {
      return "Escríbenos tu nombre.";
    },
    "nombre-corto": function () {
      return "El nombre tiene al menos 2 letras.";
    },
    correo: function () {
      return "Falta tu correo corporativo.";
    },
    "correo-bad": function () {
      return "El correo no se ve válido. Revisa el formato (nombre@empresa.cl).";
    },
    telefono: function () {
      return "Falta un teléfono de contacto.";
    },
    "telefono-bad": function () {
      return "El teléfono tiene al menos 7 dígitos.";
    },
    empresa: function () {
      return "Escribe el nombre de tu empresa.";
    },
    "empresa-corta": function () {
      return "El nombre de la empresa es muy corto.";
    },
    sector: function () {
      return "Elige el sector de tu operación.";
    },
    mensaje: function () {
      return "Cuéntanos brevemente qué necesitas.";
    },
    "mensaje-corto": function () {
      return "El mensaje es muy corto. Agrega un par de líneas.";
    },
    consent: function () {
      return "Necesitamos tu OK para contactarte.";
    },
  };

  var validator = {
    nombre: function (v) {
      if (!v) return MESSAGES.nombre();
      if (v.trim().length < 2) return MESSAGES["nombre-corto"]();
      return "";
    },
    empresa: function (v) {
      if (!v) return MESSAGES.empresa();
      if (v.trim().length < 2) return MESSAGES["empresa-corta"]();
      return "";
    },
    correo: function (v) {
      if (!v) return MESSAGES.correo();
      var re = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
      if (!re.test(v.trim())) return MESSAGES["correo-bad"]();
      return "";
    },
    telefono: function (v) {
      if (!v) return MESSAGES.telefono();
      if (v.replace(/\D/g, "").length < 7) return MESSAGES["telefono-bad"]();
      return "";
    },
    sector: function (v) {
      if (!v) return MESSAGES.sector();
      return "";
    },
    mensaje: function (v) {
      if (!v) return MESSAGES.mensaje();
      if (v.trim().length < 10) return MESSAGES["mensaje-corto"]();
      return "";
    },
    consent: function (v) {
      if (!v) return MESSAGES.consent();
      return "";
    },
  };

  var setupForm = function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstInvalid = null;

      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.type === "submit" || el.type === "checkbox" && el.name !== "consent") return;
        if (!el.required && el.name !== "consent") return;
        var check = validator[el.name];
        if (!check) return;
        var errSlot = form.querySelector('small[data-for="' + el.name + '"]');
        var message = check(el.value);
        if (message) {
          el.classList.add("invalid");
          if (errSlot) errSlot.textContent = message;
          if (!firstInvalid) firstInvalid = el;
        } else {
          el.classList.remove("invalid");
          if (errSlot) errSlot.textContent = "";
        }
      });

      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }

      form.querySelectorAll(".invalid").forEach(function (el) {
        el.classList.remove("invalid");
      });
      renderSuccess(form);
    });

    form.addEventListener("input", function (e) {
      var el = e.target;
      var check = validator[el.name];
      if (!check || !el.classList.contains("invalid")) return;
      var errSlot = form.querySelector('small[data-for="' + el.name + '"]');
      var message = check(el.value);
      if (!message) {
        el.classList.remove("invalid");
        if (errSlot) errSlot.textContent = "";
      }
    });

    form.querySelectorAll("select").forEach(function (sel) {
      sel.addEventListener("change", function () {
        if (sel.classList.contains("invalid")) {
          var check = validator[sel.name];
          var errSlot = form.querySelector('small[data-for="' + sel.name + '"]');
          var message = check(sel.value);
          if (!message) {
            sel.classList.remove("invalid");
            if (errSlot) errSlot.textContent = "";
          }
        }
      });
    });

    var consent = form.querySelector('input[name="consent"]');
    if (consent) {
      consent.addEventListener("change", function () {
        if (consent.classList.contains("invalid")) {
          consent.classList.remove("invalid");
          var errSlot = form.querySelector('small[data-for="consent"]');
          if (errSlot) errSlot.textContent = "";
        }
      });
    }
  };

  var renderSuccess = function (form) {
    var box = document.createElement("div");
    box.className = "form-success";
    if (form.classList.contains("quote-card")) box.classList.add("quote-card");
    box.setAttribute("role", "status");
    box.innerHTML =
      '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>' +
      '<path d="m9 11 3 3L22 4"/></svg>' +
      "<h3>Recibido. Hora de ponernos a trabajar.</h3>" +
      "<p>Tu solicitud ya está con un ingeniero de la mesa técnica. Respuesta en menos de 24 h hábiles.</p>" +
      '<a href="#casos">Mientras tanto, revisa los casos de éxito</a>';
    form.replaceWith(box);
  };

  var quoteForm = document.getElementById("quote-form");
  var contactForm = document.getElementById("contact-form");

  var bindErrorSlots = function (form) {
    form.querySelectorAll(".err").forEach(function (small) {
      var field = small.closest(".field");
      if (!field) return;
      var input = field.querySelector("input, select, textarea");
      if (input) small.setAttribute("data-for", input.name);
    });
  };

  if (quoteForm) {
    bindErrorSlots(quoteForm);
    setupForm(quoteForm);
  }
  if (contactForm) {
    bindErrorSlots(contactForm);
    setupForm(contactForm);
  }
})();