/* HDIP — small progressive-enhancement layer. No dependencies. */
(function () {
  'use strict';

  /* ---- Mobile nav ---- */
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      menu.classList.toggle('is-open', !open);
      document.body.style.overflow = !open ? 'hidden' : '';
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('is-open');
        document.body.style.overflow = '';
      }
    });
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) toggle.click();
    });
  }

  /* ---- Sticky header shadow ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Reveal on scroll + counters + bars ---- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;


  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('[data-reveal]').forEach(function (el) { el.classList.add('is-in'); });
    document.querySelectorAll('.bar > i').forEach(function (b) { b.style.transform = 'scaleX(' + (b.dataset.value / 100) + ')'; });
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      el.classList.add('is-in');
      el.querySelectorAll('.bar > i').forEach(function (b) { b.style.transform = 'scaleX(' + (b.dataset.value / 100) + ')'; });
      io.unobserve(el);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.15 });

  document.querySelectorAll('[data-reveal]').forEach(function (el, i) {
    el.style.transitionDelay = Math.min(i % 4, 3) * 70 + 'ms';
    io.observe(el);
  });
  document.querySelectorAll('.bar').forEach(function (el) {
    if (!el.closest('[data-reveal]')) io.observe(el);
  });


  /* ---- Current year in footer ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();

/* ---- Year switches (homepage impact, project phases) ---- */
(function () {
  'use strict';
  function wire(tabAttr, panelAttr) {
    var tabs = document.querySelectorAll('[' + tabAttr + ']');
    if (!tabs.length) return;
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var year = tab.getAttribute(tabAttr);
        var group = tab.closest('.yrswitch');
        var scope = group ? group.closest('section') || document : document;
        scope.querySelectorAll('[' + tabAttr + ']').forEach(function (t) {
          var on = t === tab;
          t.classList.toggle('is-on', on);
          t.setAttribute('aria-selected', String(on));
        });
        scope.querySelectorAll('[' + panelAttr + ']').forEach(function (p) {
          p.classList.toggle('is-on', p.getAttribute(panelAttr) === year);
        });
      });
    });
  }
  wire('data-year-tab', 'data-year-panel');
  wire('data-phase-tab', 'data-phase-panel');
})();

/* ---- Tab semantics: keep aria-selected / roving tabindex in sync, and
        support arrow-key navigation as the tablist pattern requires. ---- */
(function () {
  'use strict';
  document.querySelectorAll('.yrswitch[role="tablist"]').forEach(function (list) {
    var tabs = [].slice.call(list.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
      });
      tab.focus();
    }
    list.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      var rtl = document.documentElement.dir === 'rtl';
      var next = null;
      if (e.key === 'ArrowRight') next = tabs[i + (rtl ? -1 : 1)];
      else if (e.key === 'ArrowLeft') next = tabs[i + (rtl ? 1 : -1)];
      else if (e.key === 'Home') next = tabs[0];
      else if (e.key === 'End') next = tabs[tabs.length - 1];
      if (!next) return;
      e.preventDefault();
      next.click();
      select(next);
    });
    list.addEventListener('click', function (e) {
      var t = e.target.closest('[role="tab"]');
      if (t) select(t);
    });
  });
})();

/* ---- Hero slideshow ----------------------------------------------------
   Auto-advance is a convenience, never a requirement: the markup ships with
   slide one visible, the controls are revealed only here, and anything that
   moves on its own can be stopped (WCAG 2.2.2). It pauses on hover, on focus,
   when the tab is hidden, and when scrolled out of view; with reduced motion
   it never starts and the dots become a plain picker. */
