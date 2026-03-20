// ═══════════════════════════════════════════════════════════════
//  📦 Taller Semana 2 — Condicionales if/elif/else
//  ─────────────────────────────────────────────────────────────
//  Ejercicios mixtos: selección múltiple, verdadero/falso,
//  unir conceptos, leer diagramas de flujo, trazar código.
//
//  Tipos de ejercicio:
//    'choice'   → selección múltiple clásica (4 opciones)
//    'tf'       → verdadero o falso
//    'match'    → unir conceptos (arrastrar o selección)
//    'flow'     → interpretar diagrama de flujo con Mermaid
//    'trace'    → trazar código Python y determinar la salida
// ═══════════════════════════════════════════════════════════════

// ─── SECCIÓN 1: Selección Múltiple (conceptos) ───
const choiceExercises = [
  {
    type: 'choice',
    title: '¿Qué es un condicional?',
    instruction: 'Elige la definición más correcta.',
    question: '¿Qué permite hacer la estructura if en Python?',
    options: [
      'Repetir un bloque de código varias veces',
      'Ejecutar un bloque de código solo si se cumple una condición',
      'Definir una función reutilizable',
      'Imprimir texto en la consola',
    ],
    correct: 1,
    explanation: 'La estructura if evalúa una condición: si es True, ejecuta el bloque indentado. Si es False, lo salta.',
  },
  {
    type: 'choice',
    title: '¿Cuándo se ejecuta el else?',
    instruction: 'Piensa en la relación entre if y else.',
    question: '¿En qué caso se ejecuta el bloque dentro de else?',
    options: [
      'Siempre se ejecuta',
      'Cuando la condición del if es True',
      'Cuando la condición del if es False',
      'Solo si el usuario presiona Enter',
    ],
    correct: 2,
    explanation: 'El bloque else se ejecuta únicamente cuando la condición del if resulta False. Es el "camino alternativo".',
  },
  {
    type: 'choice',
    title: '¿Para qué sirve elif?',
    instruction: 'Recuerda que elif es la combinación de else + if.',
    question: '¿Cuál es la función de elif?',
    options: [
      'Terminar el programa inmediatamente',
      'Evaluar una condición adicional si las anteriores fueron False',
      'Reemplazar completamente al else',
      'Crear un bucle infinito',
    ],
    correct: 1,
    explanation: 'elif permite evaluar múltiples condiciones en secuencia. Se ejecuta solo si las condiciones anteriores (if y otros elif) fueron False.',
  },
  {
    type: 'choice',
    title: 'Indentación en Python',
    instruction: 'La indentación es fundamental en Python.',
    question: '¿Qué pasa si no indentas el bloque después del if?',
    options: [
      'Python lo ejecuta normalmente',
      'Se produce un IndentationError',
      'El código se ejecuta al revés',
      'Python agrega la indentación automáticamente',
    ],
    correct: 1,
    explanation: 'Python usa la indentación (espacios o tabulaciones) para saber qué código pertenece al bloque del if. Sin ella, hay un error de sintaxis.',
  },
  {
    type: 'choice',
    title: 'Estructura correcta',
    instruction: 'Observa las opciones cuidadosamente.',
    question: '¿Cuál es la sintaxis correcta de un if en Python?',
    options: [
      '<code>if (edad >= 18) {</code>',
      '<code>if edad >= 18:</code>',
      '<code>if edad >= 18 then</code>',
      '<code>IF edad >= 18 DO</code>',
    ],
    correct: 1,
    explanation: 'En Python la sintaxis es: if condición: (con dos puntos al final, sin paréntesis obligatorios y sin llaves).',
  },
];

