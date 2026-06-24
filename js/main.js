function toggleMenu() {
  var nav = document.getElementById('navLinks');
  if (nav) nav.classList.toggle('open');
}

function initRecipeFilters() {
  var grid = document.getElementById('recipeGrid');
  var dishFilters = document.getElementById('dishFilters');
  var cookFilters = document.getElementById('cookFilters');

  if (!grid || !dishFilters || !cookFilters) return;

  var cards = grid.querySelectorAll('.recipe-card[data-category][data-cook]');
  if (!cards.length) return;

  var activeDish = 'all';
  var activeCook = 'all';

  function applyFilters() {
    dishFilters.querySelectorAll('.filter-tab-dish').forEach(function (tab) {
      tab.classList.toggle('active', tab.getAttribute('data-filter') === activeDish);
    });

    cookFilters.querySelectorAll('.filter-tab-cook').forEach(function (tab) {
      tab.classList.toggle('active', tab.getAttribute('data-cook') === activeCook);
    });

    cards.forEach(function (card) {
      var dishMatch = activeDish === 'all' || card.getAttribute('data-category') === activeDish;
      var cookMatch = activeCook === 'all' || card.getAttribute('data-cook') === activeCook;
      card.classList.toggle('is-filtered-out', !(dishMatch && cookMatch));
    });
  }

  function applyHash() {
    var hash = window.location.hash.slice(1);
    if (!hash) return;

    if (hash.indexOf('cook-') === 0) {
      var cookSlug = hash.slice(5);
      if (cookFilters.querySelector('[data-cook="' + cookSlug + '"]')) {
        activeCook = cookSlug;
      }
      return;
    }

    if (dishFilters.querySelector('[data-filter="' + hash + '"]')) {
      activeDish = hash;
    }
  }

  dishFilters.addEventListener('click', function (event) {
    var tab = event.target.closest('.filter-tab-dish');
    if (!tab) return;
    activeDish = tab.getAttribute('data-filter') || 'all';
    applyFilters();
  });

  cookFilters.addEventListener('click', function (event) {
    var tab = event.target.closest('.filter-tab-cook');
    if (!tab) return;
    activeCook = tab.getAttribute('data-cook') || 'all';
    applyFilters();
  });

  window.addEventListener('hashchange', function () {
    applyHash();
    applyFilters();
  });

  applyHash();
  applyFilters();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initRecipeFilters);
} else {
  initRecipeFilters();
}
