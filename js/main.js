function toggleMenu() {
  var nav = document.getElementById('navLinks');
  nav.classList.toggle('open');
}

document.addEventListener('DOMContentLoaded', function () {
  var tabs = document.querySelectorAll('.filter-tab');
  var cards = document.querySelectorAll('.recipe-card[data-category]');

  if (!tabs.length || !cards.length) return;

  function applyFilter(filter) {
    tabs.forEach(function (t) {
      t.classList.toggle('active', t.getAttribute('data-filter') === filter);
    });

    cards.forEach(function (card) {
      if (filter === 'all' || card.getAttribute('data-category') === filter) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      applyFilter(tab.getAttribute('data-filter'));
    });
  });

  var hash = window.location.hash.slice(1);
  if (hash && document.querySelector('.filter-tab[data-filter="' + hash + '"]')) {
    applyFilter(hash);
  }
});