// ─── SECCIÓN 2: Verdadero o Falso ───
const tfExercises = [
  {
    type: 'tf',
    title: 'Sobre el if',
    statement: 'El bloque de código dentro de un <code>if</code> se ejecuta siempre, sin importar la condición.',
    correct: false,
    explanation: 'Falso. Solo se ejecuta si la condición es True.',
  },
  {
    type: 'tf',
    title: 'Sobre el else',
    statement: 'Un <code>if</code> puede existir sin un <code>else</code>.',
    correct: true,
    explanation: 'Verdadero. El else es opcional. Puedes tener un if solo, sin else.',
  },
  {
    type: 'tf',
    title: 'Sobre elif',
    statement: 'Puedes poner tantos <code>elif</code> como necesites después de un <code>if</code>.',
    correct: true,
    explanation: 'Verdadero. Puedes encadenar múltiples elif para evaluar varias condiciones.',
  },
  {
    type: 'tf',
    title: 'Sobre la indentación',
    statement: 'En Python, la indentación (espacios al inicio) es solo decorativa y no afecta la ejecución.',
    correct: false,
    explanation: 'Falso. La indentación en Python es obligatoria y define qué código pertenece a cada bloque.',
  },
  {
    type: 'tf',
    title: 'Orden de evaluación',
    statement: 'Si la condición del <code>if</code> es True, Python ya no evalúa los <code>elif</code> ni el <code>else</code>.',
    correct: true,
    explanation: 'Verdadero. Python ejecuta solo el primer bloque cuya condición sea True y salta el resto.',
  },
  {
    type: 'tf',
    title: 'Sobre comparaciones',
    statement: 'La expresión <code>5 == "5"</code> en Python da como resultado <code>True</code>.',
    correct: false,
    explanation: 'Falso. 5 es un int y "5" es un str. En Python, son tipos diferentes y == devuelve False.',
  },
  {
    type: 'tf',
    title: 'Sobre and / or',
    statement: 'La expresión <code>True and False</code> da como resultado <code>True</code>.',
    correct: false,
    explanation: 'Falso. Con "and", ambas condiciones deben ser True. Como una es False, el resultado es False.',
  },
  {
    type: 'tf',
    title: 'Sobre else sin if',
    statement: 'Puedes escribir un <code>else</code> sin tener un <code>if</code> antes.',
    correct: false,
    explanation: 'Falso. El else siempre debe ir asociado a un if previo.',
  },
];

// ─── SECCIÓN 3: Unir Conceptos ───
const matchExercises = [
  {
    type: 'match',
    title: 'Conecta cada palabra clave con su función',
    pairs: [
      { left: '<code>if</code>', right: 'Evalúa la primera condición', id: 'a' },
      { left: '<code>elif</code>', right: 'Evalúa condiciones adicionales', id: 'b' },
      { left: '<code>else</code>', right: 'Se ejecuta cuando nada anterior es True', id: 'c' },
      { left: '<code>==</code>', right: 'Compara si dos valores son iguales', id: 'd' },
      { left: '<code>!=</code>', right: 'Compara si dos valores son diferentes', id: 'e' },
    ],
  },
  {
    type: 'match',
    title: 'Conecta cada código con su resultado',
    pairs: [
      { left: '<code>if True:</code>', right: 'Siempre se ejecuta el bloque', id: 'a' },
      { left: '<code>if False:</code>', right: 'Nunca se ejecuta el bloque', id: 'b' },
      { left: '<code>if 10 > 5:</code>', right: 'Se ejecuta porque 10 es mayor que 5', id: 'c' },
      { left: '<code>if 3 > 7:</code>', right: 'No se ejecuta porque 3 no es mayor que 7', id: 'd' },
    ],
  },
];

