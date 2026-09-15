(() => {
  const video = document.getElementById('hero-trailer');
  const trailer = document.getElementById('trailer');
  const toggle = document.getElementById('trailer-toggle');
  const sound = document.getElementById('trailer-sound');
  const fullscreen = document.getElementById('trailer-fullscreen');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  video.muted = true;
  video.controls = false;
  [toggle, sound, fullscreen].forEach(button => button.hidden = false);
  const update = () => {
    toggle.textContent = video.paused ? 'Play' : 'Pause';
    sound.textContent = video.muted ? 'Sound off' : 'Sound on';
    sound.setAttribute('aria-pressed', String(!video.muted));
  };
  const play = () => video.play().catch(update);
  video.addEventListener('play', update);
  video.addEventListener('pause', update);
  video.addEventListener('volumechange', update);
  toggle.addEventListener('click', () => video.paused ? play() : video.pause());
  sound.addEventListener('click', () => { video.muted = !video.muted; update(); });
  const expanded = () => !!document.fullscreenElement || trailer.classList.contains('is-expanded');
  const updateFullscreen = () => { fullscreen.textContent = expanded() ? '⛶ Exit fullscreen' : '⛶ Fullscreen'; };
  const fallback = value => {
    trailer.classList.toggle('is-expanded', value);
    document.body.classList.toggle('expanded', value);
    updateFullscreen();
  };
  fullscreen.addEventListener('click', async () => {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else if (trailer.classList.contains('is-expanded')) fallback(false);
      else if (trailer.requestFullscreen) await trailer.requestFullscreen();
      else if (video.webkitEnterFullscreen) video.webkitEnterFullscreen();
      else fallback(true);
    } catch { fallback(!trailer.classList.contains('is-expanded')); }
    updateFullscreen();
  });
  document.addEventListener('fullscreenchange', updateFullscreen);
  document.addEventListener('keydown', event => { if (event.key === 'Escape') fallback(false); });
  if (!reduced.matches && !navigator.connection?.saveData) play();
  const chapters = [...document.querySelectorAll('.chapter')];
  const visible = new Set();
  let queued = false;
  const paint = () => {
    queued = false;
    if (reduced.matches) return;
    for (const chapter of visible) {
      const rect = chapter.getBoundingClientRect();
      const progress = Math.max(0, Math.min(1, (innerHeight - rect.top) / (innerHeight + rect.height)));
      chapter.style.setProperty('--shot-scale', (1 + .018 * Math.sin(progress * Math.PI)).toFixed(4));
    }
  };
  const schedule = () => { if (!queued && !reduced.matches) { queued = true; requestAnimationFrame(paint); } };
  if ('IntersectionObserver' in window) {
    document.documentElement.classList.add('motion-ready');
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) { entry.target.classList.add('in-view'); visible.add(entry.target); }
        else visible.delete(entry.target);
      }
      schedule();
    }, {threshold:0.06});
    chapters.forEach(chapter => observer.observe(chapter));
    window.addEventListener('scroll', schedule, {passive:true});
    window.addEventListener('resize', schedule, {passive:true});
  }
  reduced.addEventListener('change', () => {
    if (reduced.matches) { video.pause(); chapters.forEach(chapter => chapter.style.removeProperty('--shot-scale')); }
    else schedule();
  });
  update();
})();
