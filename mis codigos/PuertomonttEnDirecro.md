<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Transmisiones Deportivas Sur — Transmisiones deportivas en vivo | Sur de Chile</title>
<meta name="description" content="Transmisión en vivo de partidos de básquetbol y otros deportes en todo el sur de Chile. Locución pre-partido y fotografía de evento. Cotiza por WhatsApp.">
<meta property="og:title" content="Transmisiones Deportivas Sur">
<meta property="og:description" content="Transmisión en vivo de eventos deportivos en el sur de Chile, con foco en básquetbol.">
<meta property="og:image" content="assets/logo.png">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/logo.png">

<!-- Vue 3 (build global, producción) -->
<script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>

<!-- Tailwind CSS (Play CDN) -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          brand: {
            orange: '#EF6F5A',
            orangeDark: '#D85A45',
            orangeLight: '#FBE3DD'
          }
        },
        fontFamily: {
          heading: ['Poppins', 'sans-serif'],
          body: ['Inter', 'sans-serif']
        }
      }
    }
  }
</script>

<!-- Tipografías -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<!-- Iconos (Lucide) -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>

<!-- Animaciones al hacer scroll -->
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>

<!-- Carrusel (servicios en mobile) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Lightbox para la galería -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>

<style>
  /* Mínimo CSS manual: solo lo que Tailwind no resuelve */
  .font-heading{ letter-spacing: -0.01em; }
  /* Respeta accesibilidad: desactiva animaciones si el usuario lo prefiere */
  @media (prefers-reduced-motion: reduce) {
    [data-aos]{ transition: none !important; transform: none !important; opacity: 1 !important; }
    .animate-ping{ animation: none !important; }
  }
</style>
</head>

<body class="bg-white text-gray-900 font-body antialiased">

