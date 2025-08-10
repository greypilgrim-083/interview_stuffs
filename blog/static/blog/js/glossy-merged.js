// glossy-merged.js
// Place in: blog/static/blog/js/glossy-merged.js
(function () {
  // parallax / shapes follow mouse (subtle)
  const shapes = document.querySelectorAll('.bg-shapes .shape');
  document.addEventListener('mousemove', (e) => {
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    shapes.forEach((s, i) => {
      const speed = (i + 1) * 6;
      const tx = (x - 0.5) * speed;
      const ty = (y - 0.5) * speed;
      s.style.transform = `translate(${tx}px, ${ty}px)`;
    });
  });

  // subtle scroll parallax of whole bg container
  const parallax = document.querySelector('.bg-shapes');
  window.addEventListener('scroll', () => {
    if (!parallax) return;
    const scrolled = window.pageYOffset;
    parallax.style.transform = `translateY(${scrolled * 0.2}px)`;
  });

  // ripple effect for clickable glass elements with class .glass
  document.querySelectorAll('.glass, .btn, .card').forEach(el => {
    el.addEventListener('click', function (e) {
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;
      const ripple = document.createElement('div');
      ripple.className = 'ripple';
      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });

  // simple client-side form success UI (only for non-submitted demo forms)
  document.querySelectorAll('form').forEach(f => {
    // don't override forms that have action - only add UX for forms with no action on demo pages
    if (f.getAttribute('data-no-demo') === '1') return;
    f.addEventListener('submit', function (e) {
      // If the form will actually make a real backend post, don't block it.
      if (this.getAttribute('action')) return;
      e.preventDefault();
      const msg = document.createElement('div');
      msg.style.cssText = 'position:fixed;left:50%;top:30%;transform:translateX(-50%);background:rgba(0,0,0,0.7);color:#fff;padding:14px 22px;border-radius:10px;z-index:9999';
      msg.textContent = 'Sent — we will get back to you soon.';
      document.body.appendChild(msg);
      setTimeout(() => msg.remove(), 2400);
      this.reset();
    });
  });
})();
