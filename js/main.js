function toggleMenu() {
  var nav = document.getElementById('navLinks');
  nav.classList.toggle('open');
}

document.addEventListener('DOMContentLoaded', function () {
  var dishTabs = document.querySelectorAll('.filter-tab-dish');
  var cookTabs = document.querySelectorAll('.filter-tab-cook');
  var cards = document.querySelectorAll('.recipe-card[data-category]');

  if (!cards.length) return;

  var activeDish = 'all';
  var activeCook = 'all';

  function applyFilters() {
    if (dishTabs.length) {
      dishTabs.forEach(function (t) {
        t.classList.toggle('active', t.getAttribute('data-filter') === activeDish);
      });
    }

    if (cookTabs.length) {
      cookTabs.forEach(function (t) {
        t.classList.toggle('active', t.getAttribute('data-cook') === activeCook);
      });
    }

    cards.forEach(function (card) {
      var dishMatch = activeDish === 'all' || card.getAttribute('data-category') === activeDish;
      var cookMatch = activeCook === 'all' || card.getAttribute('data-cook') === activeCook;
      card.style.display = dishMatch && cookMatch ? '' : 'none';
    });
  }

  dishTabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      activeDish = tab.getAttribute('data-filter');
      applyFilters();
    });
  });

  cookTabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      activeCook = tab.getAttribute('data-cook');
      applyFilters();
    });
  });

  var hash = window.location.hash.slice(1);
  if (hash) {
    if (hash.indexOf('cook-') === 0) {
      var cookSlug = hash.replace('cook-', '');
      if (document.querySelector('.filter-tab-cook[data-cook="' + cookSlug + '"]')) {
        activeCook = cookSlug;
      }
    } else if (document.querySelector('.filter-tab-dish[data-filter="' + hash + '"]')) {
      activeDish = hash;
    }
    applyFilters();
  }
});
