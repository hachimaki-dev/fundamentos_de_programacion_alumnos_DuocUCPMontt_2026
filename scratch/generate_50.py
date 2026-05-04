import json

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="../js/theme-engine.js"></script>
  <link rel="stylesheet" href="../css/themes.css" />
  <link rel="stylesheet" href="../css/utilities.css" />
  <title>🏋️‍♂️ 55 Desafíos de Lógica — Fundamentos 2026</title>
  <link rel="stylesheet" href="../css/main.css" />
  <style>
    .exercise-box {
      background: var(--t-glass-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 2px solid var(--t-glass-border);
      border-radius: var(--t-radius);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 8px 32px var(--t-shadow);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .exercise-box:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 40px var(--t-shadow-hover);
      border-color: var(--t-accent-subtle);
    }
    .exercise-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--t-accent);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .exercise-desc {
      margin-bottom: 1rem;
      line-height: 1.7;
      color: var(--t-text);
      font-size: 1.05rem;
    }
    .exercise-desc p { margin-bottom: 0.5rem; }
    .exercise-desc strong { color: var(--t-primary); font-weight: 700; }
    .code-output {
      background: var(--t-code-bg);
      color: var(--t-code-text);
      font-family: var(--t-font-code, 'Fira Code', monospace);
      padding: 1rem;
      border-radius: 0.8rem;
      margin-top: 0.5rem;
      white-space: pre-wrap;
      font-size: 0.95rem;
      border-left: 4px solid var(--t-purple);
    }
    .hint {
      background: var(--t-tip-bg);
      border: 1px solid var(--t-tip-border);
      color: var(--t-text);
      padding: 0.8rem 1rem;
      border-radius: 0.8rem;
      font-size: 0.95rem;
      margin-bottom: 1rem;
      display: flex;
      gap: 0.5rem;
      align-items: flex-start;
    }
    .hint::before { content: '💡'; font-size: 1.2rem; }
    
    /* Accordion styles */
    details > summary {
      list-style: none;
    }
    details > summary::-webkit-details-marker {
      display: none;
    }
    details[open] summary ~ * {
      animation: sweep .3s ease-in-out;
    }
    @keyframes sweep {
      0%    {opacity: 0; transform: translateY(-10px)}
      100%  {opacity: 1; transform: translateY(0)}
    }
    .danger-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.3rem 0.8rem;
      border-radius: 2rem;
      font-size: 0.75rem;
      font-weight: 900;
      margin-bottom: 1rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      60% { transform: translate(-3px, 1px) rotate(0deg); }
      70% { transform: translate(3px, 1px) rotate(-1deg); }
      80% { transform: translate(-1px, -1px) rotate(1deg); }
      90% { transform: translate(1px, 2px) rotate(0deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    #hell-bg-fixed {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none;
      z-index: -2;
      background: radial-gradient(circle at center 80%, rgba(50,0,0,0.8) 0%, rgba(10,0,0,0.95) 100%);
      opacity: 0;
      transition: opacity 0.1s;
    }
    #embers {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none;
      z-index: -1;
      background-image: 
        radial-gradient(circle, rgba(255,60,0,0.8) 2px, transparent 3px),
        radial-gradient(circle, rgba(255,0,0,0.6) 1px, transparent 2px);
      background-size: 100px 100px, 60px 60px;
      background-position: 0 0, 30px 30px;
      opacity: 0;
      animation: rise 15s linear infinite;
    }
    @keyframes rise {
      0% { background-position: 0 0, 30px 30px; }
      100% { background-position: 0 -100px, 30px -70px; }
    }
  </style>
</head>
<body class="min-h-screen relative overflow-x-hidden transition-colors duration-700">
  <div id="hell-bg-fixed"></div>
  <div id="embers"></div>
  <div class="bg-shape" style="width:300px;height:300px;background:var(--t-shape-1);top:10%;left:-5%;"></div>
  <div class="bg-shape" style="width:200px;height:200px;background:var(--t-shape-2);top:60%;right:-3%;"></div>
  <div class="bg-shape" style="width:250px;height:250px;background:var(--t-shape-3);bottom:5%;left:40%;"></div>
  <div class="bg-shape" style="width:180px;height:180px;background:var(--t-shape-4);top:30%;right:20%;"></div>

  <div class="relative z-10">
    <div class="page-container">
      <div class="page-header">
        <a href="../index.html" class="back-btn mb-4">← Volver al diario</a>
        <h1 class="text-3xl md:text-4xl font-bold text-kawaii-deep mt-4 mb-2">🏋️‍♂️ 55 Desafíos de Lógica</h1>
      </div>
    </div>
    
    <div class="max-w-5xl mx-auto px-4 pb-16 mt-2 space-y-8 fade-in-up">
    
      <div class="exercise-box !border-kawaii-primary !bg-kawaii-primary/5">
        <h3 class="font-bold text-xl text-kawaii-deep mb-3 flex items-center gap-2">🔥 Tu Misión: Convertirte en Leyenda</h3>
        <p class="text-[1.05rem] text-kawaii-text mb-4 leading-relaxed">
          Completar 55 ejercicios seguidos puede parecer una montaña imposible de escalar. ¡Pero te aseguro que tienes todo lo necesario para llegar a la cima! No te rindas, hazlos paso a paso. Al terminar esto, tu lógica de programación estará a otro nivel y dominarás el código.
        </p>
        
        <h4 class="font-bold text-kawaii-deep text-md mb-2 flex items-center gap-2">🛠️ Preparación en GitHub (Obligatorio)</h4>
        <p class="text-md text-kawaii-text mb-3">
          Antes de tirar tu primera línea de código, abre tu terminal en VSCode y crea tu propia rama en este repositorio usando el siguiente formato exacto:<br>
          Secciones válidas: <strong>001D, 002D, 003D, 405D, 004V</strong>
        </p>
        <div class="code-output text-sm py-3 mb-2 font-bold">git checkout -b EA2/TUSECCION_desafio55_TuNombre

<span class="text-gray-400 font-normal"># Ejemplo:</span>
git checkout -b EA2/001D_desafio55_CarlosPerez</div>
      </div>

      {content}
      
    </div>
    <footer class="site-footer mt-12">
      <div class="flex flex-col items-center justify-center gap-3">
        <p class="text-sm text-kawaii-text/60">Hecho con 💖 para Fundamentos de Programación 2026</p>
      </div>
    </footer>
  </div>
  <script src="../js/theme-selector.js"></script>
  <script>
    // RPG Hell Descent Script
    window.addEventListener('scroll', () => {
      const scrolled = window.scrollY;
      const maxScroll = document.body.scrollHeight - window.innerHeight;
      const factor = maxScroll > 0 ? Math.min(1, Math.max(0, scrolled / maxScroll)) : 0;
      
      const hellBg = document.getElementById('hell-bg-fixed');
      const embers = document.getElementById('embers');
      
      if (hellBg) {
        // Starts showing halfway, reaches max at bottom
        let opacity = 0;
        if (factor > 0.3) {
          opacity = (factor - 0.3) / 0.7;
        }
        hellBg.style.opacity = opacity;
      }
      
      if (embers) {
        // Embers appear near the end
        let eOpacity = 0;
        if (factor > 0.6) {
          eOpacity = (factor - 0.6) / 0.4;
        }
        embers.style.opacity = eOpacity;
      }
    });
  </script>
