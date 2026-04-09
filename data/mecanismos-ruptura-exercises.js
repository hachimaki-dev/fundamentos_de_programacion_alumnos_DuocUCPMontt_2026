// ═══════════════════════════════════════════════════════════════
//  📦 Taller — Mecanismos de Ruptura y Menús en Python
//  ─────────────────────────────────────────────────────────────
//  Ejercicios: selección múltiple, verdadero/falso, unir,
//  encontrar el error, completar código, trazar código.
// ═══════════════════════════════════════════════════════════════

// ─── SECCIÓN 1: Selección Múltiple ───
const rupturaChoiceExercises = [
  {
    type: 'choice',
    title: '¿Qué hace la sentencia break?',
    instruction: 'Elige la definición más precisa sobre "break".',
    question: 'En un ciclo while, ¿cuál es el comportamiento exacto de "break"?',
    options: [
      'Pausa el programa hasta que el usuario presione una tecla.',
      'Rompe o termina completamente el ciclo en el que se encuentra, pasando a la instrucción siguiente al ciclo.',
      'Salta todo lo que queda del bloque y vuelve al inicio del ciclo para evaluar la condición.',
      'Cierra el programa de Python por completo.'
    ],
    correct: 1,
    explanation: 'La instrucción "break" rompe el ciclo actual de forma repentina e inmediata. La ejecución salta a la primera línea de código después de terminar el bloque del bucle.',
  },
  {
    type: 'choice',
    title: '¿Qué hace la sentencia continue?',
    instruction: 'Piensa en la diferencia entre break y continue.',
    question: '¿Qué hace "continue" cuando se ejecuta dentro de un while?',
    options: [
      'Termina el programa.',
      'Añade un valor continuo a una variable.',
      'Salta el resto del código dentro del bloque y vuelve al inicio (a la evaluación de la condición) para la próxima iteración.',
      'Es exactamente lo mismo que "break".'
    ],
    correct: 2,
    explanation: '"continue" no rompe el ciclo; solo interrumpe la iteración *actual*. Salta lo que quede de bloque y vuelve arriba para revisar la condición de nuevo.',
  },
  {
    type: 'choice',
    title: 'Ciclo while con "or"',
    instruction: 'Analiza la evaluación de condiciones dobles.',
    question: 'Si tienes: `while accion == "saltar" or accion == "correr":`, ¿cuándo entrará al ciclo?',
    options: [
      'Cuando accion valga "saltar", o cuando valga "correr". Basta con que una se cumpla.',
      'Solo cuando accion valga ambas cosas a la vez (imposible).',
      'Cuando accion sea cualquier palabra distinta a "saltar" o "correr".',
      'Nunca va a entrar por un error de sintaxis.'
    ],
    correct: 0,
    explanation: 'El operador lógico "or" requiere que al menos UNA de las expresiones sea Verdadera para que la condición completa sea True.',
  },
  {
    type: 'choice',
    title: 'Menús Interactivos',
    instruction: 'Revisa la lógica para armar un menú.',
    question: '¿Por qué se usa un ciclo para crear un menú interactivo en una aplicación (como en Minecraft o Valorant)?',
    options: [
      'Para que el menú se vea más bonito en pantalla.',
      'Para que el usuario pueda tomar múltiples decisiones, entrar y salir de opciones, hasta que elija expresamente "Salir".',
      'Para gastar menos memoria RAM.',
      'No se necesitan ciclos para los menús continuos.'
    ],
    correct: 1,
    explanation: 'Los ciclos while son el pilar de los menús (ej: `while opcion != "Salir":`) porque mantienen el programa funcionando y "escuchando" las peticiones del usuario repetidamente.',
  }
];

// ─── SECCIÓN 2: Verdadero o Falso ───
const rupturaTfExercises = [
  {
    type: 'tf',
    title: 'continue y el final del ciclo',
    statement: '<code>continue</code> rompe por completo el ciclo, y el programa continúa con la línea de código que está después del while.',
    correct: false,
    explanation: 'Falso. Ese es el efecto de <code>break</code>. <code>continue</code> solo salta el resto de la *vuelta actual* y regresa al inicio del bloque.',
  },
  {
    type: 'tf',
    title: 'Uso de while True',
    statement: 'Es un patrón común usar <code>while True:</code> junto a un <code>if</code> y un <code>break</code> adentro, para detener el ciclo cuando ocurre un evento específico.',
    correct: true,
    explanation: 'Verdadero. Muchas veces se declara <code>while True:</code> y, al suceder alguna condición (ej. que la vida llegue a 0), se llama a <code>break</code>.',
  },
  {
    type: 'tf',
    title: 'If dentro de While',
    statement: 'No está permitido usar un <code>if</code> y un <code>else</code> dentro de un ciclo <code>while</code>.',
    correct: false,
    explanation: 'Falso. Las estructuras condicionales (if/elif/else) se pueden "anidar" dentro de un ciclo while o for (y viceversa) sin ningún problema. Esencial para Menús.',
  },
  {
    type: 'tf',
    title: 'Operador AND',
    statement: 'Para que <code>while vida > 0 and pociones > 0:</code> sea True, ambas condiciones deben cumplirse a la vez.',
    correct: true,
    explanation: 'Verdadero. El operador lógico <code>and</code> exige que tanto la condición izquierda como la derecha sean Verdaderas.',
  },
  {
    type: 'tf',
    title: 'Orden de Instrucciones',
    statement: 'Si pongo <code>continue</code> en la primera línea del <code>while</code>, las líneas de abajo nunca se van a ejecutar.',
    correct: true,
    explanation: 'Verdadero. Al ejecutarse <code>continue</code> inmediatamente, se vuelve de inmediato al inicio, por lo que el resto del bloque estructurado quedará inalcanzable (código muerto).',
  }
];

