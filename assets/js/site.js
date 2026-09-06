/* lucianomusella.com — web-v2 · nav, motion, embeds, tracking (sin dependencias) */
(function () {
  'use strict';
  var d = document, w = window;
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mobile = w.matchMedia('(max-width: 600px)').matches;

  /* ---------- atribución + tracking (dataLayer, sin proveedor) ---------- */
  var utm = {};
  try {
    var q = new URLSearchParams(location.search);
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach(function (k) { if (q.get(k)) utm[k] = q.get(k); });
    if (Object.keys(utm).length) sessionStorage.setItem('lm_utm', JSON.stringify(utm));
    else utm = JSON.parse(sessionStorage.getItem('lm_utm') || '{}');
    if (!localStorage.getItem('lm_first_touch')) {
      localStorage.setItem('lm_first_touch', JSON.stringify({ at: new Date().toISOString(), landing: location.pathname, referrer: d.referrer || 'direct', utm: utm }));
    }
    if (!sessionStorage.getItem('lm_sid')) sessionStorage.setItem('lm_sid', Math.random().toString(36).slice(2) + Date.now().toString(36));
  } catch (e) {}
  w.dataLayer = w.dataLayer || [];
  function track(event, props) {
    var p = Object.assign({ event: event, path: location.pathname, page_type: d.body.dataset.page || 'page', ts: Date.now() }, utm, props || {});
    try { p.session_id = sessionStorage.getItem('lm_sid'); p.first_touch = JSON.parse(localStorage.getItem('lm_first_touch') || 'null'); } catch (e) {}
    w.dataLayer.push(p);
    if (w.console && (location.hostname === 'localhost' || location.hostname === '127.0.0.1' || /vercel\.app$/.test(location.hostname))) console.log('[track]', event, p);
    if (typeof w.fbq === 'function' && p.fb_event) { try { w.fbq('trackCustom', p.fb_event, {}); } catch (e) {} }
  }
  w.lmTrack = track;
  track('page_view', d.body.dataset.pageProps ? JSON.parse(d.body.dataset.pageProps) : {});
  d.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (!el) return;
    var props = {};
    try { props = JSON.parse(el.getAttribute('data-track-props') || '{}'); } catch (err) {}
    props.href = el.getAttribute('href') || null;
    track(el.getAttribute('data-track'), props);
  });

  /* ---------- nav ---------- */
  var nav = d.querySelector('.nav'), hero = d.querySelector('.hero'), burger = d.querySelector('.burger'), menu = d.querySelector('.menu');
  var lastY = 0;
  function onScroll() {
    var y = w.scrollY;
    if (nav) {
      nav.classList.toggle('is-scrolled', y > 40);
      nav.classList.toggle('is-hidden', y > 400 && y > lastY && !(menu && menu.classList.contains('is-open')));
    }
    var prog = d.querySelector('.progress');
    if (prog) { var h = d.documentElement.scrollHeight - w.innerHeight; prog.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, y / h) : 0) + ')'; }
    lastY = y;
  }
  w.addEventListener('scroll', function () { w.requestAnimationFrame(onScroll); }, { passive: true });
  onScroll();
  if (hero && nav) {
    new IntersectionObserver(function (en) { nav.classList.toggle('is-light', en[0].isIntersecting && en[0].intersectionRatio > 0.15); }, { threshold: [0, 0.15, 0.5] }).observe(hero);
  }
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = !menu.classList.contains('is-open');
      menu.classList.toggle('is-open', open); burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', open); d.body.style.overflow = open ? 'hidden' : '';
      if (open) nav.classList.remove('is-hidden');
    });
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { menu.classList.remove('is-open'); burger.classList.remove('is-open'); d.body.style.overflow = ''; }); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('is-open')) burger.click(); });
  }
  /* item activo */
  var path = location.pathname;
  d.querySelectorAll('.nav__links a').forEach(function (a) {
    var h = a.getAttribute('href');
    if ((h === '/' && (path === '/' || path === '/index.html')) || (h !== '/' && path.indexOf(h) === 0)) a.classList.add('is-active');
  });

  /* ---------- hero: entrada + parallax + video ---------- */
  if (hero) {
    w.requestAnimationFrame(function () { setTimeout(function () { hero.classList.add('is-in'); }, 80); });
    var media = hero.querySelector('.hero__media'), vid = hero.querySelector('video');
    if (vid) {
      if (mobile || reduce) { vid.removeAttribute('autoplay'); vid.pause(); vid.style.display = 'none'; }
      else { vid.addEventListener('canplay', function () { hero.classList.add('has-video'); }); var p = vid.play(); if (p && p.catch) p.catch(function () {}); }
    }
    if (media && !reduce && !mobile) {
      var ticking = false;
      w.addEventListener('scroll', function () {
        if (ticking) return; ticking = true;
        w.requestAnimationFrame(function () {
          var y = Math.min(w.scrollY, hero.offsetHeight);
          media.style.transform = 'translate3d(0,' + (y * 0.12) + 'px,0)';
          ticking = false;
        });
      }, { passive: true });
    }
  }

  /* ---------- reveals ---------- */
  var rev = d.querySelectorAll('[data-reveal]');
  if (reduce) rev.forEach(function (el) { el.classList.add('is-in'); });
  else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    rev.forEach(function (el) { io.observe(el); });
  }

  /* ---------- tema del body según sección visible ---------- */
  var secs = d.querySelectorAll('[data-bg]');
  if (secs.length) {
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) d.body.dataset.theme = en.target.dataset.bg; });
    }, { threshold: 0.35 });
    secs.forEach(function (s) { tio.observe(s); });
  }

  /* ---------- filas horizontales ---------- */
  d.querySelectorAll('.row').forEach(function (row) {
    var sc = row.querySelector('.row__scroll'), prev = row.querySelector('[data-prev]'), next = row.querySelector('[data-next]');
    if (!sc) return;
    function step() { var c = sc.firstElementChild; return c ? c.getBoundingClientRect().width + 20 : 300; }
    function upd() { if (prev) prev.disabled = sc.scrollLeft < 8; if (next) next.disabled = sc.scrollLeft + sc.clientWidth > sc.scrollWidth - 8; }
    if (prev) prev.addEventListener('click', function () { sc.scrollBy({ left: -step() * 2, behavior: reduce ? 'auto' : 'smooth' }); });
    if (next) next.addEventListener('click', function () { sc.scrollBy({ left: step() * 2, behavior: reduce ? 'auto' : 'smooth' }); });
    sc.addEventListener('scroll', function () { w.requestAnimationFrame(upd); }, { passive: true });
    w.addEventListener('resize', upd); upd();
    /* arrastre con mouse en desktop */
    var down = false, sx = 0, sl = 0;
    sc.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; sx = e.clientX; sl = sc.scrollLeft; sc.style.scrollSnapType = 'none'; });
    w.addEventListener('pointermove', function (e) { if (!down) return; sc.scrollLeft = sl - (e.clientX - sx); });
    w.addEventListener('pointerup', function () { if (!down) return; down = false; sc.style.scrollSnapType = ''; });
  });

  /* ---------- embeds diferidos de YouTube ---------- */
  d.querySelectorAll('[data-yt]').forEach(function (ph) {
    ph.addEventListener('click', function (e) {
      e.preventDefault();
      var id = ph.getAttribute('data-yt');
      var f = d.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1';
      f.title = ph.getAttribute('data-title') || 'Video'; f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share'; f.allowFullscreen = true;
      f.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border:0';
      ph.style.position = 'relative'; ph.innerHTML = ''; ph.appendChild(f);
      track('video_started', { video_id: id, title: f.title });
    });
  });
  d.querySelectorAll('[data-video-view]').forEach(function (el) {
    var seen = false;
    new IntersectionObserver(function (en) { if (!seen && en[0].isIntersecting && en[0].intersectionRatio >= 0.5) { seen = true; track('video_view', { video_id: el.getAttribute('data-video-view') }); } }, { threshold: 0.5 }).observe(el);
  });

  /* ---------- botones copiar ---------- */
  d.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var pre = b.closest('.codeblock').querySelector('pre');
      var txt = pre ? pre.innerText : '';
      function done() { var t = b.innerHTML; b.classList.add('is-done'); b.textContent = 'Copiado ✓'; setTimeout(function () { b.classList.remove('is-done'); b.innerHTML = t; }, 1600); track('resource_copy', { block: b.getAttribute('data-i') }); }
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(done, done); else done();
    });
  });

  /* ---------- lectura de recurso: started / completed ---------- */
  var art = d.querySelector('.prose[data-resource]');
  if (art) {
    var slug = art.getAttribute('data-resource'), started = false, completed = false, t0 = Date.now();
    var end = d.createElement('div'); end.style.height = '1px'; art.appendChild(end);
    w.addEventListener('scroll', function () {
      if (started) return;
      var r = art.getBoundingClientRect(); var seen = (w.innerHeight - r.top) / r.height;
      if (seen > 0.25) { started = true; track('resource_started', { resource: slug }); }
    }, { passive: true });
    new IntersectionObserver(function (en) {
      if (!completed && en[0].isIntersecting && Date.now() - t0 > 3000) { completed = true; track('resource_completed', { resource: slug, read_seconds: Math.round((Date.now() - t0) / 1000) }); }
    }).observe(end);
  }

  /* ---------- formulario del reto (prototipo, sin backend) ---------- */
  d.querySelectorAll('form[data-proto]').forEach(function (form) {
    var startedF = false;
    form.addEventListener('focusin', function () { if (!startedF) { startedF = true; track('challenge_registration_started', { challenge: form.dataset.proto }); } });
    form.addEventListener('submit', function (e) {
      e.preventDefault(); var ok = true;
      form.querySelectorAll('[required]').forEach(function (i) {
        var f = i.closest('.field'); var bad = !i.value.trim() || (i.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(i.value));
        if (f) f.classList.toggle('is-error', bad); if (bad) ok = false;
      });
      if (!ok) { var first = form.querySelector('.is-error input'); if (first) first.focus(); return; }
      form.classList.add('is-done');
      track('challenge_registered', { challenge: form.dataset.proto, prototype: true });
    });
    form.querySelectorAll('input,select').forEach(function (i) { i.addEventListener('input', function () { var f = i.closest('.field'); if (f) f.classList.remove('is-error'); }); });
  });

  /* ---------- feedback físico en tap ---------- */
  d.addEventListener('pointerdown', function (e) { var b = e.target.closest('.btn,.chip,.card,.res,.route,.vitem,.coll__i,.show__i'); if (b) b.classList.add('is-pressed'); }, { passive: true });
  ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (ev) { d.addEventListener(ev, function () { d.querySelectorAll('.is-pressed').forEach(function (b) { b.classList.remove('is-pressed'); }); }, { passive: true }); });

  /* ---------- transición de página (fade) ---------- */
  if (!reduce) {
    d.body.style.opacity = '0'; d.body.style.transition = 'opacity .35s cubic-bezier(.32,.72,0,1)';
    w.requestAnimationFrame(function () { d.body.style.opacity = '1'; });
    d.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]'); if (!a) return;
      var h = a.getAttribute('href');
      if (!h || h.charAt(0) === '#' || a.target === '_blank' || /^(https?:)?\/\//.test(h) || e.metaKey || e.ctrlKey) return;
      e.preventDefault(); d.body.style.opacity = '0'; setTimeout(function () { location.href = h; }, 180);
    });
    w.addEventListener('pageshow', function (ev) { if (ev.persisted) d.body.style.opacity = '1'; });
  }
})();
