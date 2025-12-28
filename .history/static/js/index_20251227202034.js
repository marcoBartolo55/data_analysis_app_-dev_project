// index.js - Efectos interactivos para el tema de cine
document.addEventListener('DOMContentLoaded', function() {
    console.log('Data Analysis Cinema - Iniciando efectos interactivos');
    
    // Menú hamburguesa
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('closeBtn');
    
    if (hamburgerBtn && sidebar) {
        hamburgerBtn.addEventListener('click', function() {
            sidebar.classList.add('active');
        });
    }
    
    if (closeBtn && sidebar) {
        closeBtn.addEventListener('click', function() {
            sidebar.classList.remove('active');
        });
    }
    
    // Cerrar sidebar al hacer clic en un enlace
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (sidebar) {
                sidebar.classList.remove('active');
            }
        });
    });
    
    // Cerrar sidebar al hacer clic fuera de él
    document.addEventListener('click', function(event) {
        if (sidebar && sidebar.classList.contains('active')) {
            if (!sidebar.contains(event.target) && !hamburgerBtn.contains(event.target)) {
                sidebar.classList.remove('active');
            }
        }
    });
    
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
    
    // 2. Efectos para butacas decorativas
    const seats = document.querySelectorAll('.seat');
    seats.forEach(seat => {
        seat.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.1)';
            this.style.backgroundColor = 'var(--cinema-accent)';
            this.style.boxShadow = '0 15px 25px rgba(255, 0, 0, 0.5)';
            playSeatSound();
        });
        
        seat.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.backgroundColor = 'var(--cinema-primary)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.3)';
        });
        
        seat.addEventListener('click', function() {
            // Efecto de selección
            this.classList.toggle('selected');
            
            if (this.classList.contains('selected')) {
                this.style.backgroundColor = 'var(--cinema-gold)';
                this.style.boxShadow = '0 0 20px rgba(255, 215, 0, 0.8)';
                showNotification('Butaca seleccionada');
            } else {
                this.style.backgroundColor = 'var(--cinema-primary)';
                this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.3)';
            }
        });
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
    
    // 6. Sistema de notificaciones tipo cine
    function showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'cinema-notification';
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-film"></i>
                <span>${message}</span>
            </div>
        `;
        
        // Estilos para la notificación
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(to right, var(--cinema-dark), var(--cinema-primary));
            color: white;
            padding: 15px 25px;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
            z-index: 1000;
            border-left: 4px solid var(--cinema-gold);
            transform: translateX(150%);
            transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        `;
        
        document.body.appendChild(notification);
        
        // Animación de entrada
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 10);
        
        // Auto-eliminar después de 3 segundos
        setTimeout(() => {
            notification.style.transform = 'translateX(150%)';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 500);
        }, 3000);
    }
    
    // 7. Simulación de sonido de butaca
    function playSeatSound() {
        // En una implementación real, usarías el Audio API
        // Por ahora, solo registro en consola
        console.log('🎬 Sonido de butaca de cine');
        
        // Crear elemento de audio (descomentar para usar sonidos reales)
        /*
        const audio = new Audio('/static/sounds/seat-click.mp3');
        audio.volume = 0.3;
        audio.play().catch(e => console.log('Error de audio:', e));
        */
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
    