// ─── SECCIÓN 3: Unir Conceptos ───
const rupturaMatchExercises = [
  {
    type: 'match',
    title: 'Conecta cada concepto lógico con su función en la ruptura',
    pairs: [
      { left: '<code>break</code>', right: 'Abandona el ciclo completamente.', id: 'a' },
      { left: '<code>continue</code>', right: 'Abandona solo la iteración actual.', id: 'b' },
      { left: '<code>while True:</code>', right: 'Ciclo infinito; se apoya en una ruptura manual.', id: 'c' },
      { left: 'Condición Compuesta', right: 'Uso de operadores and/or para verificar múltiples cosas.', id: 'd' }
    ]
  },
  {
    type: 'match',
    title: 'Conecta el evento de videojuego con su operador lógico',
    pairs: [
      { left: 'Basta con morir O elegir salir (una de las dos)', right: '<code>or</code>', id: 'a' },
      { left: 'Tiene que tener maná Y estar apuntando a un enemigo (ambas)', right: '<code>and</code>', id: 'b' },
      { left: 'El menú se rompe si elige "Q"', right: '<code>if opcion == "Q": break</code>', id: 'c' },
      { left: 'Saltea el ataque por armadura', right: '<code>if block: continue</code>', id: 'd' }
    ]
  }
];

// ─── SECCIÓN 4: Encontrar el Error ───
const rupturaErrorExercises = [
  {
    type: 'error',
    title: 'El Continue Inmortal',
    instruction: 'Lee este código. Intenta descubrir el bug intencional.',
    code: `while True:
    numero = int(input("Ingresa un número (-1 para salir): "))
    if numero % 3 == 0:
        continue
    if numero == -1:
        break
    print("Número aceptado:", numero)`,
    question: '¿Qué sucede si el usuario ingresa -1 para poder salir?',
    options: [
      'Sale del ciclo normalmente y el programa termina.',
      'Imprime "Número aceptado: -1".',
      'Entra en un loop infinito porque -1 % 3 no es 0.',
      'Nunca sale, porque -1 también entra a la condición `if numero % 3 == 0` y ejecuta el continue.'
    ],
    correct: 0, 
    explanation: 'Es engañoso: Aunque -1 % 3 es 2 en Python (no 0), avanza a `if numero == -1` y hace `break`. ¡Sorpresa, aquí en realidad SÍ sale! Pero si ingresaran "0" como salir, el % 3 daría 0, ejecutaría continue y ¡nunca evaluaría si era 0!. La respuesta es que sale normalmente.',
  },
  {
    type: 'error',
    title: 'Bloque Inalcanzable',
    instruction: 'Identifica la estructura "código zombie".',
    code: `i = 0
while True:
    print(i)
    break
    if i == 2:
        print("Llegamos a dos")
    i += 1`,
    question: '¿Por qué el if y el i += 1 nunca se van a ejecutar?',
    options: [
      'Porque i siempre valdrá 0.',
      'Porque el programa detecta un error de sintaxis al tener break antes del if.',
      'Porque la instrucción break rompe el ciclo en la iteración 1, interrumpiendo el flujo antes de llegar a las demás instrucciones.',
      'Sí se van a ejecutar.'
    ],
    correct: 2,
    explanation: 'El break incondicional rompe el bucle automáticamente tras el print de "0". El resto del bloque jamás será evaluado.',
  },
  {
    type: 'error',
    title: 'Validación Lógica Confusa',
    instruction: 'Un usuario quiere seguir jugando mientras el estado sea "Jugando"... o si su KDA es mayor a 1.',
    code: `estado = "Jugando"
kda = 2
while estado == "Jugando" and kda > 1:
    print("¡Continúas en la partida de Valorant!")
    estado = input("¿Renunciar? (Si/Jugando): ")
    kda = kda - 0.5`,
    question: '¿Qué pasa si el jugador escribe "Jugando", pero el KDA baja de 1?',
    options: [
      'Sigue jugando porque escribió "Jugando".',
      'Termina el programa porque al usar `and`, DEBEN cumplirse AMBAS condiciones, así que al perder KDA, rompe.',
      'Aparece un error',
      'El programa entra en ciclo infinito.'
    ],
    correct: 1,
    explanation: 'Si una de las condiciones del `and` se vuelve falsa (kda baja a 1 o inferior), la condición general del while es False y el ciclo finaliza.',
  }
];

