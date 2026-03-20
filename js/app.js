// ═══════════════════════════════════════════════════════════════
//  ⚙️ Motor Vue Reutilizable — Lógica compartida
//  ─────────────────────────────────────────────────────────────
//  Este archivo contiene funciones y mixins reutilizables
//  que cualquier página de ejercicios puede importar.
// ═══════════════════════════════════════════════════════════════

/**
 * Inicializa el estado de un array de ejercicios.
 * Agrega campos de control (answered, selected) a cada ejercicio.
 */
function initState(exercises) {
  return exercises.map(ex => ({
    ...ex,
    answered: false,
    selected: null,
  }));
}

/**
 * Resalta código Python usando Prism.js.
 * Retorna el código sin cambios si Prism no está disponible.
 */
function highlightPython(code) {
  if (typeof Prism !== 'undefined' && Prism.languages.python) {
    return Prism.highlight(code, Prism.languages.python, 'python');
  }
  return code;
}

/**
 * Configura Mermaid con el tema kawaii.
 * Debe llamarse una vez en mounted().
 */
function setupMermaid() {
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({
      startOnLoad: false,
      theme: 'base',
      themeVariables: {
        primaryColor: '#f8bbd0',
        primaryTextColor: '#4a4a4a',
        primaryBorderColor: '#f48fb1',
        secondaryColor: '#e1bee7',
        tertiaryColor: '#b3e5fc',
        lineColor: '#ce93d8',
        fontFamily: 'Quicksand',
        fontSize: '14px',
      },
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis',
      }
    });
  }
}

/**
 * Re-renderiza todos los diagramas mermaid en el DOM.
 * Debe llamarse después de cambiar de tab o resetear.
 */
function renderMermaidDiagrams() {
  if (typeof mermaid !== 'undefined') {
    document.querySelectorAll('.mermaid').forEach(el => {
      el.removeAttribute('data-processed');
    });
    mermaid.run();
  }
}

/**
 * Mixin de Vue para la funcionalidad de quiz/ejercicios.
 * Incluye data, computed, y methods reutilizables.
 */
const quizMixin = {
  data() {
    return {
      activeTab: 'python',
      pythonExercises: initState(typeof pythonExercises !== 'undefined' ? pythonExercises : []),
      flowExercises: initState(typeof flowExercises !== 'undefined' ? flowExercises : []),
      score: 0,
    };
  },
  computed: {
    currentExercises() {
      if (this.activeTab === 'python') return this.pythonExercises;
      if (this.activeTab === 'flow') return this.flowExercises;
      return [];
    },
    answeredCount() {
      return this.currentExercises.filter(e => e.answered).length;
    },
    progressPercent() {
      if (this.currentExercises.length === 0) return 0;
      return Math.round((this.answeredCount / this.currentExercises.length) * 100);
    },
  },
  methods: {
    highlightCode(code) {
      return highlightPython(code);
    },
    switchTab(tab) {
      this.activeTab = tab;
      this.recalcScore();
      this.$nextTick(() => renderMermaidDiagrams());
    },
    selectOption(exerciseIdx, optionIdx) {
      const ex = this.currentExercises[exerciseIdx];
      if (ex.answered) return;
      ex.selected = optionIdx;
      ex.answered = true;
      if (optionIdx === ex.correct) {
        this.score++;
      }
    },
    recalcScore() {
      this.score = this.currentExercises.filter(e => e.answered && e.selected === e.correct).length;
    },
    resetAll() {
      if (this.activeTab === 'python') {
        this.pythonExercises = initState(pythonExercises);
      } else if (this.activeTab === 'flow') {
        this.flowExercises = initState(flowExercises);
      }
      this.recalcScore();
      this.$nextTick(() => renderMermaidDiagrams());
      window.scrollTo({ top: 0 });
    },
  },
  mounted() {
    setupMermaid();
    // Check hash to select initial tab
    const hash = window.location.hash.replace('#', '');
    if (hash === 'flow' || hash === 'python') {
      this.activeTab = hash;
    }
    this.$nextTick(() => renderMermaidDiagrams());
  },
};
