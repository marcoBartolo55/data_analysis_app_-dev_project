// cine_effects.js - Efectos interactivos para el tema de cine
document.addEventListener('DOMContentLoaded', function() {
    console.log('Cine Effects cargado - Bienvenido a la experiencia cinematográfica');
    
    // Efectos para butacas interactivas
    const seats = document.querySelectorAll('.cine-seat:not(.occupied)');
    seats.forEach(seat => {
        seat.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.1)';
            this.style.boxShadow = '0 10px 20px rgba(210, 43, 43, 0.5)';
            this.style.zIndex = '10';
        });
        
        seat.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 3px 5px rgba(0, 0, 0, 0.3)';
            this.style.zIndex = '1';
        });
        
        seat.addEventListener('click', function() {
            // Alternar estado de selección
            if (!this.classList.contains('occupied')) {
                this.classList.toggle('selected');
                
                if (this.classList.contains('selected')) {
                    this.style.backgroundColor = 'var(--cinema-red)';
                    playSeatSound();
                    showSelectionToast('Butaca seleccionada');
                } else {
                    this.style.backgroundColor = 'var(--cinema-gray)';
                }
            }
        });
    });
    
    // Navegación activa con efecto de proyector
    const navLinks = document.querySelectorAll('.cine-nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Si no es un enlace activo, prevenir comportamiento por defecto
            if (!this.getAttribute('href').startsWith('http')) {
                e.preventDefault();
            }
            
            // Remover clase activa de todos los enlaces
            navLinks.forEach(item => {
                item.classList.remove('active');
                item.style.background = 'transparent';
            });
            
            // Agregar clase activa al enlace clickeado
            this.classList.add('active');
            
            // Efecto de "proyector" en el enlace activo
            const activeIndicator = this.querySelector('.cine-nav-indicator');
            if (activeIndicator) {
                activeIndicator.style.animation = 'pulse 1s ease-in-out';
                setTimeout(() => {
                    activeIndicator.style.animation = '';
                }, 1000);
            }
            
            // Mostrar nombre de la sección seleccionada
            const sectionName = this.querySelector('.cine-nav-text').textContent;
            showSectionTitle(sectionName);
        });
    });
    
    // Efecto de carga inicial
    setTimeout(() => {
        document.body.classList.add('loaded');
        
        // Animación de entrada para tarjetas
        const cards = document.querySelectorAll('.cine-card, .cine-feature');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 100 + (index * 100));
        });
        
        // Efecto de luz de proyector inicial
        const screen = document.querySelector('.cine-screen');
        if (screen) {
            screen.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.7), inset 0 0 30px rgba(210, 43, 43, 0.1)';
            
            setTimeout(() => {
                screen.style.transition = 'box-shadow 2s ease';
                screen.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.7), inset 0 0 60px rgba(210, 43, 43, 0.3)';
                
                setTimeout(() => {
                    screen.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.7), inset 0 0 30px rgba(210, 43, 43, 0.1)';
                }, 1000);
            }, 500);
        }
    }, 300);
    
    // Efecto de actualización de estadísticas
    function updateStats() {
        const statValues = document.querySelectorAll('.cine-stat-value');
        statValues.forEach(stat => {
            const originalValue = stat.textContent;
            const numericValue = parseInt(originalValue) || 0;
            
            // Efecto de conteo
            let count = 0;
            const increment = Math.ceil(numericValue / 20);
            const interval = setInterval(() => {
                count += increment;
                if (count >= numericValue) {
                    count = numericValue;
                    clearInterval(interval);
                }
                stat.textContent = count;
            }, 30);
        });
    }
    
    // Llamar a updateStats cuando sea necesario (por ejemplo, al cargar datos)
    window.updateCineStats = updateStats;
    
    // Funciones de utilidad
    function playSeatSound() {
        // En una implementación real, aquí se reproduciría un sonido
        console.log('Sonido de butaca reproducido');
    }
    
    function showSelectionToast(message) {
        // Crear y mostrar un toast de notificación
        const toast = document.createElement('div');
        toast.className = 'cine-toast';
        toast.textContent = message;
        toast.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: var(--cinema-red);
            color: white;
            padding: 12px 20px;
            border-radius: 5px;
            z-index: 1000;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            animation: fadeInOut 3s ease;
        `;
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
    
    function showSectionTitle(sectionName) {
        // Actualizar el título de la sección con efecto
        const titleElement = document.querySelector('.cine-title');
        if (titleElement) {
            const originalTitle = titleElement.textContent;
            
            titleElement.style.opacity = '0';
            titleElement.style.transform = 'translateY(-10px)';
            
            setTimeout(() => {
                titleElement.textContent = sectionName;
                titleElement.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
                titleElement.style.opacity = '1';
                titleElement.style.transform = 'translateY(0)';
                
                // Restaurar título original después de 2 segundos
                setTimeout(() => {
                    titleElement.style.opacity = '0';
                    titleElement.style.transform = 'translateY(-10px)';
                    
                    setTimeout(() => {
                        titleElement.textContent = originalTitle;
                        titleElement.style.opacity = '1';
                        titleElement.style.transform = 'translateY(0)';
                    }, 300);
                }, 2000);
            }, 300);
        }
    }
    
    // Efecto de scroll para revelar elementos
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('cine-visible');
            }
        });
    }, observerOptions);
    
    // Observar elementos para efectos de scroll
    document.querySelectorAll('.cine-card, .cine-feature, .cine-stat-card').forEach(el => {
        observer.observe(el);
    });
    
    // Añadir estilos para animaciones CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInOut {
            0% { opacity: 0; transform: translateY(10px); }
            15% { opacity: 1; transform: translateY(0); }
            85% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(-10px); }
        }
        
        .cine-visible {
            animation: fadeInUp 0.8s ease forwards;
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
        
        body.loaded {
            transition: opacity 0.5s ease;
        }
    `;
    document.head.appendChild(style);
});