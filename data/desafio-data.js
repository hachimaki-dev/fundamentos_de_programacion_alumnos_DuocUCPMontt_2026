// ═══════════════════════════════════════════════════════════════
//  🔥 Datos para Modo Desafío — Evaluación Parcial 1
// ═══════════════════════════════════════════════════════════════

const CHALLENGES = [
  // ── Desafío 1: Cirujano de Código (Indentación) ──
  {
    id: 1,
    emoji: '🔬',
    title: 'Cirujano de Código',
    subtitle: 'Ordena las líneas correctamente',
    skill: 'Indentación y estructura',
    type: 'reorder',
    description: 'Las líneas de código están desordenadas. Arrástralas al orden correcto. ¡La indentación importa!',
    exercises: [
      {
        prompt: 'Ordena este programa que verifica si un número es positivo:',
        // Lines shuffled — student must reorder
        shuffled: [
          '    print("Es positivo")',
          'if numero > 0:',
          'numero = int(input("Ingrese número: "))',
          'print("Fin")',
          'else:',
          '    print("No es positivo")',
        ],
        correct: [
          'numero = int(input("Ingrese número: "))',
          'if numero > 0:',
          '    print("Es positivo")',
          'else:',
          '    print("No es positivo")',
          'print("Fin")',
        ],
        hints: [
          '💡 Piensa: ¿qué debe pasar PRIMERO? Antes de evaluar algo, necesitas tenerlo.',
          '💡 Recuerda: las líneas con 4 espacios al inicio van DENTRO de un if o else.',
          '💡 "Fin" se muestra SIEMPRE, así que va al final, sin indentación.',
        ]
      },
      {
        prompt: 'Ordena este programa que pide edad y muestra un mensaje:',
        shuffled: [
          '    print("Eres mayor de edad")',
          'print("Proceso terminado")',
          'edad = int(input("Ingrese edad: "))',
          'else:',
          'if edad >= 18:',
          '    print("Eres menor de edad")',
        ],
        correct: [
          'edad = int(input("Ingrese edad: "))',
          'if edad >= 18:',
          '    print("Eres mayor de edad")',
          'else:',
          '    print("Eres menor de edad")',
          'print("Proceso terminado")',
        ],
        hints: [
          '💡 Primero se pide el dato al usuario con input().',
          '💡 El if y else van al mismo nivel. Lo que está DENTRO lleva 4 espacios.',
          '💡 "Proceso terminado" se muestra siempre → va al final sin indentar.',
        ]
      }
    ]
  },

  // ── Desafío 2: Comillas Perdidas ──
  {
    id: 2,
    emoji: '✏️',
    title: 'Comillas Perdidas',
    subtitle: '¿Con comillas o sin comillas?',
    skill: 'Strings vs variables vs números',
    type: 'fillgaps',
    description: 'Completa los huecos. Decide si el valor lleva comillas dobles ("") o no. ¡Un error de comillas cambia todo!',
    exercises: [
      {
        prompt: 'Completar para que imprima: Hola mundo',
        template: 'print(___)',
        gaps: [{ id: 'g1', answer: '"Hola mundo"', acceptAlso: ["'Hola mundo'"] }],
        hints: [
          '💡 print() muestra texto. Los textos literales siempre van entre comillas.',
          '💡 Si no pones comillas, Python buscará una variable llamada Hola — y no existe.',
          '💡 La respuesta es un texto literal, debe ir entre comillas: "Hola mundo"',
        ]
      },
      {
        prompt: 'Completar para guardar el número 10 en la variable x:',
        template: 'x = ___',
        gaps: [{ id: 'g1', answer: '10', reject: ['"10"', "'10'"] }],
        hints: [
          '💡 Los números NO llevan comillas. Si pones "10" sería texto, no número.',
          '💡 Con comillas: "10" es texto (no puedes sumar). Sin comillas: 10 es número.',
          '💡 Escribe simplemente: 10',
        ]
      },
      {
        prompt: 'Completar para comparar si la respuesta del usuario es "SI":',
        template: 'if respuesta == ___:',
        gaps: [{ id: 'g1', answer: '"SI"', acceptAlso: ["'SI'"] }],
        hints: [
          '💡 Estamos comparando con un texto específico. Los textos van entre comillas.',
          '💡 Sin comillas, Python buscaría una variable llamada SI.',
          '💡 La respuesta correcta es: "SI"',
        ]
      },
      {
        prompt: 'Completar para convertir texto a número entero:',
        template: 'edad = ___(input("Edad: "))',
        gaps: [{ id: 'g1', answer: 'int', reject: ['"int"', "'int'"] }],
        hints: [
          '💡 int es una función de Python (como print). Las funciones NO llevan comillas.',
          '💡 int() convierte texto a número entero. Es código, no texto.',
          '💡 Escribe: int (sin comillas, es una función)',
        ]
      }
    ]
  },

  // ── Desafío 3: True o False Python Edition ──
  {
    id: 3,
    emoji: '⚡',
    title: 'True o False: Python Edition',
    subtitle: 'Evalúa expresiones como lo haría Python',
    skill: 'Comparadores y booleanos',
    type: 'truefalse',
    description: 'Python evalúa cada expresión como True o False. ¡Tú debes pensar como Python!',
    exercises: [
      { expr: '5 > 3', answer: true, explain: '5 es mayor que 3 → True' },
      { expr: '10 == "10"', answer: false, explain: '10 es int, "10" es str. Son tipos distintos → False' },
      { expr: '7 != 7', answer: false, explain: '7 sí es igual a 7, entonces "no igual" es False' },
      { expr: 'True and False', answer: false, explain: 'and necesita que AMBOS sean True. Uno es False → False' },
      { expr: 'not True', answer: false, explain: 'not invierte: not True → False' },
      { expr: '3 >= 3', answer: true, explain: '>= significa mayor O igual. 3 es igual a 3 → True' },
      { expr: '"hola" == "Hola"', answer: false, explain: 'Python distingue mayúsculas: "h" ≠ "H" → False' },
      { expr: '0 == False', answer: true, explain: 'En Python, 0 equivale a False → True' },
      { expr: 'True or False', answer: true, explain: 'or necesita que AL MENOS UNO sea True → True' },
      { expr: '5 > 3 and 2 < 1', answer: false, explain: '5>3 es True, pero 2<1 es False. True and False → False' },
    ],
    hints: [
      '💡 Recuerda: == compara valores. = asigna valores. ¡No son lo mismo!',
      '💡 Python distingue tipos: un int nunca es igual a un str.',
      '💡 Piensa paso a paso: evalúa cada parte de la expresión por separado.',
    ]
  },

  // ── Desafío 4: Arquitecto de Decisiones ──
  {
    id: 4,
    emoji: '🏗️',
    title: 'Arquitecto de Decisiones',
    subtitle: '¿Qué muestra este código?',
    skill: 'if / elif / else anidados',
    type: 'tracecode',
    description: 'Lee el código con atención y determina qué imprime. Sigue el flujo línea por línea.',
    exercises: [
      {
        code: 'x = 15\nif x > 20:\n    print("A")\nelif x > 10:\n    print("B")\nelse:\n    print("C")',
        options: ['A', 'B', 'C', 'A y B'],
        answer: 'B',
        hints: [
          '💡 x vale 15. ¿Es 15 > 20? Si no, pasa al elif.',
          '💡 ¿Es 15 > 10? ¡Sí! Entonces entra a ESE bloque.',
          '💡 Cuando un elif se cumple, ya NO revisa los demás. Imprime "B".',
        ]
      },
      {
        code: 'edad = 20\ninscrito = "NO"\nif edad >= 18:\n    if inscrito == "SI":\n        print("Aceptado")\n    else:\n        print("Rechazado")\nelse:\n    print("Menor")',
        options: ['Aceptado', 'Rechazado', 'Menor', 'Error'],
        answer: 'Rechazado',
        hints: [
          '💡 edad=20 → ¿20 >= 18? Sí, entra al primer if.',
          '💡 Ahora revisa el if INTERNO: inscrito="NO" → ¿"NO" == "SI"? No.',
          '💡 Como el if interno es falso, entra al else interno → "Rechazado".',
        ]
      },
      {
        code: 'nota = 45\nif nota >= 60:\n    print("Aprobado")\n    if nota >= 90:\n        print("Excelente")\nelse:\n    print("Reprobado")\nprint("Fin")',
        options: ['Aprobado', 'Reprobado\\nFin', 'Aprobado\\nExcelente', 'Reprobado'],
        answer: 'Reprobado\\nFin',
        hints: [
          '💡 nota=45. ¿45 >= 60? No → salta directo al else.',
          '💡 El else imprime "Reprobado". El if interno nunca se evalúa.',
          '💡 print("Fin") está FUERA del if/else (sin indentación), se ejecuta SIEMPRE.',
        ]
      }
    ]
  },

  // ── Desafío 5: El Contador Infinito ──
  {
    id: 5,
    emoji: '🔁',
    title: 'El Contador Infinito',
    subtitle: 'Traza el while paso a paso',
    skill: 'While, contadores, acumuladores',
    type: 'tracetable',
    description: 'Completa la tabla de ejecución del while. Escribe el valor de cada variable en cada iteración.',
    exercises: [
      {
        code: 'contador = 0\nsuma = 0\nwhile contador < 3:\n    suma = suma + 2\n    contador = contador + 1\nprint(suma)',
        vars: ['contador', 'suma', 'contador < 3'],
        table: [
          { row: 'Inicio', values: ['0', '0', 'True'] },
          { row: 'Iter 1', values: ['1', '2', 'True'] },
          { row: 'Iter 2', values: ['2', '4', 'True'] },
          { row: 'Iter 3', values: ['3', '6', 'False'] },
        ],
        finalOutput: '6',
        hints: [
          '💡 En cada iteración, primero suma + 2, LUEGO contador + 1.',
          '💡 La condición se evalúa AL INICIO de cada vuelta.',
          '💡 Cuando contador llega a 3, la condición 3 < 3 es False y se detiene.',
        ]
      },
      {
        code: 'i = 1\nresultado = 0\nwhile i <= 4:\n    resultado = resultado + i\n    i = i + 1\nprint(resultado)',
        vars: ['i', 'resultado', 'i <= 4'],
        table: [
          { row: 'Inicio', values: ['1', '0', 'True'] },
          { row: 'Iter 1', values: ['2', '1', 'True'] },
          { row: 'Iter 2', values: ['3', '3', 'True'] },
          { row: 'Iter 3', values: ['4', '6', 'True'] },
          { row: 'Iter 4', values: ['5', '10', 'False'] },
        ],
        finalOutput: '10',
        hints: [
          '💡 resultado acumula el valor de i ANTES de que i aumente.',
          '💡 Iter 1: resultado = 0 + 1 = 1, luego i = 1 + 1 = 2.',
          '💡 Suma total: 1+2+3+4 = 10. Cuando i=5, 5<=4 es False.',
        ]
      }
    ]
  },

  // ── Desafío 6: Misión Final ──
  {
    id: 6,
    emoji: '🏆',
    title: 'Misión Final: El Programa Completo',
    subtitle: 'Escribe código que funcione',
    skill: 'Pensamiento algorítmico integral',
    type: 'writecode',
    description: 'Escribe un programa completo en Python. No hay opciones, no hay ayuda directa. Solo tú, tu lógica y Python.',
    exercises: [
      {
        prompt: 'Escribe un programa que pida un número al usuario. Si el número es par, muestra "PAR". Si es impar, muestra "IMPAR". Al final siempre muestra "Listo".',
        expectedOutputs: {
          even: ['PAR', 'Listo'],
          odd: ['IMPAR', 'Listo'],
        },
        mustContain: ['input', 'if', 'else', 'print'],
        mustNotContain: [],
        hints: [
          '💡 ¿Cómo saber si un número es par? El operador % (módulo) da el resto de una división.',
          '💡 Un número es par cuando numero % 2 == 0.',
          '💡 Estructura: pedir dato → convertir a int → if/else → print final.',
        ],
        sampleSolution: 'numero = int(input("Ingrese número: "))\nif numero % 2 == 0:\n    print("PAR")\nelse:\n    print("IMPAR")\nprint("Listo")'
      }
    ]
  }
];
