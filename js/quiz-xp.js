// ═══════════════════════════════════════════════════════════════
//  📊 Quiz XP Module — Otorga XP al completar ejercicios
//  ─────────────────────────────────────────────────────────────
//  Se importa en las páginas de quiz (for-loop, while-loop, etc.)
//  Usa la función RPC complete_quiz() de Supabase.
//  Requiere que supabase-client.js ya esté cargado.
// ═══════════════════════════════════════════════════════════════

const QuizXP = (() => {
  'use strict';

  let _submitted = {};  // Evitar envíos duplicados por sección

  /**
   * Envía el resultado de un quiz/sección a Supabase para otorgar XP
   * @param {string} quizId - Identificador único del quiz (ej: 'for-loop-choice')
   * @param {number} score - Puntaje obtenido
   * @param {number} total - Puntaje máximo posible
   * @returns {Promise<{xp_awarded, percentage, improved}>}
   */
  async function submitQuizResult(quizId, score, total) {
    // Evitar duplicados
    if (_submitted[quizId]) {
      console.log(`[QuizXP] Quiz "${quizId}" ya fue enviado en esta sesión.`);
      return null;
    }

    // Verificar que SupabaseManager existe
    if (typeof SupabaseManager === 'undefined') {
      console.warn('[QuizXP] SupabaseManager no disponible. XP no se otorgará.');
      return null;
    }

    // Verificar que el usuario está autenticado
    const user = await SupabaseManager.getUser();
    if (!user) {
      console.log('[QuizXP] Usuario no autenticado. XP no se otorgará.');
      return null;
    }

    try {
      const client = SupabaseManager.getClient();
      const { data, error } = await client.rpc('complete_quiz', {
        p_quiz_id: quizId,
        p_score: score,
        p_total: total
      });

      if (error) {
        console.error('[QuizXP] Error al completar quiz:', error.message);
        return null;
      }

      _submitted[quizId] = true;

      // Parsear resultado (viene como JSON del RPC)
      const result = typeof data === 'string' ? JSON.parse(data) : data;

      // Mostrar notificación
      if (result.xp_awarded > 0) {
        const pct = Math.round(result.percentage);
        let emoji = '🎉';
        if (pct >= 90) emoji = '🏆';
        else if (pct >= 70) emoji = '🔥';
        else if (pct >= 50) emoji = '💪';
        
        SupabaseManager.showToast(
          `${emoji} ¡+${result.xp_awarded} XP! Quiz completado con ${pct}%`,
          'success',
          5000
        );
      } else if (result.improved === false) {
        SupabaseManager.showToast(
          '✅ Quiz registrado. Mejora tu puntaje para ganar más XP.',
          'info',
          4000
        );
      }

      return result;
    } catch (e) {
      console.error('[QuizXP] Error inesperado:', e);
      return null;
    }
  }

  /**
   * Helper para mixin de Vue: Agrega un watcher que envía XP al completar
   * Uso en Vue app: mixins: [QuizXP.vueMixin('for-loop')]
   */
  function vueMixin(baseQuizId) {
    return {
      watch: {
        allAnswered(newVal) {
          if (newVal && this.sectionScore !== undefined && this.sectionTotal !== undefined) {
            const quizId = `${baseQuizId}-${this.currentSection || 'main'}`;
            QuizXP.submitQuizResult(quizId, this.sectionScore, this.sectionTotal);
          }
        }
      }
    };
  }

  return {
    submitQuizResult,
    vueMixin,
  };
})();
