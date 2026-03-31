// ═══════════════════════════════════════════════════════════════
//  🛒 Banco de Ejercicios a Elección — Evaluación Parcial 1
// ═══════════════════════════════════════════════════════════════

const BANCO_EJERCICIOS = [
  {
    id: 1,
    emoji: '🎮',
    title: 'Simulador de Daño de RPG',
    theme: 'Videojuegos',
    difficulty: 'Fácil',
    shortDesc: 'Ataca al jefe hasta que su vida llegue a cero usando un bucle while y validando los ataques con if.',
    fullDesc: `
<b>Objetivo:</b> Crear un pequeño simulador de un combate de rol (RPG).

1. El jefe final tiene 1000 puntos de vida iniciales.
2. Usa un ciclo <code>while</code> que se repita mientras la vida del jefe sea mayor que 0.
3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".
    `.trim()
  },
  {
    id: 2,
    emoji: '🍔',
    title: 'App de Delivery Kawaii',
    theme: 'E-commerce',
    difficulty: 'Intermedio',
    shortDesc: 'Suma el precio de los platos usando un acumulador y aplica un descuento al total si supera un monto.',
    fullDesc: `
<b>Objetivo:</b> Calcular el total a pagar de un pedido de comida, con descuentos.

1. Pregunta al usuario cuántos platos desea pedir (cantidad).
2. Usa un ciclo <code>while</code> y un contador para pedir el precio de CADA plato.
3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
4. Una vez terminado el ciclo, evalúa el subtotal con un <code>if</code>:
   - Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
   - Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".
    `.trim()
  },
  {
    id: 3,
    emoji: '🏃',
    title: 'Smartwatch Activity Tracker',
    theme: 'Móvil / Salud',
    difficulty: 'Fácil',
    shortDesc: 'Registra los kilómetros diarios durante una semana, pero sáltate los días de lesiones.',
    fullDesc: `
<b>Objetivo:</b> Monitorear tu actividad física de los últimos 7 días.

1. Crea un ciclo <code>while</code> que se ejecute 7 veces (representando los 7 días de la semana).
2. Pregunta al usuario: "¿Cuántos km corriste el día X?".
3. Si el usuario ingresa un número negativo (ej., -1), significa que se lesionó. Muestra "Día saltado" y NO sumes esos kilómetros (pero sí cuenta el día).
4. Acumula todos los kilómetros válidos.
5. Al final, si el total es >= 30, muestra "¡Meta semanal cumplida! Eres un atleta".
6. Si es menor, muestra "Sigue intentando, llevas X kilómetros, ¡tú puedes!".
    `.trim()
  },
  {
    id: 4,
    emoji: '🏦',
    title: 'Cajero Automático (PIN Seguro)',
    theme: 'Finanzas',
    difficulty: 'Avanzado',
    shortDesc: 'Maneja intentos de seguridad, bloqueo de tarjetas y un menú de retiros de dinero.',
    fullDesc: `
<b>Objetivo:</b> Simular un cajero con validación de seguridad.

1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
2. Tiene máximo 3 intentos para ingresar el PIN usando un <code>while</code>.
3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
5. Pregunta cuánto dinero quiere retirar.
6. Usa un <code>if</code> para verificar:
   - Si el monto es mayor al saldo: "Fondos insuficientes".
   - Si el monto es igual a 0: "Monto inválido".
   - Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".
    `.trim()
  },
  {
    id: 5,
    emoji: '🎬',
    title: 'Taquilla del Cine Kawaii',
    theme: 'Eventos',
    difficulty: 'Intermedio',
    shortDesc: 'Vende entradas para una película, calculando precios distintos según la edad y sumando la ganancia final.',
    fullDesc: `
<b>Objetivo:</b> Gestionar la venta de N entradas en una sala de cine.

1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
2. Usa un ciclo <code>while</code> para procesar CADA entrada.
3. Para cada entrada, pregunta la EDAD de la persona.
   - Si es menor de 12 años, su entrada cuesta $3.000.
   - Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
   - Si es adulto mayor (65 o más), la entrada cuesta $4.000.
4. Usa un acumulador para sumar el precio de todas las entradas.
5. Imprime al final el gran total recaudado en esa transacción.
    `.trim()
  },
  {
    id: 6,
    emoji: '🌡️',
    title: 'Alarma de Invernadero',
    theme: 'IoT / Control',
    difficulty: 'Medio',
    shortDesc: 'Monitorea el clima. Si tres mediciones consecutivas son muy altas, dispara las alarmas.',
    fullDesc: `
<b>Objetivo:</b> Prevenir que se quemen las plantas en un invernadero automatizado.

1. El programa funcionará con un ciclo <code>while</code> indefinido (preguntando "Ingrese temperatura actual").
2. Si la temperatura ingresada es 0, el programa termina la lectura de datos.
3. El límite de peligro es 35°C. Usa un contador especial de "alertas consecutivas" inicializado en 0.
4. Si ingresas una temp >= 35, suma 1 al contador de alertas consecutivas.
5. Si ingresas una temp < 35, el contador de alertas ESTRICTAMENTE vuelve a 0 (porque ya no es consecutiva).
6. Si en cualquier momento el contador llega a 3, imprime un texto inmenso "¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!" y finaliza el ciclo usando break.
    `.trim()
  },
  {
    id: 7,
    emoji: '🐶',
    title: 'Negocio: Paseador de Perros',
    theme: 'Emprendimiento',
    difficulty: 'Medio',
    shortDesc: 'Calcula cuánto ganó el paseador hoy según el peso de los perritos paseados.',
    fullDesc: `
<b>Objetivo:</b> Control de ganancias de un negocio de servicios variables.

1. Pregunta al usuario cuántos perros paseó en total el día de hoy.
2. Usa un ciclo para que, por cada perro, pida ingresar su peso en kg.
3. Evalúa con if/elif/else:
   - Perro pequeño (menos de 10 kg) -> Cuesta $2.000.
   - Perro mediano (entre 10 y < 25 kg) -> Cuesta $4.000.
   - Perro grande (25 kg o más) -> Cuesta $6.000.
4. Suma lo ganado en un acumulador total.
5. Al finalizar el ciclo, imprime "Resumen del día: Has paseado X perros ganando en total $Y".
    `.trim()
  },
  {
    id: 8,
    emoji: '📊',
    title: 'Contador de Votos Estudiantil',
    theme: 'Social / Escolar',
    difficulty: 'Básico',
    shortDesc: 'Haz una encuesta, cuenta votos "A favor" y "En contra" y determina qué opción ganó.',
    fullDesc: `
<b>Objetivo:</b> Procesar los resultados de una pequeña encuesta del curso.

1. Pregunta cuántos estudiantes van a votar (ej. N encuestados).
2. Usa un <code>while</code> para recoger los votos. En cada iteración pide que el estudiante escriba "A" (A favor) o "C" (En contra).
3. Vas a necesitar DOS contadores (uno para A, uno para C) que parten en 0.
4. Si ingresan algo distinto a "A" o "C", muestra "Voto nulo no contabilizado" (no lo sumes a nada, pero la iteración se gasta igual).
5. Fuera del ciclo, compara ambos contadores.
   - Si A > C, imprime "Ganó A favor".
   - Si C > A, imprime "Ganó En Contra".
   - Si A == C, imprime "Empate".
    `.trim()
  },
  {
    id: 9,
    emoji: '🕹️',
    title: 'Minijuego: El Número Secreto',
    theme: 'Juegos',
    difficulty: 'Fácil',
    shortDesc: 'Crea el clásico juego donde el usuario adivina el número, dándole pistas de "más alto" o "más bajo".',
    fullDesc: `
<b>Objetivo:</b> Programar un juego clásico de interacción constante.

1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
2. Usa un <code>while</code> que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
3. Dentro del while: pide un número al usuario.
   - Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
   - Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
4. Usa un contador para registrar en cuántos turnos logró adivinar.
5. Imprime al final "¡Ganaste en X intentos!".
    `.trim()
  },
  {
    id: 10,
    emoji: '🏥',
    title: 'Triage de Sala de Urgencia',
    theme: 'Salud',
    difficulty: 'Medio',
    shortDesc: 'Programa un árbol de decisiones if/elif/else sin usar while.',
    fullDesc: `
<b>Objetivo:</b> Evaluar la urgencia clínica de un paciente para determinar si necesita atención inmediata.

1. Pide 3 datos:
   - Edad (entero).
   - "Tiene dificultad para respirar" (respuesta "SI" o "NO").
   - Nivel de dolor del 1 al 10.
2. LÓGICA DEL TRIAGE:
   - Si tiene dificultad para respirar == "SI", es URGENCIAS NIVEL 1 pase inmediatamente. (Lo demás no importa).
   - Elif si NO respira con dificultad, pero la edad > 60 Y el nivel de dolor > 7, es URGENCIAS NIVEL 2, pase pronto.
   - Elif si nivel de dolor es menor a 4, URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.
   - Else, para los demás casos: URGENCIAS NIVEL 3-4, tome asiento por favor.
3. Ojo con usar los comparadores adecuados (==) y anidar (if dentro de elif).
    `.trim()
  },
  {
    id: 11,
    emoji: '🚇',
    title: 'Torniquete de Metro',
    theme: 'Transporte',
    difficulty: 'Fácil',
    shortDesc: 'Calcula la recaudación del torniquete diferenciando perfiles en un ciclo infinito hasta corte.',
    fullDesc: `
<b>Objetivo:</b> Cobrador automático del metro santiaguino.

1. Crea un ciclo <code>while</code> infinito hasta que el operador ingrese "CORTE".
2. Pide el tipo de pasajero (puede escribir: "N" para normal, "E" para estudiante, o "CORTE").
3. Precios: Normal $800, Estudiante $250.
4. Acumula el dinero total recaudado.
5. Y mantén contadores separados: ¿Cuántos normales pasaron? ¿Cuántos estudiantes?
6. Al ingresar "CORTE", el programa sale del ciclo y muestra en pantalla:
   - Pasajeros normales: X
   - Estudiantes: Y
   - Total dinero caja: Z
    `.trim()
  },
  {
    id: 12,
    emoji: '🎵',
    title: 'Creador de Playlists al Límite',
    theme: 'Música',
    difficulty: 'Medio',
    shortDesc: 'Ve ingresando la duración de las canciones, el bucle debe detenerse si la playlist supera un tiempo total máximo.',
    fullDesc: `
<b>Objetivo:</b> No llenar la memoria de un reproductor que soporta máximo 60 minutos.

1. Tienes un reproductor MP3 minúsculo que solo permite guardar canciones mientras el tiempo total sea EXACTO o MENOR a 60 minutos.
2. Usa un acumulador "duracion_total" partido en 0.
3. El <code>while</code> se ejecuta MIENTRAS la duracion_total <= 60.
4. Pide: "Minutos de la siguiente canción: ".
5. ATENCIÓN: Solo suma la canción al acumulador SI (condición) la canción cabe en el tiempo restante.
   - Si no cabe (ej, quedan 2 mins libres y la canción dura 4), muestra "La canción de X minutos no cabe". (Y la canción NO se agrega).
   - Como no se agregó, la suma no cambia. El ciclo volverá a pedir otra pista.
6. Si suma_total llega justo a 60, el ciclo terminará solo. Muestra "¡Espacio lleno al 100%!".
    `.trim()
  },
  {
    id: 13,
    emoji: '🛒',
    title: 'Supermercado Mayorista',
    theme: 'Comercio',
    difficulty: 'Avanzado',
    shortDesc: 'Cobro de productos donde solo se aplica descuento por volumen del mismo artículo.',
    fullDesc: `
<b>Objetivo:</b> Sistema de cobro que evalúe promociones por mayor.

1. Pide registrar un único producto estrella.
2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó ("¡Felicidades obtuvo el X% descuento! Su total es...").
5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".
    `.trim()
  },
  {
    id: 14,
    emoji: '🦸',
    title: 'Ranking de Superhéroes',
    theme: 'Cultura Pop',
    difficulty: 'Fácil',
    shortDesc: 'Clasificador en base a sus estadísticas.',
    fullDesc: `
<b>Objetivo:</b> Determinar el rango de clasificación para un afiliado de la agencia. 

1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos "Daños Civiles (en costo monetario)" tuvo el héroe este mes.
2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime "Héroe Categoría S. Bono máximo!".
3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: "Héroe Categoría A. Cumple promedio".
4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: "Despedido. Demasiado caos".
5. Si no cae en lo de arriba: "Héroe en observación".
6. Programa las validaciones con los if, elif y else garantizando que todo tiene lógica correcta.
    `.trim()
  },
  {
    id: 15,
    emoji: '🚗',
    title: 'Sistema Autopista Peaje',
    theme: 'Transporte',
    difficulty: 'Medio',
    shortDesc: 'Controlador de vehículos diferenciando el flujo',
    fullDesc: `
<b>Objetivo:</b> Contador analítico de transporte para un peaje de carretera.

1. Usar bucle infinito hasta que el cobrador ingrese tipo vehiculo "SALIR".
2. Los tipos que se pueden ingresar son: "AUTO", "CAMION", "MOTO".
3. Precios: AUTO=$1500, MOTO=$500, CAMION=$3500. Si introducen otra cosa muestra error.
4. Acumular en todo momento LA CANTIDAD de cada vehiculo que pasó.
5. Acumular el DINERO GLOBAL generado.
6. Al poner "SALIR", muestra un cierre de caja: (Ganancia Total, y por porcentaje aproximado qué tipo de vehiculo es el ganador del dia, ej: pasaron mas motos que autos).
    `.trim()
  }
];