// ─── SECCIÓN 4: Leer e interpretar diagramas de flujo ───
const flowConditionalExercises = [
  {
    type: 'flow',
    title: 'Descuento VIP',
    instruction: 'Sigue el diagrama paso a paso con la entrada dada.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese total de compra: total"/]
    B --> C{total >= 50000?}
    C -- Sí --> D["descuento = total * 0.15"]
    C -- No --> E{total >= 20000?}
    E -- Sí --> F["descuento = total * 0.05"]
    E -- No --> G["descuento = 0"]
    D --> H["final = total - descuento"]
    F --> H
    G --> H
    H --> I[/"Mostrar: 'Pago final:', final"/]
    I --> J([Fin])`,
    inputHint: 'total → 60000',
    question: '¿Cuál es el pago final que se muestra?',
    options: [
      '<code>Pago final: 51000</code>',
      '<code>Pago final: 57000</code>',
      '<code>Pago final: 60000</code>',
      '<code>Pago final: 9000</code>',
    ],
    correct: 0,
    explanation: 'total=60000. ¿60000 >= 50000? → Sí → descuento = 60000 * 0.15 = 9000. final = 60000 - 9000 = 51000.',
  },
  {
    type: 'flow',
    title: 'Categoría de temperatura',
    instruction: 'Determina qué mensaje se muestra.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese temperatura: temp"/]
    B --> C{temp >= 30?}
    C -- Sí --> D[/"Mostrar: 'Hace calor ☀️'"/]
    C -- No --> E{temp >= 15?}
    E -- Sí --> F[/"Mostrar: 'Clima agradable 🌤️'"/]
    E -- No --> G[/"Mostrar: 'Hace frío ❄️'"/]
    D --> H([Fin])
    F --> H
    G --> H`,
    inputHint: 'temp → 22',
    question: '¿Qué mensaje se muestra?',
    options: [
      '<code>Hace calor ☀️</code>',
      '<code>Clima agradable 🌤️</code>',
      '<code>Hace frío ❄️</code>',
      'No muestra nada',
    ],
    correct: 1,
    explanation: 'temp=22. ¿22 >= 30? → No. ¿22 >= 15? → Sí → "Clima agradable 🌤️".',
  },
  {
    type: 'flow',
    title: 'Verificar edad y VIP',
    instruction: 'Este diagrama tiene dos condiciones que se evalúan.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese edad: edad"/]
    B --> C[/"¿Es VIP? (si/no): vip"/]
    C --> D{edad >= 18?}
    D -- Sí --> E{vip == 'si'?}
    D -- No --> F[/"Mostrar: 'No puede entrar'"/]
    E -- Sí --> G[/"Mostrar: 'Bienvenido VIP'"/]
    E -- No --> H[/"Mostrar: 'Bienvenido'"/]
    F --> I([Fin])
    G --> I
    H --> I`,
    inputHint: 'edad → 25, vip → "no"',
    question: '¿Qué mensaje se muestra?',
    options: [
      '<code>No puede entrar</code>',
      '<code>Bienvenido VIP</code>',
      '<code>Bienvenido</code>',
      '<code>Error</code>',
    ],
    correct: 2,
    explanation: 'edad=25. ¿25 >= 18? → Sí. vip="no". ¿"no" == "si"? → No → "Bienvenido".',
  },
];

// ─── SECCIÓN 5: Trazar código Python ───
const traceExercises = [
  {
    type: 'trace',
    title: 'If simple',
    instruction: 'Traza el código paso a paso.',
    code: 'edad = 16\n\nif edad >= 18:\n    print("Mayor de edad")\nelse:\n    print("Menor de edad")',
    inputHint: null,
    question: '¿Qué se imprime?',
    options: [
      '<code>Mayor de edad</code>',
      '<code>Menor de edad</code>',
      'No imprime nada',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'edad=16. ¿16 >= 18? → False → Se ejecuta el else → "Menor de edad".',
  },
  {
    type: 'trace',
    title: 'If / elif / else',
    instruction: 'Presta atención al valor de nota y las condiciones.',
    code: 'nota = 5.5\n\nif nota >= 6.0:\n    print("Aprobado con distinción")\nelif nota >= 4.0:\n    print("Aprobado")\nelse:\n    print("Reprobado")',
    inputHint: null,
    question: '¿Qué muestra la consola?',
    options: [
      '<code>Aprobado con distinción</code>',
      '<code>Aprobado</code>',
      '<code>Reprobado</code>',
      'Muestra ambos: Aprobado con distinción y Aprobado',
    ],
    correct: 1,
    explanation: 'nota=5.5. ¿5.5 >= 6.0? → No. ¿5.5 >= 4.0? → Sí → "Aprobado". Se ejecuta solo el primer bloque True.',
  },
  {
    type: 'trace',
    title: 'Condicionales anidados',
    instruction: 'Un if dentro de otro if: analiza con cuidado.',
    code: 'x = 10\ny = 5\n\nif x > 0:\n    if y > 0:\n        print("Ambos positivos")\n    else:\n        print("Solo x es positivo")\nelse:\n    print("x no es positivo")',
    inputHint: null,
    question: '¿Qué imprime el código?',
    options: [
      '<code>Ambos positivos</code>',
      '<code>Solo x es positivo</code>',
      '<code>x no es positivo</code>',
      '<code>Error</code>',
    ],
    correct: 0,
    explanation: 'x=10, y=5. ¿10 > 0? → Sí (entra al primer if). ¿5 > 0? → Sí → "Ambos positivos".',
  },
  {
    type: 'trace',
    title: 'Input y condicional',
    instruction: 'El usuario ingresa el valor indicado.',
    code: 'temp = int(input("Temperatura: "))\n\nif temp > 30:\n    msg = "¡Mucho calor!"\nelif temp > 20:\n    msg = "Buen clima"\nelif temp > 10:\n    msg = "Hace fresco"\nelse:\n    msg = "¡Hace frío!"\n\nprint(msg)',
    inputHint: 'Temperatura → "15"',
    question: '¿Qué mensaje se imprime?',
    options: [
      '<code>¡Mucho calor!</code>',
      '<code>Buen clima</code>',
      '<code>Hace fresco</code>',
      '<code>¡Hace frío!</code>',
    ],
    correct: 2,
    explanation: 'temp=15. ¿15 > 30? No. ¿15 > 20? No. ¿15 > 10? Sí → msg = "Hace fresco".',
  },
  {
    type: 'trace',
    title: 'Operadores lógicos en condición',
    instruction: 'Presta atención al and en la condición.',
    code: 'edad = 20\ntiene_carnet = True\n\nif edad >= 18 and tiene_carnet:\n    print("Puede conducir")\nelse:\n    print("No puede conducir")',
    inputHint: null,
    question: '¿Cuál es la salida?',
    options: [
      '<code>Puede conducir</code>',
      '<code>No puede conducir</code>',
      '<code>Error</code>',
      'No imprime nada',
    ],
    correct: 0,
    explanation: 'edad=20, tiene_carnet=True. ¿20 >= 18? → True. ¿True and True? → True → "Puede conducir".',
  },
  {
    type: 'trace',
    title: 'Variable acumuladora con condicional',
    instruction: 'Sigue el valor de la variable mensaje línea por línea.',
    code: 'precio = 35000\nmensaje = "Resumen: "\n\nif precio > 50000:\n    mensaje = mensaje + "Premium"\nelif precio > 20000:\n    mensaje = mensaje + "Estándar"\nelse:\n    mensaje = mensaje + "Básico"\n\nmensaje = mensaje + " ✓"\nprint(mensaje)',
    inputHint: null,
    question: '¿Qué se imprime?',
    options: [
      '<code>Resumen: Premium ✓</code>',
      '<code>Resumen: Estándar ✓</code>',
      '<code>Resumen: Básico ✓</code>',
      '<code>Resumen:  ✓</code>',
    ],
    correct: 1,
    explanation: 'precio=35000. ¿35000 > 50000? No. ¿35000 > 20000? Sí → mensaje = "Resumen: Estándar". Luego se agrega " ✓" → "Resumen: Estándar ✓".',
  },
  {
    type: 'trace',
    title: 'Múltiples prints',
    instruction: 'Ojo: ¿cuántos print se ejecutan?',
    code: 'n = 7\n\nif n % 2 == 0:\n    print("Es par")\nelse:\n    print("Es impar")\n\nif n > 5:\n    print("Es mayor que 5")',
    inputHint: null,
    question: '¿Qué muestra la consola? (pueden ser varias líneas)',
    options: [
      '<code>Es par</code><br><code>Es mayor que 5</code>',
      '<code>Es impar</code>',
      '<code>Es impar</code><br><code>Es mayor que 5</code>',
      '<code>Es mayor que 5</code>',
    ],
    correct: 2,
    explanation: 'n=7. 7%2=1, ¿1==0? No → "Es impar". Luego, ¿7>5? Sí → "Es mayor que 5". Son dos ifs independientes, ambos se evalúan.',
  },
  {
    type: 'trace',
    title: 'Error común: no convertir input',
    instruction: 'Lee atentamente el tipo de dato de la variable.',
    code: 'numero = input("Número: ")\n\nif numero > 10:\n    print("Grande")\nelse:\n    print("Pequeño")',
    inputHint: 'Número → "25"',
    question: '¿Qué pasa al ejecutar este código?',
    options: [
      '<code>Grande</code>',
      '<code>Pequeño</code>',
      'Error: no se puede comparar str con int',
      '<code>25</code>',
    ],
    correct: 2,
    explanation: 'input() devuelve "25" (string). No se puede comparar "25" > 10 (str vs int). Falta int(input(...)).',
  },
];
