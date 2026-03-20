// ═══════════════════════════════════════════════════════════════
//  📦 Ejercicios de Diagramas de Flujo — Datos puros
//  ─────────────────────────────────────────────────────────────
//  Para agregar más ejercicios, copia un bloque { ... } y pégalo
//  al final del array.
//
//  Campos:
//    type        → 'flow'
//    title       → título del ejercicio
//    instruction → instrucción breve
//    diagram     → sintaxis Mermaid (flowchart TD)
//    inputHint   → (opcional) qué valores de entrada usar
//    question    → la pregunta
//    options     → array de 4 alternativas (admite HTML)
//    correct     → índice de la correcta (0=A, 1=B, 2=C, 3=D)
//    explanation → texto que se muestra al responder
// ═══════════════════════════════════════════════════════════════

const flowExercises = [
  {
    type: 'flow',
    title: 'Suma de dos números',
    instruction: 'Observa el diagrama y determina la salida.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/Ingrese un número: a/]
    B --> C[/Ingrese otro número: b/]
    C --> D["resultado = a + b"]
    D --> E[/"Mostrar: 'El resultado es:', resultado"/]
    E --> F([Fin])`,
    inputHint: 'a → 4, b → 6',
    question: '¿Qué muestra la salida?',
    options: [
      '<code>El resultado es: 10</code>',
      '<code>El resultado es: 46</code>',
      '<code>resultado = 10</code>',
      '<code>Error</code>',
    ],
    correct: 0,
    explanation: 'Se leen a=4 y b=6, se suman: resultado = 10. Se muestra "El resultado es: 10".',
  },
  {
    type: 'flow',
    title: 'Aprobado o Reprobado',
    instruction: 'Sigue el flujo del diagrama con la entrada dada.',
    diagram: `flowchart TD
    A([Inicio]) --> B["nota = 0"]
    B --> C[/"Ingrese nota (1-7): nota"/]
    C --> D{"nota >= 4?"}
    D -- Sí --> E["resultado = 'Aprobado'"]
    D -- No --> F["resultado = 'Reprobado'"]
    E --> G[/"Mostrar: resultado"/]
    F --> G
    G --> H([Fin])`,
    inputHint: 'nota → 5',
    question: '¿Qué muestra la salida?',
    options: [
      '<code>Reprobado</code>',
      '<code>Aprobado</code>',
      '<code>5</code>',
      '<code>nota >= 4</code>',
    ],
    correct: 1,
    explanation: 'nota=5. ¿5 >= 4? → Sí → resultado = "Aprobado". Se muestra "Aprobado".',
  },
  {
    type: 'flow',
    title: 'Mayor de Edad',
    instruction: 'Observa la compuerta lógica del diagrama.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese su edad: edad"/]
    B --> C{"edad >= 18?"}
    C -- Sí --> D[/"Mostrar: 'Eres mayor de edad'"/]
    C -- No --> E[/"Mostrar: 'Eres menor de edad'"/]
    D --> F([Fin])
    E --> F`,
    inputHint: 'edad → 15',
    question: '¿Qué se muestra?',
    options: [
      '<code>Eres mayor de edad</code>',
      '<code>Eres menor de edad</code>',
      '<code>15</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'edad=15. ¿15 >= 18? → No → Se muestra "Eres menor de edad".',
  },
  {
    type: 'flow',
    title: 'Cálculo de Descuento',
    instruction: 'Determina el total con el descuento aplicado.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese precio: precio"/]
    B --> C{"precio > 10000?"}
    C -- Sí --> D["descuento = precio * 0.1"]
    C -- No --> E["descuento = 0"]
    D --> F["total = precio - descuento"]
    E --> F
    F --> G[/"Mostrar: 'Total:', total"/]
    G --> H([Fin])`,
    inputHint: 'precio → 15000',
    question: '¿Cuál es el total mostrado?',
    options: [
      '<code>Total: 15000</code>',
      '<code>Total: 13500</code>',
      '<code>Total: 1500</code>',
      '<code>Total: 10000</code>',
    ],
    correct: 1,
    explanation: 'precio=15000. ¿15000 > 10000? → Sí → descuento = 1500. total = 15000 - 1500 = 13500.',
  },
  {
    type: 'flow',
    title: 'Par o Impar',
    instruction: 'Sigue el flujo lógico del diagrama.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese número: n"/]
    B --> C["resto = n % 2"]
    C --> D{"resto == 0?"}
    D -- Sí --> E[/"Mostrar: 'Es par'"/]
    D -- No --> F[/"Mostrar: 'Es impar'"/]
    E --> G([Fin])
    F --> G`,
    inputHint: 'n → 7',
    question: '¿Qué muestra la salida?',
    options: [
      '<code>Es par</code>',
      '<code>Es impar</code>',
      '<code>resto = 1</code>',
      '<code>7</code>',
    ],
    correct: 1,
    explanation: 'n=7. resto = 7 % 2 = 1. ¿1 == 0? → No → "Es impar".',
  },
  {
    type: 'flow',
    title: 'Categoría por Edad',
    instruction: 'Observa las dos compuertas lógicas en secuencia.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese edad: edad"/]
    B --> C{"edad < 13?"}
    C -- Sí --> D[/"Mostrar: 'Niño'"/]
    C -- No --> E{"edad < 18?"}
    E -- Sí --> F[/"Mostrar: 'Adolescente'"/]
    E -- No --> G[/"Mostrar: 'Adulto'"/]
    D --> H([Fin])
    F --> H
    G --> H`,
    inputHint: 'edad → 16',
    question: '¿Qué categoría se muestra?',
    options: [
      '<code>Niño</code>',
      '<code>Adolescente</code>',
      '<code>Adulto</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'edad=16. ¿16 < 13? → No. ¿16 < 18? → Sí → "Adolescente".',
  },
  {
    type: 'flow',
    title: 'Número Positivo, Negativo o Cero',
    instruction: 'Sigue las decisiones paso a paso.',
    diagram: `flowchart TD
    A([Inicio]) --> B[/"Ingrese número: n"/]
    B --> C{"n > 0?"}
    C -- Sí --> D[/"Mostrar: 'Positivo'"/]
    C -- No --> E{"n < 0?"}
    E -- Sí --> F[/"Mostrar: 'Negativo'"/]
    E -- No --> G[/"Mostrar: 'Es cero'"/]
    D --> H([Fin])
    F --> H
    G --> H`,
    inputHint: 'n → 0',
    question: '¿Qué se imprime?',
    options: [
      '<code>Positivo</code>',
      '<code>Negativo</code>',
      '<code>Es cero</code>',
      '<code>0</code>',
    ],
    correct: 2,
    explanation: 'n=0. ¿0 > 0? → No. ¿0 < 0? → No → "Es cero".',
  },
  {
    type: 'flow',
    title: 'Verificar Contraseña',
    instruction: 'Observa la comparación de cadenas.',
    diagram: `flowchart TD
    A([Inicio]) --> B["clave = '1234'"]
    B --> C[/"Ingrese contraseña: intento"/]
    C --> D{"intento == clave?"}
    D -- Sí --> E[/"Mostrar: 'Acceso permitido'"/]
    D -- No --> F[/"Mostrar: 'Acceso denegado'"/]
    E --> G([Fin])
    F --> G`,
    inputHint: 'intento → "abcd"',
    question: '¿Qué se muestra?',
    options: [
      '<code>Acceso permitido</code>',
      '<code>Acceso denegado</code>',
      '<code>1234</code>',
      '<code>Error</code>',
    ],
    correct: 1,
    explanation: 'clave="1234", intento="abcd". ¿"abcd" == "1234"? → No → "Acceso denegado".',
  },
];
