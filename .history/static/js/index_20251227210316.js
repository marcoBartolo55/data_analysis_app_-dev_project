// index.js - Efectos interactivos para el tema de cine
document.addEventListener('DOMContentLoaded', function() {
    console.log('Data Analysis Cinema - Iniciando efectos interactivos');
    
    // Menú hamburguesa
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('closeBtn');
    const overlay = document.getElementById('overlay');
    
    if (hamburgerBtn && sidebar) {
        hamburgerBtn.addEventListener('click', function() {
            const isActive = sidebar.classList.contains('active');
            sidebar.classList.toggle('active', !isActive);
            if (overlay) overlay.classList.toggle('active', !isActive);
            document.body.classList.toggle('menu-open', !isActive);
        });
    }
    
    if (closeBtn && sidebar) {
        closeBtn.addEventListener('click', function() {
            sidebar.classList.remove('active');
            if (overlay) overlay.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    }
    
    // Cerrar sidebar al hacer clic en un enlace
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (sidebar) {
                sidebar.classList.remove('active');
                if (overlay) overlay.classList.remove('active');
                document.body.classList.remove('menu-open');
            }
        });
    });
    
    // Cerrar usando el overlay
    if (overlay) {
        overlay.addEventListener('click', function() {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    }
    
    // 1. Efectos para la navegación
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            // Efecto de sonido de butaca (simulado)
            playSeatSound();
            
            // Efecto visual de resplandor
            link.style.boxShadow = '0 0 15px rgba(255, 0, 0, 0.5)';
        });
        
        link.addEventListener('mouseleave', function() {
            link.style.boxShadow = 'none';
        });
        
        // Indicador de página activa
        const currentPath = window.location.pathname;
        const linkPath = link.getAttribute('href');
        
        if (currentPath.includes(linkPath.replace('/', '')) || 
            (currentPath === '/' && linkPath.includes('index'))) {
            link.classList.add('active');
            link.style.backgroundColor = 'rgba(0, 0, 0, 0.6)';
            link.style.color = 'var(--cinema-gold)';
        }
    });
    
    // 3. Efecto de proyector en la pantalla
    const screen = document.querySelector('.cinema-screen');
    if (screen) {
        // Efecto de parpadeo intermitente
        setInterval(() => {
            screen.style.boxShadow = 
                '0 10px 20px rgba(0, 0, 0, 0.7), ' +
                'inset 0 0 50px rgba(255, 215, 0, 0.3)';
            
            setTimeout(() => {
                screen.style.boxShadow = 
                    '0 10px 20px rgba(0, 0, 0, 0.7), ' +
                    'inset 0 0 30px rgba(255, 215, 0, 0.1)';
            }, 300);
        }, 5000);
    }
    
    // 4. Efectos de entrada para las tarjetas
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 + (index * 200));
    });
    
    // 5. Efecto de título principal
    const mainTitle = document.querySelector('.content-area h1');
    if (mainTitle) {
        mainTitle.style.opacity = '0';
        mainTitle.style.transform = 'translateX(-20px)';
        
        setTimeout(() => {
            mainTitle.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            mainTitle.style.opacity = '1';
            mainTitle.style.transform = 'translateX(0)';
        }, 300);
    }
    
    // 8. Efecto de scroll para elementos
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observar elementos para animaciones al hacer scroll
    document.querySelectorAll('.feature-card, .cinema-screen').forEach(el => {
        observer.observe(el);
    });
    
    // 9. Inicializar animaciones CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes screenGlow {
            0%, 100% { box-shadow: 0 10px 20px rgba(0, 0, 0, 0.7), inset 0 0 30px rgba(255, 215, 0, 0.1); }
            50% { box-shadow: 0 10px 20px rgba(0, 0, 0, 0.7), inset 0 0 60px rgba(255, 215, 0, 0.3); }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animate-in {
            animation: fadeInUp 0.8s ease forwards;
        }
        
        .cinema-notification .notification-content {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .cinema-notification i {
            color: var(--cinema-gold);
        }
    `;
    
    document.head.appendChild(style);
});