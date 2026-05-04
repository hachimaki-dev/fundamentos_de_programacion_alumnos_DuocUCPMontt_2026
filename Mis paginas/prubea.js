<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
    // 1. INICIALIZACIÓN SEGURA DE PARTÍCULAS
    // Usamos un condicional para asegurar que el elemento existe antes de cargar
    if (document.getElementById('particles-js')) {
        particlesJS("particles-js", {
            "particles": {
                "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#FF5A00" }, 
                "shape": { "type": "circle" },
                "opacity": { "value": 0.3, "random": true },
                "size": { "value": 2, "random": true },
                "line_linked": { 
                    "enable": true, 
                    "distance": 150, 
                    "color": "#4264fb", 
                    "opacity": 0.2, 
                    "width": 1 
                },
                "move": { "enable": true, "speed": 1.5, "direction": "none", "out_mode": "out" }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { 
                    "onhover": { "enable": true, "mode": "grab" }, 
                    "onclick": { "enable": true, "mode": "push" } 
                }
            },
            "retina_detect": true
        });
    }

    // 2. INTERSECTION OBSERVER CORREGIDO
    // Esta función maneja la aparición y desaparición constante
    const setupRevealAnimations = () => {
        const observerOptions = {
            root: null, // usa el viewport
            threshold: 0.1, // se activa al ver el 10% del elemento
            rootMargin: "0px 0px -50px 0px" // evita que se active justo en el borde inferior
        };

        const revealCallback = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                } else {
                    // Quitamos la clase al salir para que la animación se repita
                    entry.target.classList.remove('active');
                }
            });
        };

        const observer = new IntersectionObserver(revealCallback, observerOptions);

        // Aplicamos el observador a todos los elementos con la clase .reveal
        const targets = document.querySelectorAll('.reveal');
        targets.forEach(target => observer.observe(target));
    };

    // 3. EJECUCIÓN AL CARGAR EL DOM
    // Asegura que todo el HTML esté listo antes de intentar animar
    document.addEventListener('DOMContentLoaded', () => {
        setupRevealAnimations();
        
        // Fix para el mapa (opcional): 
        // Si no tienes API Key, puedes cambiar el src a este formato estándar gratuito:
        const mapIframe = document.querySelector('.map-container iframe');
        if (mapIframe && mapIframe.src.includes('TU_API_KEY')) {
            mapIframe.src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11943.518178120353!2d-73.134114!3d-41.774431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9618179427e99763%3A0x62916b9996d83b0!2sCalbuco%2C%20Los%20Lagos!5e0!3m2!1ses!2scl!4v1700000000000!5m2!1ses!2scl";
        }
    });
</script>