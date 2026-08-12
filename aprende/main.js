// ========================================
// NAVBAR SCROLL STATE
// ========================================
const navbar = document.getElementById('navbar');
function updateNavbarScroll() {
  if (window.scrollY > 24) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}
window.addEventListener('scroll', updateNavbarScroll, { passive: true });
updateNavbarScroll();

// ========================================
// MOBILE NAV TOGGLE
// ========================================
const navToggle = document.getElementById('navToggle');
const navCta = document.querySelector('.navbar__cta');

navToggle.addEventListener('click', () => {
  const isOpen = navToggle.classList.toggle('active');
  navCta.style.display = isOpen ? 'inline-flex' : 'none';
  navToggle.setAttribute('aria-expanded', isOpen);
  navToggle.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
});

// ========================================
// VIDEO PLACEHOLDERS -> YOUTUBE EMBED
// ========================================
document.querySelectorAll('.video-placeholder').forEach((placeholder) => {
  const playBtn = placeholder.querySelector('.play-btn');
  const videoId = placeholder.getAttribute('data-video-id');
  if (!playBtn || !videoId) return;

  playBtn.addEventListener('click', () => {
    const inner = placeholder.querySelector('.video-inner');
    inner.innerHTML = `<iframe src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0" title="${placeholder.getAttribute('data-label') || 'Video'}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
  });
});

// ========================================
// WAITLIST MODAL
// ========================================
const modal = document.getElementById('waitlistModal');
const modalClose = document.getElementById('modalClose');

function openModal() {
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

document.querySelectorAll('[data-open-waitlist]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });
});

modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => {
  if (e.target === modal) closeModal();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
});
