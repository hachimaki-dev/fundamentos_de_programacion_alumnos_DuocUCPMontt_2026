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
    isNew: true,
  },
];