// ─── SECCIÓN 5: Completar el Código ───
const rupturaCompleteExercises = [
  {
    type: 'complete',
    title: 'Menú de Selección de Campeón de LoL',
    instruction: 'Completa este ciclo para asegurar que el usuario ingrese "Bloquear" o "Elegir".',
    code: `accion = ""\nwhile accion _____ "Bloquear" _____ accion _____ "Elegir":\n    accion = input("¿Elegir o Bloquear campeón? ")\nprint("¡Riot dice: A la Grieta!")`,
    question: 'Para que repita MIENTRAS la acción sea inválida (no sea ninguna de las dos), completamos con:',
    options: [
      '<code>==</code>, <code>and</code>, <code>==</code>',
      '<code>!=</code>, <code>and</code>, <code>!=</code>',
      '<code>!=</code>, <code>or</code>, <code>!=</code>',
      '<code>==</code>, <code>or</code>, <code>==</code>'
    ],
    correct: 1,
    explanation: 'Mientras la acción sea DISTINTA de "Bloquear" Y también sea DISTINTA de "Elegir" (significa que es inválida), seguimos preguntando.',
  },
  {
    type: 'complete',
    title: 'Saltarse la penalización',
    instruction: 'Queremos iterar números del 1 al 5. Imprimir todos, MENOS el 3 usando continue.',
    code: `i = 0\nwhile i < 5:\n    i += 1\n    if i == 3:\n        _____\n    print("Minion farmeado:", i)`,
    question: 'Completa el espacio en blanco',
    options: [
      '<code>break</code>',
      '<code>continue</code>',
      '<code>pass</code>',
      '<code>return</code>'
    ],
    correct: 1,
    explanation: 'Si colocamos continue, al llegar a i == 3 se saltará el print, no lo cuenta, y volverá al inicio con el i == 4.',
  }
];

// ─── SECCIÓN 6: Trazar código Python ───
const rupturaTraceExercises = [
  {
    type: 'trace',
    title: '¿Cuántas veces imprime "Tick"?',
    instruction: 'Haz la traza de este micro-reto. Ojo con el continue.',
    code: `i = 0\nwhile i < 5:\n    i += 1\n    if i == 3:\n        continue\n    print("Tick", i)`,
    inputHint: null,
    question: 'Predice la salida sin ejecutar:',
    options: [
      '<code>Tick 1</code><br><code>Tick 2</code><br><code>Tick 3</code><br><code>Tick 4</code><br><code>Tick 5</code>',
      '<code>Tick 1</code><br><code>Tick 2</code><br><code>Tick 4</code><br><code>Tick 5</code>',
      '<code>Tick 1</code><br><code>Tick 2</code>',
      '<code>Tick 4</code><br><code>Tick 5</code>'
    ],
    correct: 1,
    explanation: 'En i=1 imprime. En i=2 imprime. En i=3 entra al if y ejecuta "continue", saltándose el print de ese número. En i=4 imprime. En i=5 imprime.',
  },
  {
    type: 'trace',
    title: '¿En qué momento se rompe la minería?',
    instruction: 'Analiza el flujo y en qué número hace break.',
    code: `bloques = 0\nwhile True:\n    print("Picando bloque:", bloques)\n    if bloques == 2:\n        break\n    bloques += 1\nprint("Regresar a base")`,
    inputHint: null,
    question: 'Predice la salida:',
    options: [
      '<code>Picando bloque: 0</code><br><code>Picando bloque: 1</code><br><code>Picando bloque: 2</code><br><code>Regresar a base</code>',
      '<code>Picando bloque: 0</code><br><code>Picando bloque: 1</code><br><code>Regresar a base</code>',
      '<code>Picando bloque: 2</code><br><code>Regresar a base</code>',
      '<code>Picando bloque: 1</code><br><code>Picando bloque: 2</code><br><code>Picando bloque: 3</code><br><code>Regresar a base</code>'
    ],
    correct: 0,
    explanation: 'En iteración 1: bloques=0 (imprime "0", sigue). En iter 2: bloques=1 (imprime "1", sigue). En iter 3: bloques=2 (imprime "2", luego if bloques==2 hace break). Luego imprime "Regresar a base".',
  },
  {
    type: 'trace',
    title: 'Generación de Menú Engañoso',
    instruction: 'Mira bien las condiciones.',
    code: `opcion = ""\nwhile opcion != "Salir":\n    opcion = input("A, B o Salir: ")\n    if opcion == "A":\n        print("Atacar")\n        break\n    if opcion == "B":\n        continue\n        print("Defender")`,
    inputHint: 'Si el usuario ingresa B, luego A',
    question: '¿Qué sucederá?',
    options: [
      'Aparecerá "Defender", luego "Atacar"',
      'No se imprime nada, luego "Atacar", luego sale del bucle',
      'Aparece "Defender" pero el ciclo no se detiene',
      'Sale inmediatamente en B'
    ],
    correct: 1,
    explanation: 'Al ingresar "B", hace continue. La instrucción print("Defender") está debajo de continue, es código inalcanzable. Vuelve al menú y al ingresar "A" imprime "Atacar" y hace break.',
  }
];
