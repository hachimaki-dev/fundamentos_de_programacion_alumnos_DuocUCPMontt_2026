// ═══════════════════════════════════════════════════════════════
//  📦 Ejercicios de Python — Datos puros
//  ─────────────────────────────────────────────────────────────
//  Para agregar más ejercicios, copia un bloque { ... } y pégalo
//  al final del array.
//
//  Campos:
//    type        → 'python'
//    title       → título del ejercicio
//    instruction → instrucción breve
//    code        → código Python (usa \n para saltos de línea)
//    inputHint   → (opcional) qué escribe el usuario en input()
//    question    → la pregunta
//    options     → array de 4 alternativas (admite HTML)
//    correct     → índice de la correcta (0=A, 1=B, 2=C, 3=D)
//    explanation → texto que se muestra al responder
// ═══════════════════════════════════════════════════════════════

const pythonExercises = [
  {
    type: 'python',
    title: 'Variables y Suma',
    instruction: 'Lee el código y determina qué se imprime en pantalla.',
    code: 'a = 5\nb = 3\nresultado = a + b\nprint("El resultado es:", resultado)',
    inputHint: null,
    question: '¿Qué muestra la consola?',
    options: [
      '<code>El resultado es: 53</code>',
      '<code>El resultado es: 8</code>',
      '<code>resultado = 8</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'Las variables a y b son enteras, se suman (5+3 = 8) y se imprime "El resultado es: 8".',
  },
  {
    type: 'python',
    title: 'Input y Parseo a Entero',
    instruction: 'El usuario ingresa el valor indicado. ¿Cuál es la salida?',
    code: 'nombre = input("Tu nombre: ")\nedad = int(input("Tu edad: "))\nprint("Hola", nombre, "tienes", edad, "años")',
    inputHint: 'nombre → "Ana", edad → "20"',
    question: '¿Qué se imprime en la consola?',
    options: [
      '<code>Hola Ana tienes 20 años</code>',
      '<code>Hola "Ana" tienes "20" años</code>',
      '<code>Tu nombre: Tu edad:</code>',
      '<code>Error: no se puede convertir</code>',
    ],
    correct: 0,
    explanation: 'input() recibe texto; int() convierte "20" a entero. print() separa los argumentos con espacio automáticamente.',
  },
  {
    type: 'python',
    title: 'Concatenación vs Suma',
    instruction: 'Presta atención a los tipos de datos.',
    code: 'a = "10"\nb = "20"\nc = a + b\nprint(c)',
    inputHint: null,
    question: '¿Qué valor muestra la consola?',
    options: [
      '<code>30</code>',
      '<code>1020</code>',
      '<code>"10" + "20"</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'Como a y b son strings (texto), el operador + los concatena: "10" + "20" = "1020".',
  },
  {
    type: 'python',
    title: 'Parseo y Aritmética',
    instruction: 'Analiza las conversiones de tipo.',
    code: 'x = int("7")\ny = int("3")\nz = x * y - 1\nprint(z)',
    inputHint: null,
    question: '¿Qué valor se imprime?',
    options: [
      '<code>21</code>',
      '<code>20</code>',
      '<code>73</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'int("7") = 7, int("3") = 3. Luego z = 7 * 3 - 1 = 21 - 1 = 20.',
  },
  {
    type: 'python',
    title: 'Lógica Proposicional',
    instruction: 'Evalúa mentalmente las expresiones lógicas.',
    code: 'a = 10\nb = 5\nc = a > b and b > 0\nd = a < b or b == 5\nprint(c, d)',
    inputHint: null,
    question: '¿Qué muestra la consola?',
    options: [
      '<code>True True</code>',
      '<code>True False</code>',
      '<code>False True</code>',
      '<code>False False</code>',
    ],
    correct: 0,
    explanation: 'c: 10>5 es True AND 5>0 es True → True. d: 10<5 es False OR 5==5 es True → True.',
  },
  {
    type: 'python',
    title: 'Operación con Módulo',
    instruction: 'Recuerda que % es el operador módulo (resto de la división).',
    code: 'a = 17\nb = 5\ncociente = a // b\nresto = a % b\nprint("Cociente:", cociente, "Resto:", resto)',
    inputHint: null,
    question: '¿Cuál es la salida?',
    options: [
      '<code>Cociente: 3 Resto: 2</code>',
      '<code>Cociente: 3.4 Resto: 2</code>',
      '<code>Cociente: 3 Resto: 3</code>',
      '<code>Cociente: 4 Resto: 2</code>',
    ],
    correct: 0,
    explanation: '17 // 5 = 3 (división entera). 17 % 5 = 2 (el resto de dividir 17 entre 5).',
  },
  {
    type: 'python',
    title: 'Input con Cálculo',
    instruction: 'El usuario ingresa los valores indicados.',
    code: 'precio = int(input("Precio: "))\ncantidad = int(input("Cantidad: "))\ntotal = precio * cantidad\nprint("Total a pagar:", total)',
    inputHint: 'precio → "1500", cantidad → "3"',
    question: '¿Qué se imprime?',
    options: [
      '<code>Total a pagar: 4500</code>',
      '<code>Total a pagar: 15003</code>',
      '<code>Total a pagar: 1500 * 3</code>',
      '<code>Error</code>',
    ],
    correct: 0,
    explanation: 'Se parsean ambos inputs a entero con int(). 1500 * 3 = 4500.',
  },
  {
    type: 'python',
    title: 'Comparaciones y Lógica',
    instruction: 'Evalúa cada expresión paso a paso.',
    code: 'x = 8\ny = 12\nz = 8\nprint(x == z)\nprint(x != y)\nprint(not(x > y))',
    inputHint: null,
    question: '¿Qué se muestra en las tres líneas de salida?',
    options: [
      '<code>True</code>, <code>True</code>, <code>True</code>',
      '<code>True</code>, <code>True</code>, <code>False</code>',
      '<code>False</code>, <code>True</code>, <code>True</code>',
      '<code>True</code>, <code>False</code>, <code>True</code>',
    ],
    correct: 0,
    explanation: '8==8 → True. 8!=12 → True. 8>12 es False, not(False) → True.',
  },
  {
    type: 'python',
    title: '¿Qué tipo de dato es?',
    instruction: 'Observa las variables y sus asignaciones.',
    code: 'a = 4\nb = "hola"\nc = 3.14\nd = True\nprint(type(a), type(b), type(c), type(d))',
    inputHint: null,
    question: '¿Cuáles son los tipos de a, b, c y d respectivamente?',
    options: [
      'int, str, float, bool',
      'int, str, int, str',
      'str, str, float, int',
      'int, str, float, int',
    ],
    correct: 0,
    explanation: '4 es int, "hola" es str, 3.14 es float, True es bool.',
  },
  {
    type: 'python',
    title: 'Error de Tipos',
    instruction: '¿Qué pasa cuando se mezclan tipos incompatibles?',
    code: 'edad = input("Edad: ")\nresultado = edad + 5\nprint(resultado)',
    inputHint: 'edad → "25"',
    question: '¿Qué ocurre al ejecutar este código?',
    options: [
      '<code>30</code>',
      '<code>255</code>',
      'Error: no se puede sumar str con int',
      '<code>25 5</code>',
    ],
    correct: 2,
    explanation: 'input() devuelve un string ("25"). No se puede sumar "25" + 5 (str + int). Falta usar int() para convertir.',
  },
];
