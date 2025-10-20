// Menu hamburger behavior: toggle, accessibility and close-on-outside
(function () {
    const btn = document.getElementById('menu-button');
    const menu = document.getElementById('main-menu');

    if (!btn || !menu) return;

    function openMenu() {
        btn.classList.add('open');
        menu.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
        btn.setAttribute('aria-label', 'Cerrar menú');
    }

    function closeMenu() {
        btn.classList.remove('open');
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-label', 'Abrir menú');
    }

    function toggleMenu() {
        const isOpen = btn.classList.contains('open');
        if (isOpen) closeMenu(); else openMenu();
    }

    btn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleMenu();
    });

    // Close when clicking outside the menu
    document.addEventListener('click', function (e) {
        const target = e.target;
        if (!menu.contains(target) && !btn.contains(target)) {
            closeMenu();
        }
    });

    // Close with Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            closeMenu();
            btn.focus();
        }
    });

    // Close when a menu link is clicked (mobile)
    menu.addEventListener('click', function (e) {
        if (e.target.tagName === 'A') {
            closeMenu();
        }
    });
})();