(function () {
  'use strict';
  var INTERVAL = 6500;

  document.querySelectorAll('[data-slideshow]').forEach(function (box) {
    var slides = [].slice.call(box.querySelectorAll('.slide'));
    if (slides.length < 2) return;

    var ui = box.querySelector('.slideshow__ui');
    var toggle = box.querySelector('[data-toggle]');
    var dots = [].slice.call(box.querySelectorAll('.dot'));
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

    var i = 0, timer = null, stopped = false, hovered = false, visible = true;
    if (ui) ui.hidden = false;           // controls exist only with script

    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) {
        var on = k === i;
        s.classList.toggle('is-on', on);
        if (on) s.removeAttribute('aria-hidden');
        else s.setAttribute('aria-hidden', 'true');
      });
      dots.forEach(function (d, k) {
        d.classList.toggle('is-on', k === i);
        d.setAttribute('aria-current', String(k === i));
      });
    }

    function canRun() { return !stopped && !hovered && visible && !reduce.matches; }
    function tick() { show(i + 1); }
    function start() { clearInterval(timer); if (canRun()) timer = setInterval(tick, INTERVAL); }
    function halt() { clearInterval(timer); timer = null; }

    function setStopped(v) {
      stopped = v;
      if (toggle) {
        if (v) toggle.setAttribute('data-paused', '');
        else toggle.removeAttribute('data-paused');
        toggle.setAttribute('aria-label',
          toggle.dataset[v ? 'labelPlay' : 'labelPause']);
      }
      if (v) halt(); else start();
    }

    if (toggle) toggle.addEventListener('click', function () { setStopped(!stopped); });

    dots.forEach(function (d) {
      d.addEventListener('click', function () {
        show(parseInt(d.dataset.goto, 10));
        if (!stopped) start();            // restart the dwell on the new slide
      });
    });

    // Pause while the visitor is reading or interacting with it.
    box.addEventListener('mouseenter', function () { hovered = true; halt(); });
    box.addEventListener('mouseleave', function () { hovered = false; start(); });
    box.addEventListener('focusin', function () { hovered = true; halt(); });
    box.addEventListener('focusout', function () {
      if (!box.contains(document.activeElement)) { hovered = false; start(); }
    });

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) halt(); else start();
    });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) start(); else halt();
      }, { threshold: 0.2 }).observe(box);
    }

    // Reduced motion can be switched on mid-session.
    if (reduce.addEventListener) {
      reduce.addEventListener('change', function () { reduce.matches ? halt() : start(); });
    }

    show(0);
    start();
  });
})();

/* ---- Staggered reveals + counting figures -------------------------------
   Motion with a job: grids arrive as grids, and the figures tally so the
   numbers read as a result rather than as decoration. Everything respects
   prefers-reduced-motion and renders fully if the script never runs. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Opt in to the hidden-until-revealed styles only now that we can reveal them.
  document.documentElement.classList.add('js-anim');

  // Safety net: if the observer never fires — a background tab, a browser that
  // throttles it, anything unexpected — show everything rather than leave the
  // page blank.
  function revealAll() {
    document.querySelectorAll('[data-reveal], [data-stagger], .rule').forEach(function (e) {
      e.classList.add('is-in');
    });
  }
  window.addEventListener('load', function () { setTimeout(revealAll, 2500); });
  setTimeout(revealAll, 6000);

  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    [].slice.call(group.children).forEach(function (child, i) {
      child.style.setProperty('--i', Math.min(i, 8));
    });
  });

  function countUp(el) {
    if (el.dataset.counted) return;
    el.dataset.counted = '1';
    var raw = el.textContent.trim();
    var m = raw.match(/^(\D*)([\d,.]+)(.*)$/);
    if (!m) return;
    var pre = m[1], num = m[2], post = m[3];
    var decimals = (num.split('.')[1] || '').length;
    var target = parseFloat(num.replace(/,/g, ''));
    if (!isFinite(target)) return;
    var grouped = num.indexOf(',') > -1;
    if (reduce) return;                       // leave the final value in place
    var dur = 1100, t0 = null;
    function frame(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var v = target * (1 - Math.pow(1 - p, 3));
      var out = v.toFixed(decimals);
      if (grouped) out = Number(out).toLocaleString('en-US',
        { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
      el.textContent = pre + out + post;
      if (p < 1) requestAnimationFrame(frame);
      else el.textContent = raw;              // land exactly on the real value
    }
    requestAnimationFrame(frame);
  }

  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('[data-stagger]').forEach(function (e) { e.classList.add('is-in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add('is-in');
      en.target.querySelectorAll('[data-count]').forEach(countUp);
      io.unobserve(en.target);
    });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.15 });
  document.querySelectorAll('[data-stagger], .yrpanels, .rule').forEach(function (e) { io.observe(e); });

  // Re-tally when the visitor switches year.
  document.querySelectorAll('[data-year-tab]').forEach(function (tab) {
    tab.addEventListener('click', function () {
      setTimeout(function () {
        var panel = document.querySelector('.yrpanel.is-on');
        if (!panel) return;
        panel.querySelectorAll('[data-count]').forEach(function (el) {
          el.dataset.counted = ''; countUp(el);
        });
      }, 40);
    });
  });
})();

/* ---- Slideshow prev / next ---- */
(function () {
  'use strict';
  document.querySelectorAll('[data-slideshow]').forEach(function (box) {
    var slides = [].slice.call(box.querySelectorAll('.slide'));
    var dots = [].slice.call(box.querySelectorAll('.dot'));
    if (slides.length < 2) return;
    function step(dir) {
      var i = slides.findIndex(function (s) { return s.classList.contains('is-on'); });
      var next = (i + dir + slides.length) % slides.length;
      if (dots[next]) dots[next].click();      // reuse the existing transition path
    }
    var p = box.querySelector('[data-prev]'), n = box.querySelector('[data-next]');
    if (p) p.addEventListener('click', function () { step(-1); });
    if (n) n.addEventListener('click', function () { step(1); });
  });
})();

