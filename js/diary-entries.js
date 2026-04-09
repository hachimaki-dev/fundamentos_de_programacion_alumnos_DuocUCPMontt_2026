// ═══════════════════════════════════════════════════════════════
//  🗓️ Registro Central de Entradas del Diario
//  ─────────────────────────────────────────────────────────────
//  Para agregar una nueva entrada al diario, simplemente agrega
//  un nuevo objeto al array. La UI se genera automáticamente.
//
//  Campos:
//    id          → identificador único (slug)
//    date        → fecha de publicación (para ordenar y mostrar)
//    emoji       → emoji representativo
//    title       → título de la entrada
//    description → descripción breve (1-2 líneas)
//    tags        → array de etiquetas ['python','flow','docs','nuevo']
//    page        → ruta relativa a la página (desde index.html)
//    isNew       → (bool) marca visual de "nuevo"
// ═══════════════════════════════════════════════════════════════

const diaryEntries = [
  {
    id: 'entrada-0-git',
    date: '2026-03-05',
    emoji: '🐙',
    title: 'Entrada 0: Lo básico de Git',
    description: 'Comandos esenciales (init, commit, status, ramas) y flujos de trabajo recomendados.',
    tags: ['docs'],
    page: 'pages/git-basics.html',
    isNew: false,
  },
  {
    id: 'semana-1-ejercicios',
    date: '2026-03-10',
    emoji: '🐍',
    title: 'Ejercicios de Trazado — Semana 1',
    description: 'Practica trazado de código Python: variables, tipos de datos, operadores y lógica. 10 ejercicios interactivos con feedback inmediato.',
    tags: ['python'],
    page: 'pages/exercises.html#python',
    isNew: false,
  },
  {
    id: 'semana-1-diagramas',
    date: '2026-03-10',
    emoji: '🔷',
    title: 'Diagramas de Flujo — Semana 1',
    description: 'Sigue el flujo de diagrama paso a paso y determina la salida. 8 ejercicios con decisiones y cálculos.',
    tags: ['flow'],
    page: 'pages/exercises.html#flow',
    isNew: false,
  },
  {
    id: 'documentacion-fundamentos',
    date: '2026-03-10',
    emoji: '📚',
    title: 'Documentación de Referencia',
    description: 'Guía rápida de consulta: variables, tipos de datos, operadores, input/output, diagramas de flujo y estrategias de resolución.',
    tags: ['docs'],
    page: 'pages/docs.html',
    isNew: false,
  },
  {
    id: 'semana-2-condicionales',
    date: '2026-03-17',
    emoji: '🔀',
    title: 'Condicionales if/elif/else — Semana 2',
    description: 'Taller completo: referencia, selección múltiple, verdadero/falso, unir conceptos, diagramas de flujo y trazado de código. ¡26 ejercicios interactivos!',
    tags: ['python', 'flow', 'docs'],
    page: 'pages/conditionals.html',
    isNew: false,
  },
  {
    id: 'semana-3-while',
    date: '2026-03-23',
    emoji: '🔁',
    title: 'Ciclo while — Semana 3',
    description: 'Taller completo: referencia, selección múltiple, V/F, unir conceptos, encontrar errores, completar código y trazar código. ¡37 ejercicios interactivos!',
    tags: ['python', 'docs'],
    page: 'pages/while-loop.html',
    isNew: true,
  },
  {
    id: 'semana-3-for',
    date: '2026-03-30',
    emoji: '🔄',
    title: 'Ciclo for — Semana 3',
    description: 'Taller completo: referencia, selección múltiple, V/F, unir conceptos, encontrar errores, completar código y trazar código. ¡39 ejercicios interactivos con for, range, break, continue y strings!',
    tags: ['python', 'docs'],
    page: 'pages/for-loop.html',
    isNew: false,
  },
  {
    id: 'quiz-interactivo-repaso',
    date: '2026-03-30',
    emoji: '🎮',
    title: 'Juego Interactivo: Repaso de Python',
    description: 'Juego estilo Kahoot para validar conocimientos en la pizarra. Cubre variables, input, output, tipos, if y while.',
    tags: ['python'],
    page: 'pages/quiz-interactivo.html',
    isNew: false,
  },
  {
    id: 'desafio-evaluacion-1',
    date: '2026-04-01',
    emoji: '🔥',
    title: 'Modo Desafío: Preparación Evaluación',
    description: 'Misiones para prepararte para el parcial. Ataca tus debilidades en indentación, comillas, bucles y condiciones.',
    tags: ['python'],
    page: 'pages/desafio-evaluacion.html',
    isNew: false,
  },
  {
    id: 'banco-ejercicios-eleccion',
    date: '2026-04-01',
    emoji: '🛒',
    title: 'Banco de Ejercicios: Elección Libre',
    description: '15 misiones de programación con temáticas muy diversas (juegos, salud, delivery). Arma tu propia guía eligiendo de 3 a 5 misiones.',
    tags: ['python'],
    page: 'pages/banco-ejercicios.html',
    isNew: false,
  },
  {
    id: 'evaluacion-formativa-1',
    date: '2026-04-06',
    emoji: '📝',
    title: 'Simulador de Evaluación 1',
    description: 'Prueba formativa integral (Tipo Universidad). Incluye alternativas, V/F, términos pareados y 3 ejercicios de desarrollo con control de flujo.',
    tags: ['python', 'docs', 'flow'],
    page: 'pages/evaluacion-1.html',
    isNew: true,
  },
  {
    id: 'mecanismos-ruptura-menus',
    date: '2026-04-09',
    emoji: '🚀',
    title: 'Mecanismos de Ruptura y Menús',
    description: 'Taller completo de break, continue, lógicas complejas y menús interactivos. ¡Con temáticas de Minecraft, K-Pop, LoL y retos propuestos!',
    tags: ['python', 'docs'],
    page: 'pages/mecanismos-ruptura.html',
    isNew: true,
  }
];