</body>
</html>
"""

exercises = [
    # Bloque 1
    {
        "title": "Liquidación de Sueldo Básico",
        "desc": "<p>Eres el contador de la empresa y debes calcular el sueldo de un empleado.</p><p><strong>Datos Iniciales:</strong> El sueldo base es 500000. El bono de colación es 50000 y el de movilización es 30000.</p><p><strong>Reglas de Negocio:</strong> Al empleado se le descuenta un 7% por salud y un 10% por AFP. Ojo: estos descuentos se calculan SÓLO sobre el sueldo base (los bonos no sufren descuentos). El sueldo líquido es el sueldo base más los bonos, menos los descuentos.</p><p><strong>Restricciones:</strong> Asigna todos los valores directamente en el código (no uses inputs). Imprime sólo el número final del sueldo líquido.</p>",
        "out": "495000.0"
    },
    {
        "title": "Proyección de Ahorro para un Auto",
        "desc": "<p>Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.</p><p><strong>Datos Iniciales:</strong> El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.</p><p><strong>Reglas de Negocio:</strong> Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.</p><p><strong>Restricciones:</strong> Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.</p>",
        "out": "23"
    },
    {
        "title": "Repartiendo la Cuenta en el Bar",
        "desc": "<p>Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.</p><p><strong>Datos Iniciales:</strong> Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).</p><p><strong>Reglas de Negocio:</strong> Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.</p><p><strong>Restricciones:</strong> Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.</p>",
        "out": "10450.0"
    },
    {
        "title": "Calculadora de Cuotas (MercadoLibre)",
        "desc": "<p>Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.</p><p><strong>Datos Iniciales:</strong> El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés. El envío a tu casa cuesta 15000.</p><p><strong>Reglas de Negocio:</strong> El envío no se paga en cuotas, se cobra completo junto con la primera cuota mensual del notebook.</p><p><strong>Restricciones:</strong> Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que deberás pagar ese primer mes.</p>",
        "out": "115000.0"
    },
    {
        "title": "Administrador de Carga Bip! Avanzado",
        "desc": "<p>Vas a hacer un seguimiento del saldo de tu tarjeta Bip! durante el día.</p><p><strong>Datos Iniciales:</strong> Tu tarjeta empieza con 10000. El pasaje de micro cuesta 730 y el de metro en punta cuesta 850. Además, harás una recarga de 3000.</p><p><strong>Reglas de Negocio:</strong> En el día tomas 1 micro y 2 metros. Después de esos viajes, recargas tu tarjeta.</p><p><strong>Restricciones:</strong> Usa una sola variable para el saldo y ve restándole o sumándole el dinero paso a paso. Imprime tu saldo al final del día.</p>",
        "out": "10570"
    },
    {
        "title": "Ganancia en Criptomonedas (Binance)",
        "desc": "<p>Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.</p><p><strong>Datos Iniciales:</strong> Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.</p><p><strong>Reglas de Negocio:</strong> Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.</p><p><strong>Restricciones:</strong> Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.</p>",
        "out": "540000.0"
    },
    {
        "title": "Armando el PC Gamer",
        "desc": "<p>Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.</p><p><strong>Datos Iniciales:</strong> Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).</p><p><strong>Reglas de Negocio:</strong> Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.</p><p><strong>Restricciones:</strong> Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.</p>",
        "out": "752500.0"
    },
    {
        "title": "Rendimiento de Servidor (AWS EC2)",
        "desc": "<p>Estás revisando cuánta memoria RAM le queda libre a tu servidor.</p><p><strong>Datos Iniciales:</strong> El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).</p><p><strong>Reglas de Negocio:</strong> Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).</p><p><strong>Restricciones:</strong> Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.</p>",
        "out": "8908.8"
    },
    {
        "title": "Costos de Producción (Emprendimiento)",
        "desc": "<p>Vas a vender poleras estampadas y necesitas calcular tus ganancias mensuales.</p><p><strong>Datos Iniciales:</strong> Vendes cada polera a 15000. Hacer una polera te cuesta: 4000 la tela, 2500 el estampado y 500 el empaque. Vendiste 50 poleras en el mes.</p><p><strong>Reglas de Negocio:</strong> La ganancia por cada polera es su precio de venta menos todo lo que te costó hacerla. La ganancia del mes es esa ganancia por unidad multiplicada por las poleras que vendiste.</p><p><strong>Restricciones:</strong> No escribas el resultado a mano, deja que Python haga las sumas y multiplicaciones. Imprime tu ganancia mensual final.</p>",
        "out": "400000"
    },
    {
        "title": "Estacionamiento Aeropuerto",
        "desc": "<p>Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.</p><p><strong>Datos Iniciales:</strong> Estacionar la primera hora cuesta 1200. Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.</p><p><strong>Reglas de Negocio:</strong> La primera hora se cobra a 1200. Las 2 horas que sobran equivalen a 4 bloques de media hora extra.</p><p><strong>Restricciones:</strong> Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.</p>",
        "out": "3200"
    },

    # Bloque 2
    {
        "title": "Clave Única Básico",
        "desc": "<p>Simula el ingreso a tu cuenta con una clave secreta.</p><p><strong>Datos Iniciales:</strong> Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.</p><p><strong>Reglas de Negocio:</strong> La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.</p><p><strong>Restricciones:</strong> Usa un bloque `if/else`. Como en este caso la clave está mal, imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos.</p>",
        "out": "Intentos fallidos: 1"
    },
    {
        "title": "Aprobación de Crédito (AND simple)",
        "desc": "<p>Revisa si un cliente cumple los requisitos del banco para pedir un crédito.</p><p><strong>Datos Iniciales:</strong> El cliente tiene un sueldo de 550000 y tiene 1 deuda activa.</p><p><strong>Reglas de Negocio:</strong> El banco exige DOS cosas a la vez: que el sueldo sea mayor a 500000 Y que la cantidad de deudas sea exactamente 0.</p><p><strong>Restricciones:</strong> Usa la palabra reservada `and` dentro de un `if` para revisar ambas cosas en la misma línea. Imprime `'Aprobado'` o `'Rechazado'`.</p>",
        "out": "Rechazado"
    },
    {
        "title": "Promoción VIP BancoEstado (OR y AND)",
        "desc": "<p>Revisa si un cliente puede subir a categoría VIP en su banco.</p><p><strong>Datos Iniciales:</strong> El cliente gana 800000, lleva 6 años en el banco y tiene 0 deudas.</p><p><strong>Reglas de Negocio:</strong> Eres VIP si cumples UNA de estas dos opciones: Opción A) Ganas más de 1000000. Opción B) Llevas 5 o más años en el banco Y tienes 0 deudas.</p><p><strong>Restricciones:</strong> Combina `or` y `and` en un mismo `if`. Usa paréntesis para agrupar la Opción B y que Python no se confunda. Imprime `'Cliente VIP'` o `'Cliente Normal'`.</p>",
        "out": "Cliente VIP"
    },
    {
        "title": "Sistema de Grados con Bonificación",
        "desc": "<p>Calcula si un alumno aprueba su ramo sumando un bono por asistencia.</p><p><strong>Datos Iniciales:</strong> Tienes un 3.6 de nota y un 85% de asistencia.</p><p><strong>Reglas de Negocio:</strong> Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos. Luego de aplicar el bono (o no), revisa tu estado: si tu nota final es 4.0 o más, estás 'Aprobado'. Si estás entre 3.5 y 3.9, vas a 'Examen'. Si tienes menos, estás 'Reprobado'.</p><p><strong>Restricciones:</strong> Usa un `if` para el bono y luego un bloque `if/elif/else` para definir el estado. Imprime solo el estado ('Aprobado', 'Examen' o 'Reprobado').</p>",
        "out": "Aprobado"
    },
    {
        "title": "Envíos MercadoLibre (Zonas Extremas)",
        "desc": "<p>Calcula cuánto debe pagar un cliente por el envío de su compra.</p><p><strong>Datos Iniciales:</strong> El cliente compró 25000 en productos y vive en la región de 'Magallanes'.</p><p><strong>Reglas de Negocio:</strong> Si la compra es mayor a 20000, el envío normal es gratis (0). Si es menor, cuesta 3000. Pero OJO: si el destino es 'Magallanes' o 'Aysen', siempre se suman 2000 extra al envío por ser zona extrema (incluso si era gratis).</p><p><strong>Restricciones:</strong> Haz un `if/else` para el costo base, y luego un `if` SEPARADO (no anidado) para sumar el recargo de zona extrema. Imprime solo el costo total del envío.</p>",
        "out": "2000"
    },
    {
        "title": "Plan de Datos WOM con Penalización",
        "desc": "<p>Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.</p><p><strong>Datos Iniciales:</strong> El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.</p><p><strong>Reglas de Negocio:</strong> A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').</p><p><strong>Restricciones:</strong> Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.</p>",
        "out": "3000"
    },
    {
        "title": "Multa Autopista por Tipo de Vehículo",
        "desc": "<p>Programa la cámara de la carretera para sacar multas según el vehículo.</p><p><strong>Datos Iniciales:</strong> Pasó un 'Camion' a 95 km/h.</p><p><strong>Reglas de Negocio:</strong> Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima'). Los camiones son más pesados y no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.</p><p><strong>Restricciones:</strong> Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) en la misma línea con un `and`. Imprime la multa correspondiente para el camión.</p>",
        "out": "Multa Grave Camión"
    },
    {
        "title": "Sistema Anti-Robo Inteligente (Smart Home)",
        "desc": "<p>Configura la alarma de tu casa para que suene solo cuando debe.</p><p><strong>Datos Iniciales:</strong> Hubo movimiento (`movimiento = True`). Son las 3 de la mañana (`hora = 3`). El dueño está en casa (`dueño_en_casa = True`).</p><p><strong>Reglas de Negocio:</strong> La alarma suena si se cumple ALGUNA de estas dos situaciones: Situación A: Hay movimiento y el dueño NO está en casa. Situación B: Hay movimiento y es de madrugada (antes de las 6 AM), no importa si el dueño está o no.</p><p><strong>Restricciones:</strong> Usa paréntesis para separar ambas situaciones con un `or` al medio. Imprime `'Alarma Sonando'` o `'Modo Silencioso'`.</p>",
        "out": "Alarma Sonando"
    },
    {
        "title": "Matchmaking por ELO (Juegos)",
        "desc": "<p>Busca un oponente justo para una partida en línea.</p><p><strong>Datos Iniciales:</strong> Tú tienes 1500 puntos. Encontraste un rival que tiene 1570 puntos.</p><p><strong>Reglas de Negocio:</strong> Para saber si la pelea es justa, hay que calcular la diferencia de puntos entre ambos. Si la diferencia es de 50 puntos o menos, la partida es 'Perfecta'. Si es de 100 o menos, es 'Justa'. Si la diferencia es mayor a 100, se debe mostrar 'Buscando otro rival...'.</p><p><strong>Restricciones:</strong> Usa la función matemática `abs(tus_puntos - sus_puntos)` para que el resultado siempre sea positivo, sin importar quién tenga más puntos. Imprime el resultado.</p>",
        "out": "Partida Justa"
    },
    {
        "title": "Simulador de Cajero: Retiro Complejo",
        "desc": "<p>El Mini-Boss: Haz que el cajero automático valide 3 reglas antes de dar dinero.</p><p><strong>Datos Iniciales:</strong> Tienes 50000 de saldo. Tu límite máximo diario para sacar plata es 200000. Quieres retirar 60000.</p><p><strong>Reglas de Negocio:</strong> Regla 1: Si lo que pides es más que tu límite diario, rechaza con 'Excede límite diario'. Regla 2: Si pides más de lo que tienes en el saldo, rechaza con 'Saldo insuficiente'. Regla 3: Si lo que pides no es múltiplo de 5000 (el cajero no da monedas), rechaza con 'Monto inválido'. Si pasas todas las reglas, 'Retiro exitoso'.</p><p><strong>Restricciones:</strong> Usa un bloque `if / elif / elif / else` para revisar regla por regla. Apenas falle una, debe imprimir el error y detenerse. Imprime el error de este caso.</p>",
        "out": "Saldo insuficiente"
    },

    # Bloque 3
    {
        "title": "Cuenta Regresiva Básica (SpaceX)",
        "desc": "<p>Crea el clásico reloj de cuenta regresiva para el despegue de un cohete.</p><p><strong>Datos Iniciales:</strong> Tienes un cronómetro que parte en 10.</p><p><strong>Reglas de Negocio:</strong> El reloj debe imprimir los números hacia atrás. Mientras el reloj sea mayor a cero, imprime el número actual y luego réstale 1. Cuando termine el tiempo, imprime 'Despegue 🚀'.</p><p><strong>Restricciones:</strong> No hagas trampa escribiendo diez `prints`. Tienes que usar un ciclo `while` para hacerlo de forma automática.</p>",
        "out": "10\\n9\\n8\\n7\\n6\\n5\\n4\\n3\\n2\\n1\\nDespegue 🚀"
    },
    {
        "title": "Ahorro Meta Mensual (PS5)",
        "desc": "<p>Simula tu chanchito de ahorros para saber cuántos meses te faltan para comprar una consola.</p><p><strong>Datos Iniciales:</strong> Tu alcancía parte en 0. Ahorras religiosamente 80000 todos los meses. La consola cuesta 450000.</p><p><strong>Reglas de Negocio:</strong> Cada mes que pasa, tú echas plata a la alcancía. Tienes que ir sumando hasta que tu ahorro iguale o supere el precio de la consola.</p><p><strong>Restricciones:</strong> Usa un ciclo `while`. Aumenta tu ahorro y suma 1 a tu contador de meses en cada vuelta. Imprime solo cuántos meses te tomó llegar a la meta.</p>",
        "out": "6"
    },
    {
        "title": "Bloqueo de Seguridad (Cajero)",
        "desc": "<p>Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.</p><p><strong>Datos Iniciales:</strong> Tienes un contador de intentos fallidos que parte en 0.</p><p><strong>Reglas de Negocio:</strong> Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.</p><p><strong>Restricciones:</strong> Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.</p>",
        "out": "Bloqueo de Tarjeta"
    },
    {
        "title": "Generador de Nombres (Instagram)",
        "desc": "<p>Vas a automatizar la creación de perfiles falsos para hacer pruebas.</p><p><strong>Datos Iniciales:</strong> La palabra base de todos los nombres será 'user_'.</p><p><strong>Reglas de Negocio:</strong> Necesitas generar exactamente 5 usuarios, numerados del 1 al 5. (ejemplo: user_1, user_2, etc).</p><p><strong>Restricciones:</strong> Usa un ciclo `for` con la herramienta `range()`. Recuerda que en Python, el `range` se detiene un número ANTES del final, así que ajusta el límite para que llegue a 5. Imprime los nombres generados en cada vuelta.</p>",
        "out": "user_1\\nuser_2\\nuser_3\\nuser_4\\nuser_5"
    },
    {
        "title": "Filtro de Palabras (Discord)",
        "desc": "<p>Crea un robot moderador de chat que censure insultos.</p><p><strong>Datos Iniciales:</strong> Tienes una lista de mensajes en el chat: `['hola', 'noob', 'genial', 'manco']`.</p><p><strong>Reglas de Negocio:</strong> El bot revisa las palabras una por una. Las palabras 'noob' y 'manco' están prohibidas. Si el bot ve una de esas palabras, debe cambiarla por el texto '[CENSURADO]'. Si la palabra es buena, la deja igual.</p><p><strong>Restricciones:</strong> Recorre la lista con un `for`. Adentro, usa un `if` para revisar si la palabra es mala e imprimir la censura, sino, imprime la palabra original.</p>",
        "hint": "Usa if palabra in ['noob', 'manco'] dentro del for.",
        "out": "hola\\n[CENSURADO]\\ngenial\\n[CENSURADO]"
    },
    {
        "title": "Procesar Cola de Impresión",
        "desc": "<p>Controla cuántas hojas le quedan a la impresora antes de imprimir un documento.</p><p><strong>Datos Iniciales:</strong> A la impresora le quedan 5 hojas. Mandaste a imprimir esto: `['TEXTO', 'FOTO', 'TEXTO', 'FOTO']`.</p><p><strong>Reglas de Negocio:</strong> Imprimir un 'TEXTO' gasta 1 hoja. Imprimir una 'FOTO' gasta 3 hojas. Antes de imprimir cada cosa, la impresora revisa si tiene hojas suficientes. Si se queda sin hojas, cancela todo y tira el mensaje 'Sin papel'.</p><p><strong>Restricciones:</strong> Resta las hojas que vas usando. Usa `break` para abortar la impresión si las hojas que te quedan son menos de las que necesitas. Imprime 'Imprimiendo [documento]' cuando sí alcance.</p>",
        "out": "Imprimiendo TEXTO\\nImprimiendo FOTO\\nImprimiendo TEXTO\\nSin papel"
    },
    {
        "title": "Saltar Errores del Sistema (Kiosko)",
        "desc": "<p>El sistema del almacén falló y guardó ventas negativas. Debes limpiar la caja.</p><p><strong>Datos Iniciales:</strong> Las ventas del día son: `[1500, -200, 5000, 0, 100]`. Tienes una variable total en 0.</p><p><strong>Reglas de Negocio:</strong> Evidentemente, una venta no puede ser menor o igual a 0. Esos son errores del sistema. Necesitas sumar todas las ventas buenas y simplemente IGNORAR las malas, sin detener el ciclo.</p><p><strong>Restricciones:</strong> Adentro de tu `for`, pon un `if` que detecte las ventas falsas y use la palabra mágica `continue` para saltárselas y pasar directo al siguiente número. Imprime la suma total limpia al final.</p>",
        "out": "6600"
    },
    {
        "title": "Búsqueda del Sospechoso (Cámaras)",
        "desc": "<p>La policía está buscando un auto robado en la lista de cámaras del peaje.</p><p><strong>Datos Iniciales:</strong> Las patentes que pasaron son: `['XY11', 'ZZ99', 'AB12', 'XX00']`. La policía busca la patente 'AB12'.</p><p><strong>Reglas de Negocio:</strong> El programa revisa patente por patente y va avisando en pantalla qué patente está mirando ('Buscando en XY11...'). Si encuentra la patente robada, dice 'Sospechoso encontrado' y DEJA DE BUSCAR (no tiene sentido mirar los autos que pasaron después).</p><p><strong>Restricciones:</strong> Usa un ciclo `for`. Apenas encuentres el auto, usa `break` para apagar la búsqueda. Imprime todo paso a paso.</p>",
        "out": "Buscando en XY11...\\nBuscando en ZZ99...\\nBuscando en AB12...\\nSospechoso encontrado"
    },
    {
        "title": "Simulación de Trote (Apple Watch)",
        "desc": "<p>Calcula cuánto rato te tomará quemar tus calorías del día trotando.</p><p><strong>Datos Iniciales:</strong> Tu meta es quemar 300 kcal. Empiezas desde el minuto 0.</p><p><strong>Reglas de Negocio:</strong> Los primeros 10 minutos tienes mucha energía y quemas 20 kcal por minuto. Del minuto 11 en adelante te cansas, así que empiezas a quemar solo 10 kcal por minuto. Tienes que sumar minutos y calorías hasta llegar a 300.</p><p><strong>Restricciones:</strong> Usa un `while`. Adentro, pon un `if/else` que revise cuántos minutos llevas para saber cuántas calorías sumar en esa vuelta. Imprime solo el total de minutos que tardaste.</p>",
        "out": "20"
    },
    {
        "title": "Procesamiento Resiliente (AWS)",
        "desc": "<p>El Mini-Boss: Haz un script que sepa qué hacer si se cae el servidor de tu página web.</p><p><strong>Datos Iniciales:</strong> Tienes una lista de códigos de respuesta web: `[200, 404, 500, 200, 500]`. Tienes solo 1 'reintento' salvavidas guardado en una variable.</p><p><strong>Reglas de Negocio:</strong> Un 200 es bueno (imprime 'Ok'). Un 404 no es grave (imprime 'No encontrado'). Pero un 500 significa que el servidor falló. Si sale un 500, gastas tu 'reintento' salvavidas (réstale 1) e imprime 'Reintentando'. PERO si te sale otro 500 y ya te quedaste sin reintentos, el sistema muere: imprime 'Servidor Caído' y cierra todo.</p><p><strong>Restricciones:</strong> Usa `for`. Usa un `if` para restarle a tus reintentos. Si el reintento es menor a 0, usa `break` para parar todo. Imprime cada mensaje en orden.</p>",
        "hint": "Resta 1 al contador al detectar un 500. Evalúa si el contador es menor a 0 antes de imprimir Reintentando.",
        "out": "Ok\\nNo encontrado\\nReintentando\\nOk\\nServidor Caído"
    },

    # Bloque 4
    {
        "title": "Armando la Playlist",
        "desc": "<p>Controla el orden en que se reproducen las canciones de tu playlist.</p><p><strong>Datos Iniciales:</strong> Tienes esta lista de canciones: `['B', 'C']`.</p><p><strong>Reglas de Negocio:</strong> El usuario apretó 'Agregar a la cola' en la canción 'D' (eso la manda al final). Luego apretó 'Reproducir siguiente' en la canción 'A' (eso la manda al inicio de todo, empujando a las demás).</p><p><strong>Restricciones:</strong> Usa la herramienta `.append()` para meter cosas al final de la lista. Usa `.insert(0, ...)` para obligar a una canción a ponerse en la posición cero (el principio). Imprime la lista completa al terminar.</p>",
        "out": "['A', 'B', 'C', 'D']"
    },
    {
        "title": "Moderador de Lobby (LoL)",
        "desc": "<p>Echa a un jugador tóxico de la sala de espera antes de empezar el juego.</p><p><strong>Datos Iniciales:</strong> Los jugadores en la sala son `['P1', 'Troll99', 'P2']`.</p><p><strong>Reglas de Negocio:</strong> Troll99 fue reportado y no puede jugar. Tienes que sacarlo de la lista para que la partida pueda empezar.</p><p><strong>Restricciones:</strong> No escribas la lista de nuevo a mano, eso es trampa. Usa la herramienta `.remove()` escribiendo exactamente el nombre del jugador que quieres borrar. Imprime la lista limpia.</p>",
        "out": "['P1', 'P2']"
    },
    {
        "title": "Últimos Vistos (YouTube)",
        "desc": "<p>Muestra el último video que vio el usuario en su perfil.</p><p><strong>Datos Iniciales:</strong> Tu historial está ordenado del más viejo al más nuevo: `['Intro', 'Tutorial', 'Gameplay']`.</p><p><strong>Reglas de Negocio:</strong> A nadie le importa lo primero que viste, quieren ver lo más reciente. Necesitas dar vuelta la lista para que lo más nuevo quede de primero, y luego mostrar solo ese video.</p><p><strong>Restricciones:</strong> Usa `.reverse()` para dar vuelta la lista físicamente. Luego, imprime solo el elemento que quedó en la posición `0`.</p>",
        "out": "Gameplay"
    },
    {
        "title": "Top Notas (Portal Alumno)",
        "desc": "<p>Encuentra tu mejor y peor nota del semestre rápidamente.</p><p><strong>Datos Iniciales:</strong> Tus notas finales fueron `[3.5, 6.2, 5.0, 2.1, 7.0]`.</p><p><strong>Reglas de Negocio:</strong> Necesitas encontrar la nota más alta y la más baja para ver si aplicas a una beca o si necesitas tutoría.</p><p><strong>Restricciones:</strong> No hagas ciclos manuales complicados. Python tiene dos herramientas que hacen esto por ti: `max()` y `min()`. Úsalas e imprime ambas notas separadas por un guion.</p>",
        "out": "7.0 - 2.1"
    },
    {
        "title": "Filtrar por Umbral (Banco)",
        "desc": "<p>Eres auditor del banco y necesitas separar las transferencias sospechosas.</p><p><strong>Datos Iniciales:</strong> Las transferencias del día fueron `[15000, 80000, 2000, 150000]`.</p><p><strong>Reglas de Negocio:</strong> Cualquier transferencia que sea mayor a 50000 pesos es considerada 'Alto Perfil' y debe ser separada en una lista especial para ser investigada. Las más chicas se ignoran.</p><p><strong>Restricciones:</strong> Crea una lista en blanco llamada `importantes`. Usa un `for` para recorrer las transferencias y, con un `if`, mete usando `.append()` solo las que cumplan la regla a tu nueva lista. Imprime la nueva lista.</p>",
        "out": "[80000, 150000]"
    },
    {
        "title": "Fusión de Servidores (Clústeres)",
        "desc": "<p>Junta los usuarios de dos servidores distintos sin crear cuentas duplicadas.</p><p><strong>Datos Iniciales:</strong> El Servidor 1 tiene a `['U1', 'U2']`. El Servidor 2 tiene a `['U2', 'U3']`.</p><p><strong>Reglas de Negocio:</strong> Tienes que pasar a los usuarios del Servidor 2 al Servidor 1. Pero OJO, el usuario 'U2' ya estaba en el Servidor 1. Si lo copias de nuevo, romperás el sistema. Solo copia a los que sean nuevos.</p><p><strong>Restricciones:</strong> Recorre el Servidor 2 con un `for`. Antes de agregar a un usuario, revisa si NO ESTÁ en el Servidor 1 usando la frase clave `not in`. Imprime cómo queda el Servidor 1 al final.</p>",
        "hint": "Usa if usuario not in servidor1:",
        "out": "['U1', 'U2', 'U3']"
    },
    {
        "title": "Multiplicador de Exp In-Place (RPG)",
        "desc": "<p>Aplica un evento de 'Doble Experiencia' a los puntajes de un jugador.</p><p><strong>Datos Iniciales:</strong> El jugador ganó esta experiencia en sus partidas: `[100, 200, 300]`.</p><p><strong>Reglas de Negocio:</strong> Es fin de semana de doble EXP. Tienes que tomar la lista original y multiplicar cada uno de sus números por 2, sobreescribiendo los valores antiguos.</p><p><strong>Restricciones:</strong> Para cambiar un número directamente dentro de una lista, necesitas saber su 'dirección' (su índice). Usa un `for` combinado con `range(len(lista))` para recorrer las posiciones. Sobreescribe multiplicando por 2 e imprime la lista modificada.</p>",
        "out": "[200, 400, 600]"
    },
    {
        "title": "Top 3 Ventas (MercadoLibre)",
        "desc": "<p>Muestra los 3 productos más vendidos de tu tienda virtual.</p><p><strong>Datos Iniciales:</strong> Tus productos vendieron estas cantidades: `[500, 1000, 200, 800, 1500]`.</p><p><strong>Reglas de Negocio:</strong> Para mostrar un 'Top 3', primero necesitas ordenar los números del más grande al más chico. Luego, simplemente recortas los primeros 3 y descartas el resto.</p><p><strong>Restricciones:</strong> Ordena la lista de mayor a menor usando `.sort(reverse=True)`. Después, usa la técnica de rebanado de listas (slicing) escribiendo `[:3]` para atrapar solo a los ganadores. Imprime esa rebanada.</p>",
        "out": "[1500, 1000, 800]"
    },
    {
        "title": "Limpieza de Formulario (Data Science)",
        "desc": "<p>Limpia los datos sucios que dejó la gente al llenar mal un formulario.</p><p><strong>Datos Iniciales:</strong> Recibiste estas respuestas: `['Juan', None, '', 'Ana', '   ']`.</p><p><strong>Reglas de Negocio:</strong> Solo sirven los nombres reales. Los espacios en blanco ('   '), las respuestas vacías ('') o los datos nulos (`None`) se consideran basura y hay que botarlos. Solo guarda los nombres válidos en una lista nueva.</p><p><strong>Restricciones:</strong> Recorre las respuestas. Usa `is not None` para asegurarte de que no sea nulo. Luego usa `.strip()` para borrarle los espacios extra y asegúrate de que no quede vacío `!= ''`. Si pasa las pruebas, guárdalo. Imprime la lista limpia.</p>",
        "hint": "Usa if elem is not None and elem.strip() != '':",
        "out": "['Juan', 'Ana']"
    },
    {
        "title": "Gestión de Inventario (Minecraft)",
        "desc": "<p>El Mini-Boss: Haz que el jugador no pueda recoger más cosas si su mochila está llena.</p><p><strong>Datos Iniciales:</strong> Tu mochila ya tiene `['mapa', 'espada']`. Solo puedes llevar 4 cosas máximo. En el piso encontraste `['madera', 'piedra', 'oro']`.</p><p><strong>Reglas de Negocio:</strong> El juego intenta recoger las cosas del piso una por una. Pero si en algún momento la mochila llega a 4 objetos, se llena, salta la alerta 'Lleno' y no puedes seguir recogiendo NADA MÁS del piso.</p><p><strong>Restricciones:</strong> Recorre las cosas del piso con un `for`. Agrégalas a tu mochila. Justo después de agregar, revisa si el largo (`len()`) de tu mochila es igual a 4. Si es así, imprime 'Lleno' y corta el ciclo con `break`. Al final, imprime cómo quedó tu mochila.</p>",
        "out": "Lleno\\n['mapa', 'espada', 'madera', 'piedra']"
    },

    # Bloque 5
    {
        "title": "Creación de Perfil Base",
        "desc": "<p>Crea el perfil de un jugador usando diccionarios (la mejor forma de guardar datos complejos).</p><p><strong>Datos Iniciales:</strong> Vas a crear un jugador nuevo.</p><p><strong>Reglas de Negocio:</strong> Un diccionario guarda datos en parejas (una 'llave' y su 'valor'). El jugador debe tener la llave `'nombre'` (pon tu nombre de valor) y la llave `'nivel'` (que parte en 1).</p><p><strong>Restricciones:</strong> Escribe el diccionario a mano usando las llaves `{}`. Luego, haz que Python extraiga tu nombre accediendo a la llave `'nombre'` usando corchetes. Imprime solo tu nombre.</p>",
        "out": "TuNombre"
    },
    {
        "title": "Actualización de Puntos (Wallet)",
        "desc": "<p>Súmale puntos de regalo a la cuenta de un cliente fiel.</p><p><strong>Datos Iniciales:</strong> El cliente tiene un diccionario con sus datos: `{'puntos': 1500}`.</p><p><strong>Reglas de Negocio:</strong> Por comprar hoy, el cliente se ganó 300 puntos extra. Tienes que sumárselos a los que ya tiene.</p><p><strong>Restricciones:</strong> No escribas el resultado final mentalmente (eso es trampa). Dile a Python que vaya a la llave `'puntos'` y le sume `+ 300` a lo que sea que haya adentro. Imprime el diccionario completo para ver el cambio.</p>",
        "out": "{'puntos': 1800}"
    },
    {
        "title": "Alta de Medio de Pago",
        "desc": "<p>Guarda la nueva tarjeta de crédito del usuario en su base de datos.</p><p><strong>Datos Iniciales:</strong> El usuario tiene su billetera vacía: `pagos = {}`.</p><p><strong>Reglas de Negocio:</strong> Acaba de inscribir su tarjeta Visa. Hay que meter ese nuevo dato al diccionario.</p><p><strong>Restricciones:</strong> Para agregar cosas a un diccionario, solo inventa una llave nueva y ponle un valor. Crea la llave `'visa'` y asígnale el texto `'activa'`. Imprime el diccionario para comprobar.</p>",
        "out": "{'visa': 'activa'}"
    },
    {
        "title": "Baja de Suscripción",
        "desc": "<p>Borra la suscripción que el usuario acaba de cancelar para que no le cobren más.</p><p><strong>Datos Iniciales:</strong> Tus cobros mensuales son: `{'spotify': 4000, 'netflix': 7000}`.</p><p><strong>Reglas de Negocio:</strong> Ya no quieres pagar Spotify. Hay que borrarlo del registro.</p><p><strong>Restricciones:</strong> Usa la palabra reservada `del` seguida de la llave que quieres matar (ej. `del diccionario['llave']`), o usa la herramienta `.pop()`. Imprime cómo quedaron tus cuentas.</p>",
        "out": "{'netflix': 7000}"
    },
    {
        "title": "Validación de Existencia (Criptos)",
        "desc": "<p>Evita que la aplicación explote revisando si el usuario tiene una criptomoneda antes de cobrarle.</p><p><strong>Datos Iniciales:</strong> El usuario tiene: `{'BTC': 0.5, 'ETH': 2.0}`.</p><p><strong>Reglas de Negocio:</strong> El usuario quiere comprar algo pagando con Solana ('SOL'). Si le intentas cobrar algo que no existe en su diccionario, Python tirará un error feo y la app se cerrará. Tienes que revisar primero.</p><p><strong>Restricciones:</strong> Usa la palabra mágica `in` dentro de un `if` para preguntar si `'SOL'` existe en las llaves del diccionario. Si está, imprime 'Procesando'. Si no, imprime 'Moneda no soportada'.</p>",
        "out": "Moneda no soportada"
    },
    {
        "title": "Suma de Ventas (Cornershop)",
        "desc": "<p>Suma todas las ganancias de los locales sin importar cómo se llamen.</p><p><strong>Datos Iniciales:</strong> Las ventas son: `{'LocalA': 150, 'LocalB': 300, 'LocalC': 100}`.</p><p><strong>Reglas de Negocio:</strong> A la gerencia no le importa qué local vendió qué cosa, solo quieren saber cuánta plata se hizo en total.</p><p><strong>Restricciones:</strong> No uses la función rápida `sum()`. Extrae solamente los números usando la herramienta `.values()` y súmalos uno por uno adentro de un ciclo `for`. Imprime el total.</p>",
        "out": "550"
    },
    {
        "title": "Sistema de Daño Condicional RPG",
        "desc": "<p>Programa la vida y la muerte de un jefe de videojuego usando un diccionario.</p><p><strong>Datos Iniciales:</strong> El jefe es `boss = {'hp': 100, 'estado': 'vivo'}`.</p><p><strong>Reglas de Negocio:</strong> Le pegaste un golpe crítico de 150 de daño (réstaselo a su 'hp'). El problema es que en matemáticas eso daría -50 de vida, pero en un juego no puedes tener vida negativa. Si la vida baja de 0, tienes que dejarla en exactamente 0 y cambiar su 'estado' a 'muerto'.</p><p><strong>Restricciones:</strong> Resta la vida. Luego usa un `if` para revisar si la vida quedó en menos de cero. Si es así, sobreescribe las dos llaves del diccionario con los nuevos valores. Imprime al jefe.</p>",
        "hint": "Evalúa el HP modificado con un if.",
        "out": "{'hp': 0, 'estado': 'muerto'}"
    },
    {
        "title": "Merge de Perfiles de Usuario",
        "desc": "<p>Junta los datos de tu aplicación con los datos que descargaste desde Google.</p><p><strong>Datos Iniciales:</strong> Tus datos locales: `{'id': 1}`. Los datos que mandó Google: `{'email': 'a@a.cl', 'foto': 'url'}`.</p><p><strong>Reglas de Negocio:</strong> El perfil del usuario necesita tener todo mezclado en un solo lugar para funcionar bien en la pantalla.</p><p><strong>Restricciones:</strong> Usa la herramienta `.update()` para inyectarle de un solo golpe todo el diccionario de Google a tu diccionario local. Imprime cómo quedó el diccionario mezclado.</p>",
        "out": "{'id': 1, 'email': 'a@a.cl', 'foto': 'url'}"
    },
    {
        "title": "Verificación de Permisos (AWS)",
        "desc": "<p>Aprende a meterte dentro de un diccionario que tiene otro diccionario adentro (datos anidados).</p><p><strong>Datos Iniciales:</strong> Los permisos del usuario son: `admin = {'rol': 'dev', 'permisos': {'S3': True, 'EC2': False}}`.</p><p><strong>Reglas de Negocio:</strong> El usuario quiere prender un servidor 'EC2'. Tienes que revisar en sus permisos si tiene la autorización (True o False) para hacerlo.</p><p><strong>Restricciones:</strong> Como es un diccionario dentro de otro, tienes que encadenar los corchetes (ej. `diccionario['llave_padre']['llave_hijo']`) dentro de tu `if`. Si tiene permiso imprime 'Creando instancia', sino imprime 'Acceso Denegado'.</p>",
        "out": "Acceso Denegado"
    },
    {
        "title": "Imprimir Boleta Detallada",
        "desc": "<p>El Mini-Boss: Sácale la información a un diccionario para armar una boleta real de restaurante.</p><p><strong>Datos Iniciales:</strong> La cuenta es: `{'Papas': 5000, 'Pizza': 10000}`.</p><p><strong>Reglas de Negocio:</strong> Tienes que sumar el total de los platos. Una vez sumado, tienes que calcular el 10% extra por la propina y sumárselo al total final.</p><p><strong>Restricciones:</strong> Usa la herramienta `.items()` en un ciclo `for` para extraer la pareja completa (el nombre del plato y el precio) al mismo tiempo. Haz la matemática e imprime `'Total final: '` junto al número final con propina.</p>",
        "out": "Total final: 16500.0"
    },

    # Bloque 6
    {
        "title": "Análisis de Sentimiento Básico (Twitter)",
        "desc": "<p>Haz que un programa cuente cuántas veces se repite una palabra en un texto.</p><p><strong>Datos Iniciales:</strong> El comentario de un cliente es: `'buen servicio mal precio buen ambiente'`. Tienes un diccionario contador: `freq = {'buen': 0, 'mal': 0}`.</p><p><strong>Reglas de Negocio:</strong> Tienes que desarmar la frase en palabras sueltas. Luego, revisas si la palabra que estás mirando está en tu diccionario. Si está, le sumas 1 a su contador.</p><p><strong>Restricciones:</strong> Usa `.split()` para picar la frase en una lista de palabras. Usa un `for` para recorrerlas. Usa `if palabra in freq:` para evitar que el código explote con palabras que no te interesan (como 'servicio' o 'precio'). Imprime tu diccionario contador al terminar.</p>",
        "hint": "Usa if palabra in freq: para asegurar que sumas correctamente.",
        "out": "{'buen': 2, 'mal': 1}"
    },
    {
        "title": "Calculadora de Liquidación Real",
        "desc": "<p>Calcula el sueldo de una persona leyendo datos desde tres lados distintos.</p><p><strong>Datos Iniciales:</strong> El `sueldo_base = 800000`. Sus bonos son: `{'colacion': 50000, 'movilizacion': 30000}`. Sus descuentos son `{'AFP': 0.10, 'Salud': 0.07}`.</p><p><strong>Reglas de Negocio:</strong> El trabajador gana la suma de su base más los bonos. Pero hay que restarle los descuentos de AFP y Salud. Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).</p><p><strong>Restricciones:</strong> Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.</p>",
        "out": "744000.0"
    },
    {
        "title": "Matchmaking Avanzado por ELO (Valorant)",
        "desc": "<p>Busca al oponente más parejo en una lista de jugadores conectados.</p><p><strong>Datos Iniciales:</strong> Tú tienes 1500 puntos. Los rivales están en una lista de diccionarios: `[{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]`.</p><p><strong>Reglas de Negocio:</strong> Para que la pelea sea justa, debes emparejarte con el jugador que tenga la diferencia de puntos más pequeña comparada contigo.</p><p><strong>Restricciones:</strong> Crea una variable `diferencia_minima` y ponle un número gigante (como 9999). Recorre la lista de rivales con un `for`. Resta tus puntos con los de ellos usando la función `abs()` para que no hayan negativos. Si la diferencia es menor que tu `diferencia_minima`, actualiza tus variables guardando ese nuevo récord y guardando el `'id'` de ese rival. Imprime solo el id del rival elegido al final.</p>",
        "hint": "Inicializa diferencia_minima = 9999 y rival_escogido = None antes del ciclo.",
        "out": "2"
    },
    {
        "title": "Carrito Inteligente Múltiple (Amazon)",
        "desc": "<p>Calcula el cobro final de un carrito de compras que tiene cantidades y precios separados.</p><p><strong>Datos Iniciales:</strong> Tu carrito es una lista de diccionarios: `[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]`.</p><p><strong>Reglas de Negocio:</strong> Tienes que multiplicar la cantidad (`qty`) por el `precio` de cada cosa para saber cuánto vale cada paquete. Suma todo. Si el monto final es mayor a 50000, le haces un descuento del 10% automático.</p><p><strong>Restricciones:</strong> Usa un `for` para recorrer el carrito y hacer la matemática. Recuerda usar corchetes (ej. `producto['qty']`) para sacar los datos. Aplica el descuento si corresponde e imprime solo el precio que debe pagar.</p>",
        "out": "54000.0"
    },
    {
        "title": "Simulador de Cajero con Desglose (BancoEstado)",
        "desc": "<p>El Boss Final del curso: Programa el cerebro de un cajero automático para que entregue la menor cantidad de billetes posibles al dar un vuelto.</p><p><strong>Datos Iniciales:</strong> El cliente quiere sacar 37000. Los billetes que existen son `20000, 10000, 5000 y 1000`. Crea un diccionario vacío para guardar tus resultados.</p><p><strong>Reglas de Negocio:</strong> Para usar pocos billetes, el cajero siempre intenta pasar primero los billetes más grandes. Por ejemplo, para 37000, primero ve cuántos de 20000 caben. Con la plata que sobra, ve cuántos de 10000 caben, y así hasta llegar a cero.</p><p><strong>Restricciones:</strong> Recorre una lista con los billetes ordenados de mayor a menor. Usa división entera (`//`) para saber cuántos billetes entregar, y guárdalo en tu diccionario como `diccionario[billete] = cantidad`. Luego, usa el módulo (`%`) para actualizar la plata que te falta por repartir. Imprime el diccionario con el desglose exacto al terminar.</p>",
        "hint": "Usa división entera // para la cantidad de billetes, y actualiza el retiro = retiro % denominacion.",
        "out": "{20000: 1, 10000: 1, 5000: 1, 1000: 2}"
    }
]

# Quick fix for exercise 41 output since it depends on generic text
exercises[40]["out"] = "TuNombre"

blocks = [
    ("Bloque 1: Fundamentos (Variables y Aritmética)", 0, 10),
    ("Bloque 2: Condicionales (Casos Reales)", 10, 20),
    ("Bloque 3: Ciclos e Iteraciones", 20, 30),
    ("Bloque 4: Colecciones y Filtrado de Datos", 30, 40),
    ("Bloque 5: Diccionarios y API Mocks", 40, 50),
    ("Bloque 6: Boss Fights (Lógica Avanzada)", 50, 55)
]

html_blocks = f'''
<style>
@keyframes shake {{ 0% {{ transform: translate(1px, 1px) rotate(0deg); }} 10% {{ transform: translate(-1px, -2px) rotate(-1deg); }} 20% {{ transform: translate(-3px, 0px) rotate(1deg); }} 30% {{ transform: translate(3px, 2px) rotate(0deg); }} 40% {{ transform: translate(1px, -1px) rotate(1deg); }} 50% {{ transform: translate(-1px, 2px) rotate(-1deg); }} 60% {{ transform: translate(-3px, 1px) rotate(0deg); }} 70% {{ transform: translate(3px, 1px) rotate(-1deg); }} 80% {{ transform: translate(-1px, -1px) rotate(1deg); }} 90% {{ transform: translate(1px, 2px) rotate(0deg); }} 100% {{ transform: translate(1px, -2px) rotate(-1deg); }} }}
</style>
<script>
window.addEventListener('scroll', () => {{
    document.querySelectorAll('.exercise-box').forEach(box => {{
        const rect = box.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) box.classList.add('fade-in');
    }});
}});
</script>
'''

for block_name, start, end in blocks:
    html_blocks += f'\n<div class="doc-section mb-12">\n<h2 class="text-2xl font-bold text-kawaii-deep border-b-2 border-kawaii-rose pb-2 mb-6" style="position:relative; z-index:10; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">📌 {block_name}</h2>\n'
    for i in range(start, min(end, len(exercises))):
        ex = exercises[i]
        
        # RPG Descent Logic
        f = i / 54.0 # 0 to 1
        
        danger_levels = [
            ("🟢", "Inofensivo", "rgba(0,255,0,0.1)", "#00bb00", "rgba(0,255,0,0.3)"),
            ("🟡", "Cuidado", "rgba(255,200,0,0.1)", "#ccaa00", "rgba(255,200,0,0.3)"),
            ("🟠", "Peligro", "rgba(255,100,0,0.15)", "#ff6600", "rgba(255,100,0,0.4)"),
            ("🔴", "Letal", "rgba(200,0,0,0.2)", "#ff3333", "rgba(255,0,0,0.5)"),
            ("💀", "Infernal", "rgba(100,0,0,0.4)", "#ff1111", "rgba(255,0,0,0.8)"),
            ("🔥", "MUERTE INMINENTE", "rgba(50,0,0,0.8)", "#ffffff", "rgba(255,50,0,1)")
        ]
        danger_idx = min(int(f * len(danger_levels)), len(danger_levels)-1)
        icon, d_text, d_bg, d_color, d_border = danger_levels[danger_idx]
        
        # Colors transitioning to dark/red
        r_bg = int(255 - 235 * f)
        g_bg = int(255 - 255 * f)
        b_bg = int(255 - 255 * f)
        a_bg = 0.05 + 0.9 * f
        box_bg = f"rgba({r_bg},{g_bg},{b_bg},{a_bg})"
        
        r_bd = int(200 + 55 * f)
        g_bd = int(200 - 200 * f)
        b_bd = int(200 - 200 * f)
        a_bd = 0.2 + 0.8 * f
        box_border = f"rgba({r_bd},{g_bd},{b_bd},{a_bd})"
        
        box_shadow = f"0 {8 + 15*f}px {32 + 30*f}px rgba({int(255*f)}, 0, 0, {0.1 + 0.6*f})"
        
        title_color = "#fff" if f > 0.4 else "var(--t-accent)"
        desc_color = "#ddd" if f > 0.4 else "var(--t-text)"
        
        animation = f"animation: shake {0.8 - (0.5*f)}s infinite;" if f > 0.85 else ""
        
        html_blocks += f'''
        <div class="exercise-box" style="background: {box_bg}; border-color: {box_border}; box-shadow: {box_shadow}; {animation}; backdrop-filter: blur({12 + 10*f}px); position: relative; z-index: 10;">
          <div class="danger-badge" style="background: {d_bg}; color: {d_color}; border: 1px solid {d_border};">
            {icon} Rango: {d_text}
          </div>
          <div class="exercise-title" style="color: {title_color}; text-shadow: 0 2px 4px rgba(0,0,0,{f});">Ejercicio {i+1}: {ex['title']}</div>
          <div class="exercise-desc" style="color: {desc_color}; text-shadow: 0 1px 2px rgba(0,0,0,{f*0.5});">{ex['desc']}</div>
        '''
        if 'hint' in ex:
            html_blocks += f'<div class="hint"><strong>Pista de Ayuda:</strong> {ex["hint"]}</div>'
            
        html_blocks += f'''
          <div class="font-bold text-sm text-gray-500 uppercase mt-4">Resultado esperado en consola:</div>
          <div class="code-output mb-4">{ex['out']}</div>
          
          <!-- Accordion de GitHub -->
          <details class="mt-4 bg-kawaii-bg/50 rounded-lg border border-kawaii-border overflow-hidden">
            <summary class="p-3 cursor-pointer text-kawaii-primary font-bold hover:bg-kawaii-bg transition-colors flex items-center justify-between">
              🚀 Sube este ejercicio a tu GitHub
              <span class="text-xs font-normal">Click para ver comandos</span>
            </summary>
            <div class="p-3 border-t border-kawaii-border text-sm">
              <p class="mb-2 text-kawaii-text">Abre tu terminal en VSCode y ejecuta paso a paso:</p>
              <div class="code-output text-xs font-mono text-gray-300">git add .
git commit -m "Resuelto Ejercicio {i+1}: {ex['title']}"
git push origin HEAD</div>
            </div>
          </details>
        </div>
        '''
    html_blocks += '</div>'

# Ensure the correct file path is written
with open("c:/Users/Maki/Desktop/fundamentos_de_programacion_alumnos_DuocUCPMontt_2026/pages/desafio-50-ejercicios.html", "w", encoding="utf-8") as f:
    f.write(html_template.replace("{content}", html_blocks))

print("Script run successfully, HTML generated!")