/* ---- Hero: open out as the visitor scrolls ------------------------------
   The hero rests as a rounded, inset panel and opens to full bleed over the
   first stretch of scroll. It drives a clip-path, so the element's box never
   changes and nothing below it reflows. Without this script the hero stays
   inset, which is a perfectly good resting state. */
(function () {
  'use strict';
  var hero = document.querySelector('.hero--full, .page-hero--media');
  if (!hero) return;

  var root = document.documentElement;
  var DIST = 280;                 // px of scroll to go from inset to full
  var last = -1, queued = false;

  function apply() {
    queued = false;
    var p = Math.min(Math.max(window.scrollY / DIST, 0), 1);
    p = p * p * (3 - 2 * p);      // ease the last few pixels so it settles
    if (Math.abs(p - last) < 0.004) return;
    last = p;
    root.style.setProperty('--hero-p', p.toFixed(3));
  }
  function onScroll() {
    // rAF is paused while the tab is hidden; coalescing through it there would
    // leave the clip stuck at a stale value, so apply directly in that case.
    if (document.hidden) { queued = false; apply(); return; }
    if (queued) return;
    queued = true;
    requestAnimationFrame(apply);
  }

  apply();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
})();

/* ---- Section rail -------------------------------------------------------
   A quick-navigation column pinned to the trailing edge: one marker per
   top-level section, labelled from that section's own heading, which scrolls
   to it on click and tracks the reading position on scroll.

   It is built here rather than in the templates so every page gets one from
   its own structure, and so a visitor without JS is never shown navigation
   that cannot work. It is a real <nav> of real links, so it is reachable by
   keyboard and announced as navigation; the markers themselves are decorative
   and the link text carries the name. */
(function () {
  'use strict';
  var main = document.getElementById('main');
  if (!main) return;

  var sections = [].slice.call(main.children).filter(function (el) {
    return el.tagName === 'SECTION';
  });
  if (sections.length < 3) return;          // not worth a rail

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var header = document.querySelector('.site-header');

  var items = [];
  sections.forEach(function (sec, i) {
    var head = sec.querySelector('h1, h2');
    var name = head ? head.textContent.trim().replace(/\s+/g, ' ') : '';
    if (!name) return;                      // a section with no heading has no name
    if (!sec.id) sec.id = 'sec-' + (i + 1);
    items.push({ sec: sec, name: name });
  });
  if (items.length < 3) return;

  var nav = document.createElement('nav');
  nav.className = 'rail';
  nav.setAttribute('aria-label', document.documentElement.lang === 'ar'
    ? 'أقسام الصفحة' : 'Page sections');

  var list = document.createElement('ul');
  items.forEach(function (it) {
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.href = '#' + it.sec.id;
    a.innerHTML = '<span class="rail__name"></span><span class="rail__dot" aria-hidden="true"></span>';
    a.querySelector('.rail__name').textContent = it.name;
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var top = it.sec.getBoundingClientRect().top + window.scrollY
              - (header ? header.getBoundingClientRect().height : 0) - 8;
      window.scrollTo({ top: Math.max(top, 0), behavior: reduce.matches ? 'auto' : 'smooth' });
      // Keep the address bar and the back button honest about where we are.
      history.replaceState(null, '', '#' + it.sec.id);
    });
    li.appendChild(a);
    list.appendChild(li);
    it.link = a;
  });
  nav.appendChild(list);
  document.body.appendChild(nav);

  /* Mark the section currently occupying the middle of the viewport. */
  function mark(active) {
    items.forEach(function (it) {
      var on = it === active;
      it.link.classList.toggle('is-on', on);
      if (on) it.link.setAttribute('aria-current', 'true');
      else it.link.removeAttribute('aria-current');
    });
  }

  var ticking = false;
  function update() {
    ticking = false;
    var mid = window.scrollY + window.innerHeight * 0.4;
    var current = items[0];
    items.forEach(function (it) {
      if (it.sec.offsetTop <= mid) current = it;
    });
    mark(current);
  }
  function onScroll() {
    if (document.hidden) { update(); return; }   // rAF is paused when hidden
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(update);
  }
  update();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
})();
