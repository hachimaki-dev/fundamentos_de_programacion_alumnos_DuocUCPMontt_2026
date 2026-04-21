// ═══════════════════════════════════════════════════════════════
//  🏟️ Reto Interactivo de Aula — Datos de Actividades
//  ─────────────────────────────────────────────────────────────
//  Actividades diseñadas para proyección en clase presencial.
//  Cada actividad tiene un tipo de interacción diferente para
//  mantener el ritmo, la sorpresa y la participación real.
// ═══════════════════════════════════════════════════════════════

const retoAulaActividades = [

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 1 — Calentamiento: ¿Qué imprime esto?
  // ──────────────────────────────────────────────────
  {
    id: 1,
    tipo: 'predecir',
    emoji: '🔮',
    titulo: '¿Qué aparece en pantalla?',
    instruccionDocente: '🖐️ <strong>Manos arriba:</strong> Pide que todos lean el código en silencio durante 10 segundos. Luego pregunta: "¿Quién cree saber la respuesta? ¡Levanten la mano!" Elige a alguien que normalmente no participa.',
    dinamica: 'Levanten la mano',
    code: `nombre = "Python"
edad = 3
print("Hola", nombre)
print("Versión:", edad + 1)`,
    pregunta: '¿Qué se verá exactamente en la consola?',
    opciones: [
      'Hola Python\\nVersión: 4',
      'Hola nombre\\nVersión: edad + 1',
      'HolaPython\\nVersión:4',
      'Error: no se puede sumar'
    ],
    correcta: 0,
    explicacion: '<strong>print("Hola", nombre)</strong> imprime <code>Hola Python</code> (con espacio automático por la coma). Luego <code>edad + 1</code> = <code>3 + 1</code> = <code>4</code>. El resultado es:<br><code>Hola Python</code><br><code>Versión: 4</code>',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 2 — De pie o sentados
  // ──────────────────────────────────────────────────
  {
    id: 2,
    tipo: 'de-pie',
    emoji: '🧍',
    titulo: '¡De pie o sentados!',
    instruccionDocente: '🧍 <strong>Dinámica corporal:</strong> Lee cada afirmación en voz alta. Si creen que es VERDADERA → de pie. Si creen que es FALSA → sentados. ¡Mira la sala antes de dar la respuesta! Hazlo rápido, máximo 8 segundos por afirmación.',
    dinamica: 'Pararse / Sentarse',
    afirmaciones: [
      {
        texto: '<code>input()</code> siempre devuelve un número entero.',
        correcta: false,
        explicacion: '¡FALSO! <code>input()</code> SIEMPRE devuelve un <strong>string</strong> (texto). Para obtener un número debes convertirlo con <code>int()</code> o <code>float()</code>.'
      },
      {
        texto: '<code>print("5" + "3")</code> imprime <code>53</code>.',
        correcta: true,
        explicacion: '¡VERDADERO! Como ambos son strings (texto entre comillas), el operador <code>+</code> los concatena. Resultado: <code>"53"</code>.'
      },
      {
        texto: 'Un <code>while True:</code> sin <code>break</code> se ejecuta para siempre.',
        correcta: true,
        explicacion: '¡VERDADERO! Si no hay un <code>break</code> ni ninguna condición que lo detenga, el ciclo será infinito. ¡Cuidado con eso!'
      },
      {
        texto: 'El ciclo <code>for</code> se usa cuando NO sabemos cuántas veces repetir.',
        correcta: false,
        explicacion: '¡FALSO! El <code>for</code> se usa justamente cuando SÍ sabemos cuántas veces repetir (recorrer una lista, un rango definido). El <code>while</code> es para cuando NO lo sabemos.'
      },
      {
        texto: '<code>if 5 > 3:</code> es una condición válida en Python.',
        correcta: true,
        explicacion: '¡VERDADERO! <code>5 > 3</code> se evalúa como <code>True</code>, así que el bloque del <code>if</code> se ejecuta.'
      },
    ],
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 3 — Detectar el error
  // ──────────────────────────────────────────────────
  {
    id: 3,
    tipo: 'error',
    emoji: '🐛',
    titulo: '¡Caza el Bug!',
    instruccionDocente: '🗣️ <strong>Respuesta coral:</strong> Muestra el código y di: "A la cuenta de 3, todos gritan dónde está el error. ¡1... 2... 3!" Acepta múltiples respuestas y guía hacia la correcta.',
    dinamica: 'Respuesta coral',
    code: `edad = input("¿Cuántos años tienes? ")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")`,
    pregunta: 'Este código tiene un bug que hará que Python lance un error. ¿Dónde está?',
    opciones: [
      'Falta el <code>:</code> después del <code>else</code>',
      '<code>input()</code> devuelve texto y se compara con un número sin convertir',
      'No se puede usar <code>>=</code> en Python',
      'El <code>print</code> necesita punto y coma al final'
    ],
    correcta: 1,
    explicacion: '¡El clásico error de novato! <code>input()</code> devuelve un <strong>string</strong>, y no puedes comparar un string con un número usando <code>>=</code>. La corrección es: <code>edad = <strong>int(</strong>input("¿Cuántos años tienes? ")<strong>)</strong></code>',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 4 — Completar el código
  // ──────────────────────────────────────────────────
  {
    id: 4,
    tipo: 'completar',
    emoji: '✍️',
    titulo: 'Completa el puzzle',
    instruccionDocente: '🖐️ <strong>Manos arriba rápido:</strong> Muestra el código con los huecos. Da 15 segundos para pensar. "¿Quién tiene la respuesta? ¡Primera mano que vea!" Intenta elegir a alguien diferente a la actividad anterior.',
    dinamica: 'Levanten la mano',
    code: `numero = int(input("Ingresa un número: "))

if numero ______ 0:
    print("Positivo")
______ numero == 0:
    print("Es cero")
______:
    print("Negativo")`,
    pregunta: '¿Qué operador y palabras clave van en los huecos ______ para que el programa clasifique correctamente un número?',
    opciones: [
      '<code>></code> / <code>elif</code> / <code>else</code>',
      '<code>==</code> / <code>else if</code> / <code>else</code>',
      '<code>>=</code> / <code>elif</code> / <code>if</code>',
      '<code>></code> / <code>if</code> / <code>elif</code>'
    ],
    correcta: 0,
    explicacion: 'Necesitamos: <code>></code> para verificar si es positivo (mayor que 0), <code>elif</code> (no "else if") para la segunda condición, y <code>else</code> para cubrir el caso restante (negativo).',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 5 — ¿Qué pasaría si...?
  // ──────────────────────────────────────────────────
  {
    id: 5,
    tipo: 'que-pasaria',
    emoji: '🤔',
    titulo: '¿Qué pasaría si...?',
    instruccionDocente: '💬 <strong>Discusión en parejas:</strong> Pide que se giren hacia su compañero de al lado. Tienen 30 segundos para discutir la respuesta. Luego pide a una pareja al azar que explique su razonamiento en voz alta.',
    dinamica: 'Discusión entre compañeros',
    code: `contador = 1
while contador <= 5:
    print(contador)
    contador += 1`,
    pregunta: '¿Qué pasaría si cambiamos <code>contador += 1</code> por <code>contador += 2</code>?',
    opciones: [
      'Imprime: 1, 2, 3, 4, 5',
      'Imprime: 1, 3, 5',
      'Imprime: 2, 4',
      'Error: no se puede sumar 2'
    ],
    correcta: 1,
    explicacion: 'Si incrementamos de 2 en 2:<br>• Vuelta 1: contador=1 → imprime 1, luego contador=3<br>• Vuelta 2: contador=3 → imprime 3, luego contador=5<br>• Vuelta 3: contador=5 → imprime 5, luego contador=7<br>• contador=7, y 7 ≤ 5 es FALSO → se detiene.<br><strong>Resultado: 1, 3, 5</strong>',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 6 — Ordenar los pasos
  // ──────────────────────────────────────────────────
  {
    id: 6,
    tipo: 'ordenar',
    emoji: '🔢',
    titulo: 'Ordena el algoritmo',
    instruccionDocente: '🖐️ <strong>Voluntarios al frente:</strong> Muestra las líneas desordenadas. Pide 4 voluntarios. Cada uno recibe un "número de línea" (1 al 4). Deben pararse al frente y ordenarse para formar el programa correcto. ¡Que la sala les ayude!',
    dinamica: 'Voluntarios al frente',
    descripcion: 'Un programa que pide un número y dice si es par o impar. Las líneas están desordenadas. ¡Ordénalas correctamente!',
    lineasDesordenadas: [
      'print("Es par")',
      'numero = int(input("Dime un número: "))',
      'else:',
      'if numero % 2 == 0:',
      'print("Es impar")',
    ],
    ordenCorrecto: [1, 3, 0, 2, 4],
    lineasOrdenadas: [
      'numero = int(input("Dime un número: "))',
      'if numero % 2 == 0:',
      '    print("Es par")',
      'else:',
      '    print("Es impar")',
    ],
    explicacion: 'El orden correcto es:<br>1️⃣ Pedir el número con <code>input()</code> y convertirlo con <code>int()</code><br>2️⃣ Evaluar si es divisible por 2 usando <code>%</code><br>3️⃣ Si sí → imprimir "Es par"<br>4️⃣ Si no (<code>else</code>) → imprimir "Es impar"',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 7 — Predecir la salida (for)
  // ──────────────────────────────────────────────────
  {
    id: 7,
    tipo: 'predecir',
    emoji: '🔄',
    titulo: 'Traza mental: el ciclo for',
    instruccionDocente: '✋ <strong>Manos arriba con opciones:</strong> Muestra las 4 opciones. "Levante la mano derecha quien crea que es la A. Levante la izquierda quien crea que es la B..." Cuenta las manos antes de revelar.',
    dinamica: 'Votación con manos',
    code: `for i in range(4):
    print(i * 2)`,
    pregunta: '¿Qué números aparecerán en pantalla, uno por línea?',
    opciones: [
      '0, 2, 4, 6',
      '2, 4, 6, 8',
      '0, 1, 2, 3',
      '1, 2, 3, 4'
    ],
    correcta: 0,
    explicacion: '<code>range(4)</code> genera: <strong>0, 1, 2, 3</strong>.<br>Multiplicamos cada uno por 2:<br>• 0 × 2 = <strong>0</strong><br>• 1 × 2 = <strong>2</strong><br>• 2 × 2 = <strong>4</strong><br>• 3 × 2 = <strong>6</strong><br>Resultado: <code>0, 2, 4, 6</code>',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 8 — Mega bug: múltiples errores
  // ──────────────────────────────────────────────────
  {
    id: 8,
    tipo: 'mega-error',
    emoji: '💀',
    titulo: '¡Código catastrófico!',
    instruccionDocente: '🗣️ <strong>Lluvia de ideas coral:</strong> Muestra el código y di: "Este código tiene TRES errores. ¡Griten los que encuentren!" Anota en la pizarra cada error que nombren. ¿Pueden encontrar los 3?',
    dinamica: 'Lluvia de ideas',
    code: `# Programa que suma números hasta que el usuario escriba "salir"
total = 0
while true:
    dato = input("Número (o salir): ")
    if dato == "salir"
        break
    total = total + dato
print("La suma es:" total)`,
    errores: [
      {
        linea: 3,
        error: '<code>true</code> debe ser <code>True</code> (con mayúscula)',
        tipo: 'Sintaxis'
      },
      {
        linea: 5,
        error: 'Falta el <code>:</code> después de <code>if dato == "salir"</code>',
        tipo: 'Sintaxis'
      },
      {
        linea: 7,
        error: '<code>dato</code> es un string (viene de input). Falta convertirlo: <code>total = total + int(dato)</code>',
        tipo: 'Lógica / Tipo'
      },
      {
        linea: 8,
        error: 'Falta una coma entre <code>"La suma es:"</code> y <code>total</code> dentro del <code>print()</code>',
        tipo: 'Sintaxis'
      }
    ],
    explicacion: 'Este código tiene <strong>4 errores</strong> (¡aún más de los que creían!):<br>1️⃣ <code>true</code> → <code>True</code><br>2️⃣ Falta <code>:</code> en el <code>if</code><br>3️⃣ Falta <code>int()</code> para convertir el input<br>4️⃣ Falta coma en el <code>print()</code>',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 9 — Mini reto al computador
  // ──────────────────────────────────────────────────
  {
    id: 9,
    tipo: 'computador',
    emoji: '💻',
    titulo: 'Reto relámpago al computador',
    instruccionDocente: '💻 <strong>Voluntario al computador del profe:</strong> Pide un voluntario que pase al computador conectado al proyector. Tiene 90 segundos para escribir el programa. ¡La sala le puede ayudar gritando sugerencias! Si se traba, permite que otro compañero lo releve.',
    dinamica: 'Voluntario al computador',
    enunciado: 'Escribe un programa que pida al usuario su nombre y cuántas veces quiere saludar. Luego, usa un ciclo <code>for</code> para imprimir "¡Hola, [nombre]!" ese número de veces.',
    ejemplo: `Ingresa tu nombre: Ana
¿Cuántas veces saludar? 3

¡Hola, Ana!
¡Hola, Ana!
¡Hola, Ana!`,
    solucion: `nombre = input("Ingresa tu nombre: ")
veces = int(input("¿Cuántas veces saludar? "))

for i in range(veces):
    print("¡Hola,", nombre + "!")`,
    pistas: [
      '¿Qué función usas para pedir datos al usuario?',
      '¿Qué conversión necesitas para el número de veces?',
      '¿Qué función genera una secuencia numérica para el for?'
    ],
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 10 — Predecir con while + if
  // ──────────────────────────────────────────────────
  {
    id: 10,
    tipo: 'predecir',
    emoji: '🧠',
    titulo: 'Traza mental avanzada',
    instruccionDocente: '📝 <strong>Respuesta escrita:</strong> Pide que todos escriban su respuesta en un papel o cuaderno. Da 30 segundos. Luego di: "¡Levanten su papel!" Mira las respuestas antes de revelar. Comenta los errores más comunes que veas.',
    dinamica: 'Escribir y mostrar',
    code: `x = 10
while x > 0:
    if x % 3 == 0:
        print(x)
    x -= 2`,
    pregunta: '¿Qué números imprimirá este programa? Piensa paso a paso.',
    opciones: [
      '9, 6, 3',
      '6',
      '10, 8, 6, 4, 2',
      '6, 0'
    ],
    correcta: 1,
    explicacion: 'Vamos paso a paso:<br>• x=10 → 10%3=1 → NO imprime. x=8<br>• x=8 → 8%3=2 → NO imprime. x=6<br>• x=6 → 6%3=0 → <strong>Imprime 6</strong>. x=4<br>• x=4 → 4%3=1 → NO imprime. x=2<br>• x=2 → 2%3=2 → NO imprime. x=0<br>• x=0 → 0 > 0 es FALSO → sale del while<br><br><strong>Solo imprime: 6</strong> ¡Muchos dirán 6 y 0, pero 0 no es mayor que 0!',
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 11 — Verdadero / Falso con trampa
  // ──────────────────────────────────────────────────
  {
    id: 11,
    tipo: 'vf-trampa',
    emoji: '⚡',
    titulo: 'Verdadero o Falso... ¡con trampa!',
    instruccionDocente: '🧍 <strong>De pie / Sentados rápido:</strong> Lee cada afirmación. "Si creen que es verdadero, quédense de pie. Si es falso, siéntense." ¡Hazlo rápido para que no puedan copiar al compañero!',
    dinamica: 'Pararse / Sentarse',
    afirmaciones: [
      {
        texto: 'El código <code>for i in range(1, 5):</code> ejecuta el bloque <strong>5 veces</strong>.',
        correcta: false,
        explicacion: '¡FALSO! <code>range(1, 5)</code> genera 1, 2, 3, 4. Son <strong>4 veces</strong>, no 5. ¡Recuerda que el límite superior NO se incluye!'
      },
      {
        texto: 'Se puede usar un <code>if</code> dentro de un <code>while</code>.',
        correcta: true,
        explicacion: '¡VERDADERO! Puedes anidar (combinar) cualquier estructura dentro de otra. Es algo muy común y útil.'
      },
      {
        texto: 'El operador <code>==</code> se usa para <strong>asignar</strong> un valor a una variable.',
        correcta: false,
        explicacion: '¡FALSO! <code>==</code> es para <strong>comparar</strong>. Para <strong>asignar</strong> se usa un solo <code>=</code>. Confundirlos es uno de los errores más frecuentes.'
      },
    ],
  },

  // ──────────────────────────────────────────────────
  // ACTIVIDAD 12 — Reto final cooperativo
  // ──────────────────────────────────────────────────
  {
    id: 12,
    tipo: 'reto-final',
    emoji: '🏆',
    titulo: 'Desafío final: ¡Código cooperativo!',
    instruccionDocente: '🤝 <strong>Código en cadena:</strong> Pide 5 voluntarios. Cada uno escribirá UNA línea del programa (en la pizarra o en el computador). No pueden hablar entre sí, solo pueden leer lo que escribió el anterior. El resto de la sala puede aplaudir o abuchear (con cariño) después de cada línea. ¡Es caótico y divertido!',
    dinamica: 'Voluntarios en cadena',
    enunciado: 'El programa debe: pedir números al usuario usando un <code>while</code> hasta que escriba <code>0</code>. Por cada número, debe decir si es positivo o negativo usando <code>if</code>. Al terminar, debe mostrar cuántos números ingresó en total.',
    lineasNecesarias: 5,
    solucionReferencia: `contador = 0

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if numero > 0:
        print("Es positivo")
    else:
        print("Es negativo")
    contador += 1

print("Ingresaste", contador, "números en total")`,
    criterios: [
      '¿Usaron <code>while</code> correctamente?',
      '¿Convirtieron el input a <code>int()</code>?',
      '¿Verificaron la condición de salida con <code>if</code> y <code>break</code>?',
      '¿Clasificaron positivo/negativo con <code>if/else</code>?',
      '¿Contaron con un acumulador o contador?',
    ],
  },
];
