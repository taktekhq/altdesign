/* altdesign motion, no dependencies. Load with <script defer src="motion.js"></script>.
   - [data-reveal]: rises 32px and fades in once as it enters (stagger children with data-reveal-delay="80").
   - [data-tagline]: the tagline section; each word brightens from 30% to full, in reading order, as it crosses 70% of the viewport.
   - [data-count="790"]: a number rolls up once when seen (keep the real number in the HTML for crawlers and screen readers).
   - [data-scrub-video]: a muted video whose time follows the scroll through its section (a "film" hero).
   Everything is visible without JS, and nothing moves under prefers-reduced-motion. */
(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');
  if (reduce) return;

  var once = function (els, fn, margin) {
    if (!('IntersectionObserver' in window)) { els.forEach(fn); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { fn(e.target); io.unobserve(e.target); } });
    }, { rootMargin: margin || '0px 0px -12% 0px' });
    els.forEach(function (el) { io.observe(el); });
  };
  var all = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  once(all('[data-reveal]'), function (el) {
    el.style.transitionDelay = (el.getAttribute('data-reveal-delay') || 0) + 'ms';
    el.classList.add('in');
  });

  all('[data-tagline]').forEach(function (block) {
    var words = [];
    block.querySelectorAll('[data-tagline] > *').forEach(function (line) { split(line, words); });
    if (!block.children.length) split(block, words);
    once(words, function (w) { w.classList.add('on'); }, '0px 0px -30% 0px');
  });
  function split(node, out) {
    var parts = node.textContent.trim().split(/\s+/);
    node.textContent = '';
    parts.forEach(function (t, i) {
      var s = document.createElement('span'); s.className = 'w'; s.textContent = t;
      node.appendChild(s); if (i < parts.length - 1) node.appendChild(document.createTextNode(' '));
      out.push(s);
    });
  }

  once(all('[data-count]'), function (el) {
    var to = parseFloat(el.getAttribute('data-count')), txt = el.textContent, pre = txt.match(/^[^\d]*/)[0];
    var t0 = performance.now(), dur = 1200;
    (function tick(t) {
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = pre + Math.round(to * e).toLocaleString('en-US');
      if (k < 1) requestAnimationFrame(tick); else el.textContent = txt;
    })(t0);
  });

  all('[data-scrub-video]').forEach(function (v) {
    var sec = v.closest('section') || v.parentNode, ticking = false;
    v.pause();
    function sync() {
      ticking = false;
      if (!v.duration) return;
      var r = sec.getBoundingClientRect(), span = r.height - innerHeight;
      var k = span > 0 ? Math.min(1, Math.max(0, -r.top / span)) : 0;
      v.currentTime = k * v.duration;
    }
    addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(sync); } }, { passive: true });
  });
})();