<div id="app">

  <!-- ===== NAVBAR ===== -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm shadow-sm">
    <div class="container mx-auto px-5 md:px-8 h-16 flex items-center justify-between">
      <a href="#inicio" class="flex items-center gap-2.5 min-w-0">
        <img src="assets/logo.png" alt="Logo" class="w-9 h-9 object-contain flex-shrink-0">
        <span class="font-heading font-extrabold text-base md:text-lg truncate">{{ business.nombre }}</span>
      </a>

      <nav class="hidden md:flex items-center gap-7">
        <a v-for="link in navLinks" :key="link.href" :href="link.href"
           class="text-sm font-medium text-gray-600 hover:text-brand-orange transition-colors">
          {{ link.label }}
        </a>
      </nav>

      <a :href="whatsappLink" target="_blank" rel="noopener"
         class="hidden md:inline-flex items-center gap-2 bg-brand-orange hover:bg-brand-orangeDark text-white font-semibold text-sm px-5 min-h-[44px] rounded-full transition-colors">
        <i data-lucide="message-circle" class="w-4 h-4"></i>
        WhatsApp
      </a>

      <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden p-2 -mr-2" aria-label="Abrir menú">
        <i :data-lucide="mobileMenuOpen ? 'x' : 'menu'" class="w-6 h-6"></i>
      </button>
    </div>

    <!-- Menú mobile -->
    <div v-show="mobileMenuOpen" class="md:hidden bg-white border-t border-gray-100 px-5 py-4 space-y-3">
      <a v-for="link in navLinks" :key="link.href" :href="link.href" @click="mobileMenuOpen = false"
         class="block text-base font-medium text-gray-700 py-1">
        {{ link.label }}
      </a>
      <a :href="whatsappLink" target="_blank" rel="noopener" @click="mobileMenuOpen = false"
         class="flex items-center justify-center gap-2 bg-brand-orange text-white font-semibold min-h-[44px] rounded-full mt-2">
        <i data-lucide="message-circle" class="w-4 h-4"></i> Cotizar por WhatsApp
      </a>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section id="inicio" class="relative bg-gray-900 pt-16">
    <div class="absolute inset-0 bg-cover bg-center" style="background-image:url('assets/foto-accion-1.png');"></div>
    <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/80 to-brand-orangeDark/40"></div>

    <div class="relative z-10 container mx-auto px-5 md:px-8 py-24 md:py-36 text-center md:text-left max-w-3xl">
      <span class="inline-flex items-center gap-2 bg-white/10 border border-white/20 text-white text-xs font-semibold px-3 py-1.5 rounded-full mb-5" data-aos="fade-up">
        <span class="relative flex h-2.5 w-2.5">
          <span class="absolute inline-flex h-full w-full rounded-full bg-brand-orange opacity-75 animate-ping"></span>
          <span class="relative inline-flex h-2.5 w-2.5 rounded-full bg-brand-orange"></span>
        </span>
        EN VIVO POR TODO EL SUR DE CHILE
      </span>

      <h1 class="font-heading font-extrabold text-4xl md:text-6xl text-white leading-tight mb-5" data-aos="fade-up" data-aos-delay="100">
        Transmisiones deportivas en vivo para todo el sur de Chile
      </h1>

      <p class="text-white/85 text-lg mb-8" data-aos="fade-up" data-aos-delay="200">
        Cobertura profesional de partidos de básquetbol y otras disciplinas, con locución pre-partido y fotografía del evento.
      </p>

      <div class="flex flex-col sm:flex-row gap-3 justify-center md:justify-start" data-aos="fade-up" data-aos-delay="300">
        <a :href="whatsappLink" target="_blank" rel="noopener"
           class="inline-flex items-center justify-center gap-2 bg-brand-orange hover:bg-brand-orangeDark text-white font-semibold min-h-[44px] px-6 rounded-full transition-colors">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          Cotizar por WhatsApp
        </a>
        <a href="#galeria"
           class="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 border border-white/30 text-white font-semibold min-h-[44px] px-6 rounded-full transition-colors">
          <i data-lucide="images" class="w-4 h-4"></i>
          Ver galería
        </a>
      </div>
    </div>
  </section>

  <!-- ===== SERVICIOS ===== -->
  <section id="servicios" class="py-20 bg-white">
    <div class="container mx-auto px-5 md:px-8">
      <div class="max-w-xl mx-auto text-center mb-12" data-aos="fade-up">
        <p class="text-brand-orange font-semibold text-sm tracking-wide uppercase mb-2">Servicios</p>
        <h2 class="font-heading font-bold text-3xl md:text-4xl mb-3">Lo que cubrimos en cada evento</h2>
        <p class="text-gray-500">Tres servicios pensados para que tu partido llegue a más gente, sin complicaciones.</p>
      </div>

      <div class="servicesSwiper overflow-hidden -mx-5 px-5 md:mx-0 md:px-0">
        <div class="swiper-wrapper md:!grid md:grid-cols-3 md:gap-6">
          <div v-for="servicio in services" :key="servicio.titulo" class="swiper-slide md:!w-auto h-auto">
            <div class="bg-white border border-gray-100 shadow-sm hover:shadow-md rounded-2xl p-7 h-full flex flex-col transition-shadow">
              <div class="w-12 h-12 bg-brand-orangeLight rounded-xl flex items-center justify-center mb-5">
                <i :data-lucide="servicio.icono" class="w-6 h-6 text-brand-orangeDark"></i>
              </div>
              <h3 class="font-heading font-bold text-lg mb-2">{{ servicio.titulo }}</h3>
              <p class="text-gray-500 text-sm flex-1 mb-5">{{ servicio.descripcion }}</p>
              <div class="flex items-baseline gap-1.5 pt-4 border-t border-gray-100">
                <span class="font-heading font-extrabold text-2xl text-brand-orangeDark">{{ servicio.precio }}</span>
                <span class="text-gray-400 text-xs">{{ servicio.nota }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="swiper-pagination relative mt-6 md:hidden"></div>
      </div>
    </div>
  </section>

  <!-- ===== GALERÍA ===== -->
  <section id="galeria" class="py-20 bg-brand-orangeLight/30">
    <div class="container mx-auto px-5 md:px-8">
      <div class="max-w-xl mx-auto text-center mb-12" data-aos="fade-up">
        <p class="text-brand-orange font-semibold text-sm tracking-wide uppercase mb-2">Galería</p>
        <h2 class="font-heading font-bold text-3xl md:text-4xl mb-3">Momentos que hemos cubierto</h2>
        <p class="text-gray-500">Algunas fotos de transmisiones y partidos anteriores.</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
        <a v-for="(foto, i) in gallery" :key="foto.src" :href="foto.src" :data-title="foto.alt"
           class="glightbox block rounded-xl overflow-hidden aspect-square group" data-gallery="galeria"
           data-aos="fade-up" :data-aos-delay="(i % 3) * 100">
          <img :src="foto.src" :alt="foto.alt" loading="lazy"
               class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
        </a>
      </div>
      <!-- Para agregar más fotos a futuro: solo suma objetos { src, alt } al array 'gallery' en data() -->
    </div>
  </section>

  <!-- ===== NOSOTROS ===== -->
  <section id="nosotros" class="py-20 bg-white">
    <div class="container mx-auto px-5 md:px-8">
      <div class="max-w-xl mx-auto text-center mb-12" data-aos="fade-up">
        <p class="text-brand-orange font-semibold text-sm tracking-wide uppercase mb-2">Por qué elegirnos</p>
        <h2 class="font-heading font-bold text-3xl md:text-4xl">Cercanos a la cancha, en todo el sur</h2>
      </div>

      <div class="grid sm:grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="(item, i) in whyUs" :key="item.titulo"
             class="text-center md:text-left" data-aos="fade-up" :data-aos-delay="i * 100">
          <div class="w-12 h-12 bg-brand-orangeLight rounded-xl flex items-center justify-center mb-4 mx-auto md:mx-0">
            <i :data-lucide="item.icono" class="w-6 h-6 text-brand-orangeDark"></i>
          </div>
          <h3 class="font-heading font-bold text-base mb-1.5">{{ item.titulo }}</h3>
          <p class="text-gray-500 text-sm">{{ item.descripcion }}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CONTACTO ===== -->
  <section id="contacto" class="py-20 bg-gray-900">
    <div class="container mx-auto px-5 md:px-8">
      <div class="grid md:grid-cols-2 gap-12 items-start max-w-4xl mx-auto">

        <div data-aos="fade-up">
          <p class="text-brand-orange font-semibold text-sm tracking-wide uppercase mb-2">Contacto</p>
          <h2 class="font-heading font-bold text-3xl text-white mb-4">Cotiza tu próxima transmisión</h2>
          <p class="text-white/70 mb-7">Escríbenos directo por WhatsApp o déjanos tus datos y te respondemos a la brevedad.</p>

          <a :href="whatsappLink" target="_blank" rel="noopener"
             class="inline-flex items-center gap-2 bg-brand-orange hover:bg-brand-orangeDark text-white font-semibold min-h-[44px] px-6 rounded-full transition-colors mb-5">
            <i data-lucide="message-circle" class="w-4 h-4"></i>
            Escribir por WhatsApp
          </a>

          <a :href="'mailto:' + business.email" class="flex items-center gap-2.5 text-white/80 hover:text-white text-sm">
            <i data-lucide="mail" class="w-4 h-4"></i>
            {{ business.email }}
          </a>
        </div>

        <form @submit.prevent="enviarFormulario" class="bg-white rounded-2xl p-6 md:p-7 space-y-4" data-aos="fade-up" data-aos-delay="150">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">Nombre</label>
            <input v-model="contactForm.nombre" type="text" required placeholder="Tu nombre"
                   class="w-full border border-gray-200 rounded-lg px-4 min-h-[44px] text-sm focus:outline-none focus:ring-2 focus:ring-brand-orange">
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">Servicio</label>
            <select v-model="contactForm.servicio" required
                    class="w-full border border-gray-200 rounded-lg px-4 min-h-[44px] text-sm focus:outline-none focus:ring-2 focus:ring-brand-orange">
              <option value="" disabled>Selecciona un servicio</option>
              <option v-for="servicio in services" :key="servicio.titulo" :value="servicio.titulo">{{ servicio.titulo }}</option>
              <option value="Otro">Otro</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">Mensaje</label>
            <textarea v-model="contactForm.mensaje" rows="3" placeholder="Cuéntanos sobre tu evento (fecha, lugar, deporte)"
                      class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-orange resize-none"></textarea>
          </div>
          <button type="submit"
                  class="w-full inline-flex items-center justify-center gap-2 bg-brand-orange hover:bg-brand-orangeDark text-white font-semibold min-h-[44px] rounded-lg transition-colors">
            <i data-lucide="send" class="w-4 h-4"></i>
            Enviar por WhatsApp
          </button>
        </form>

      </div>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer class="bg-gray-950 py-8">
    <div class="container mx-auto px-5 md:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-2.5">
        <img src="assets/logo.png" alt="Logo" class="w-7 h-7 object-contain">
        <span class="font-heading font-bold text-white text-sm">{{ business.nombre }}</span>
      </div>
      <p class="text-white/40 text-xs text-center">© {{ year }} {{ business.nombre }}. Todos los derechos reservados.</p>
      <a :href="'mailto:' + business.email" class="text-white/50 hover:text-white text-xs">{{ business.email }}</a>
    </div>
  </footer>

  <!-- Botón flotante de WhatsApp -->
  <a :href="whatsappLink" target="_blank" rel="noopener" aria-label="Cotizar por WhatsApp"
     class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-brand-orange hover:bg-brand-orangeDark text-white rounded-full shadow-lg flex items-center justify-center transition-colors">
    <i data-lucide="message-circle" class="w-6 h-6"></i>
  </a>

</div>

<script>
const { createApp } = Vue;

createApp({
  data() {
    return {
      mobileMenuOpen: false,
      year: new Date().getFullYear(),
      business: {
        nombre: 'Transmisiones Deportivas Sur', // ← cambia esto por tu nombre real cuando lo tengas
        whatsapp: '56979436564',
        email: 'matias.felipe7777@gmail.com'
      },
      navLinks: [
        { label: 'Inicio', href: '#inicio' },
        { label: 'Servicios', href: '#servicios' },
        { label: 'Galería', href: '#galeria' },
        { label: 'Nosotros', href: '#nosotros' },
        { label: 'Contacto', href: '#contacto' }
      ],
      services: [
        {
          icono: 'radio',
          titulo: 'Transmisión en vivo',
          descripcion: 'Cobertura en vivo de partidos de básquetbol y otras disciplinas deportivas, llevada directo a tu público.',
          precio: '$20.000',
          nota: 'CLP por partido'
        },
        {
          icono: 'mic',
          titulo: 'Presentación pre-partido',
          descripcion: 'Locución y presentación de equipos antes de que arranque el juego, para darle ambiente profesional al evento.',
          precio: '$5.000',
          nota: 'CLP por evento'
        },
        {
          icono: 'camera',
          titulo: 'Fotografía del evento',
          descripcion: 'Cobertura fotográfica del partido, contratable como adicional junto a la transmisión en vivo.',
          precio: 'Consultar',
          nota: 'agregado opcional'
        }
      ],
      // Para agregar más fotos: solo suma objetos { src, alt } a este array
      gallery: [
        { src: 'assets/foto-accion-1.png', alt: 'Jugador de básquetbol en acción, equipo verde y negro' },
        { src: 'assets/foto-accion-2.png', alt: 'Fotografía en blanco y negro de jugador en cancha, dorsal 13' }
      ],
      whyUs: [
        { icono: 'map-pin', titulo: 'Cobertura regional', descripcion: 'Cubrimos partidos en cualquier comuna del sur de Chile.' },
        { icono: 'trophy', titulo: 'Foco en básquetbol', descripcion: 'Especialistas en básquetbol, con experiencia también en otras disciplinas.' },
        { icono: 'signal', titulo: 'Calidad de transmisión', descripcion: 'Transmisión estable y prolija, pensada para que se vea profesional.' },
        { icono: 'camera', titulo: 'Fotografía como extra', descripcion: 'Suma fotografía del evento junto a tu transmisión en vivo.' }
      ],
      contactForm: {
        nombre: '',
        servicio: '',
        mensaje: ''
      }
    }
  },
  computed: {
    whatsappLink() {
      const texto = encodeURIComponent('Hola, quiero cotizar una transmisión');
      return `https://wa.me/${this.business.whatsapp}?text=${texto}`;
    }
  },
  methods: {
    enviarFormulario() {
      const partes = [
        `Hola, quiero cotizar una transmisión.`,
        `Nombre: ${this.contactForm.nombre}`,
        `Servicio: ${this.contactForm.servicio}`,
        this.contactForm.mensaje ? `Mensaje: ${this.contactForm.mensaje}` : null
      ].filter(Boolean);
      const texto = encodeURIComponent(partes.join('\n'));
      window.open(`https://wa.me/${this.business.whatsapp}?text=${texto}`, '_blank');
    }
  },
  mounted() {
    lucide.createIcons();

    AOS.init({ duration: 700, once: true, offset: 40 });

    new Swiper('.servicesSwiper', {
      slidesPerView: 1.1,
      spaceBetween: 16,
      pagination: { el: '.swiper-pagination', clickable: true },
      breakpoints: {
        768: { slidesPerView: 3, spaceBetween: 24, allowTouchMove: false }
      }
    });

    new GLightbox({ selector: '.glightbox' });
  }
}).mount('#app');
</script>

</body>
</html>hh