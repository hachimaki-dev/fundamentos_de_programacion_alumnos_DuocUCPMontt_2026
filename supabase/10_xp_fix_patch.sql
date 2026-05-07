-- ============================================================
-- 🔧 10 — XP FIX PATCH (Security Trigger + Dojo Points)
-- ============================================================
-- EJECUTAR EN SQL EDITOR DE SUPABASE
-- Este parche corrige el bug crítico donde el trigger de seguridad
-- bloqueaba TODOS los cambios de XP, incluyendo los de triggers
-- y funciones internas.
-- También añade el sistema de puntos exclusivos por dojo.
-- ============================================================

-- ============================================================
-- 1. FIX CRÍTICO: Reescribir protect_gamification_columns()
-- ============================================================
-- El bug: current_setting('role') SIEMPRE devuelve 'authenticated' 
-- en Supabase, incluso dentro de SECURITY DEFINER functions.
-- Solución: usar una variable de sesión como flag bypass.

CREATE OR REPLACE FUNCTION public.protect_gamification_columns()
RETURNS TRIGGER AS $$
BEGIN
  -- Si la variable de sesión 'app.bypass_gamification_protection' está 
  -- seteada a 'true', significa que la llamada viene de una función 
  -- interna (award_xp_and_badge, triggers, etc.) y debe permitirse.
  IF current_setting('app.bypass_gamification_protection', true) IS DISTINCT FROM 'true' THEN
    -- Proteger: restaurar valores de gamificación para evitar trampas
    NEW.xp := OLD.xp;
    NEW.level := OLD.level;
    NEW.achievements := OLD.achievements;
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- 2. FIX: Reescribir award_xp_and_badge() con bypass flag
-- ============================================================

CREATE OR REPLACE FUNCTION public.award_xp_and_badge(
  target_user UUID, 
  xp_amount INTEGER, 
  badge_id TEXT DEFAULT NULL
) RETURNS VOID AS $$
DECLARE
  current_achievements TEXT[];
  user_faction UUID;
BEGIN
  -- Activar bypass para que el trigger de seguridad nos deje pasar
  PERFORM set_config('app.bypass_gamification_protection', 'true', true);

  -- Obtener logros actuales y facción
  SELECT achievements, faction_id 
  INTO current_achievements, user_faction 
  FROM public.profiles 
  WHERE id = target_user;
  
  -- Si badge_id fue provisto y no lo tiene, lo añadimos
  IF badge_id IS NOT NULL AND NOT (badge_id = ANY(COALESCE(current_achievements, '{}'))) THEN
    UPDATE public.profiles 
    SET 
      xp = COALESCE(xp, 0) + xp_amount,
      achievements = array_append(COALESCE(achievements, '{}'), badge_id)
    WHERE id = target_user;
  ELSE
    -- Solo sumamos XP (si xp_amount > 0)
    IF xp_amount > 0 THEN
      UPDATE public.profiles 
      SET xp = COALESCE(xp, 0) + xp_amount
      WHERE id = target_user;
    END IF;
  END IF;

  -- Actualizar el XP de la facción si el usuario pertenece a una
  IF user_faction IS NOT NULL AND xp_amount > 0 THEN
    UPDATE public.factions
    SET total_xp = COALESCE(total_xp, 0) + xp_amount
    WHERE id = user_faction;
  END IF;

  -- Desactivar bypass
  PERFORM set_config('app.bypass_gamification_protection', 'false', true);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;


-- ============================================================
-- 3. DOJO POINTS: Agregar tracking de puntos exclusivos
-- ============================================================

-- Columna de XP exclusivo del dojo en participantes
ALTER TABLE public.competition_participants
ADD COLUMN IF NOT EXISTS dojo_xp INTEGER DEFAULT 0;

-- ============================================================
-- 4. TRIGGERS MEJORADOS para XP del Dojo
-- ============================================================

-- A. Al subir solución: +50 XP global + 50 dojo_xp
CREATE OR REPLACE FUNCTION public.trigger_submission_xp()
RETURNS TRIGGER AS $$
BEGIN
  -- Otorga 50 XP global por subir solución
  PERFORM public.award_xp_and_badge(NEW.user_id, 50, 'first_blood');
  
  -- Sumar dojo_xp al participante de esta competencia
  UPDATE public.competition_participants
  SET dojo_xp = COALESCE(dojo_xp, 0) + 50
  WHERE competition_id = NEW.competition_id 
    AND user_id = NEW.user_id;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- B. Al recibir un Like: +10 XP global + 10 dojo_xp para el autor
CREATE OR REPLACE FUNCTION public.trigger_vote_xp()
RETURNS TRIGGER AS $$
DECLARE
  target_author UUID;
  target_comp UUID;
  author_likes INTEGER;
BEGIN
  -- Solo dar XP si es un voto positivo (like)
  IF NEW.vote = 1 THEN
    -- Buscar el autor y la competencia de la submission
    SELECT user_id, competition_id 
    INTO target_author, target_comp 
    FROM public.competition_submissions 
    WHERE id = NEW.submission_id;
    
    IF target_author IS NOT NULL AND target_author != NEW.user_id THEN
      -- Dar 10 XP global al autor
      PERFORM public.award_xp_and_badge(target_author, 10, NULL);
      
      -- Sumar 10 dojo_xp al autor en esta competencia
      UPDATE public.competition_participants
      SET dojo_xp = COALESCE(dojo_xp, 0) + 10
      WHERE competition_id = target_comp 
        AND user_id = target_author;
      
      -- Chequear si llegó a 5 likes para el logro social_butterfly
      SELECT likes_count INTO author_likes 
      FROM public.competition_submissions 
      WHERE id = NEW.submission_id;
      
      IF author_likes >= 4 THEN
        PERFORM public.award_xp_and_badge(target_author, 0, 'social_butterfly');
      END IF;
    END IF;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- C. Al publicar en el muro del dojo: +5 XP global + 5 dojo_xp
CREATE OR REPLACE FUNCTION public.trigger_wall_post_xp()
RETURNS TRIGGER AS $$
BEGIN
  -- XP global
  PERFORM public.award_xp_and_badge(NEW.user_id, 5, NULL);
  
  -- dojo_xp para el participante
  UPDATE public.competition_participants
  SET dojo_xp = COALESCE(dojo_xp, 0) + 5
  WHERE competition_id = NEW.competition_id 
    AND user_id = NEW.user_id;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;


-- ============================================================
-- 5. CLEANUP: Eliminar función huérfana de facciones
-- ============================================================
-- La función update_faction_xp() nunca tuvo trigger asociado
-- y su lógica ya está cubierta en award_xp_and_badge()
DROP FUNCTION IF EXISTS public.update_faction_xp() CASCADE;


-- ============================================================
-- 6. QUIZ COMPLETIONS: Tabla para tracking de ejercicios
-- ============================================================

CREATE TABLE IF NOT EXISTS public.quiz_completions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  quiz_id TEXT NOT NULL,          -- Ej: 'for-loop', 'while-loop', 'conditionals'
  score INTEGER NOT NULL,         -- Puntaje obtenido
  total INTEGER NOT NULL,         -- Puntaje máximo posible
  percentage REAL NOT NULL,       -- Porcentaje (0-100)
  xp_awarded INTEGER DEFAULT 0,  -- XP que se otorgó
  completed_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(user_id, quiz_id)       -- 1 registro por quiz por usuario (se actualiza)
);

ALTER TABLE public.quiz_completions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users read own quiz completions" ON public.quiz_completions
  FOR SELECT TO authenticated USING (auth.uid() = user_id);

CREATE POLICY "Users insert own quiz completions" ON public.quiz_completions
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users update own quiz completions" ON public.quiz_completions
  FOR UPDATE TO authenticated USING (auth.uid() = user_id);

-- RPC para completar un quiz y otorgar XP
CREATE OR REPLACE FUNCTION public.complete_quiz(
  p_quiz_id TEXT,
  p_score INTEGER,
  p_total INTEGER
) RETURNS JSON AS $$
DECLARE
  v_user_id UUID;
  v_percentage REAL;
  v_xp INTEGER;
  v_existing RECORD;
  v_prev_xp INTEGER;
  v_net_xp INTEGER;
BEGIN
  -- Obtener user actual
  v_user_id := auth.uid();
  IF v_user_id IS NULL THEN
    RETURN json_build_object('error', 'Not authenticated');
  END IF;

  -- Calcular porcentaje
  v_percentage := CASE WHEN p_total > 0 THEN (p_score::REAL / p_total::REAL) * 100 ELSE 0 END;
  
  -- Calcular XP basado en rendimiento:
  -- >= 90%: 30 XP
  -- >= 70%: 20 XP
  -- >= 50%: 10 XP  
  -- < 50%: 5 XP (por intentar)
  v_xp := CASE
    WHEN v_percentage >= 90 THEN 30
    WHEN v_percentage >= 70 THEN 20
    WHEN v_percentage >= 50 THEN 10
    ELSE 5
  END;

  -- Chequear si ya completó este quiz antes
  SELECT xp_awarded INTO v_existing FROM public.quiz_completions 
  WHERE user_id = v_user_id AND quiz_id = p_quiz_id;
  
  IF FOUND THEN
    v_prev_xp := COALESCE(v_existing.xp_awarded, 0);
    -- Solo dar XP adicional si mejoró (diferencia)
    v_net_xp := GREATEST(0, v_xp - v_prev_xp);
    
    UPDATE public.quiz_completions
    SET score = p_score,
        total = p_total,
        percentage = v_percentage,
        xp_awarded = GREATEST(v_xp, v_prev_xp), -- Guardar el mejor
        completed_at = now()
    WHERE user_id = v_user_id AND quiz_id = p_quiz_id;
  ELSE
    v_net_xp := v_xp;
    
    INSERT INTO public.quiz_completions (user_id, quiz_id, score, total, percentage, xp_awarded)
    VALUES (v_user_id, p_quiz_id, p_score, p_total, v_percentage, v_xp);
  END IF;

  -- Otorgar XP neto (solo la diferencia si mejoró)
  IF v_net_xp > 0 THEN
    PERFORM public.award_xp_and_badge(v_user_id, v_net_xp, NULL);
  END IF;

  RETURN json_build_object(
    'xp_awarded', v_net_xp,
    'total_quiz_xp', v_xp,
    'percentage', v_percentage,
    'improved', v_net_xp > 0
  );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;


-- ============================================================
-- 7. CODE ROYALE: Tabla de problemas para pool dinámico
-- ============================================================

CREATE TABLE IF NOT EXISTS public.code_royale_problems (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  difficulty TEXT DEFAULT 'medium' CHECK (difficulty IN ('easy', 'medium', 'hard')),
  example_input TEXT,
  example_output TEXT,
  time_limit_seconds INTEGER DEFAULT 300, -- 5 min por defecto
  xp_reward INTEGER DEFAULT 100,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.code_royale_problems ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads royale problems" ON public.code_royale_problems
  FOR SELECT TO authenticated USING (true);

-- Insertar pool inicial de problemas
INSERT INTO public.code_royale_problems (title, description, difficulty, example_input, example_output, time_limit_seconds, xp_reward)
VALUES 
  ('Invertir Diccionario', 
   'Crea una función `invertir(d)` que reciba un diccionario y devuelva uno nuevo donde las llaves sean los valores y los valores las llaves.',
   'medium', '{"a": 1, "b": 2}', '{1: "a", 2: "b"}', 300, 100),
  
  ('Fibonacci con Generador', 
   'Crea un generador `fib(n)` que produzca los primeros `n` números de Fibonacci usando `yield`.',
   'medium', 'fib(7)', '0, 1, 1, 2, 3, 5, 8', 300, 100),
  
  ('Palíndromo Inteligente', 
   'Crea una función `es_palindromo(texto)` que ignore espacios, tildes y mayúsculas. Ejemplo: "Anita lava la tina" → True.',
   'easy', '"Anita lava la tina"', 'True', 240, 80),
  
  ('Matriz Espiral', 
   'Crea una función `espiral(n)` que devuelva una matriz n×n con los números del 1 al n² en orden espiral (sentido horario).',
   'hard', 'espiral(3)', '[[1,2,3],[8,9,4],[7,6,5]]', 420, 150),
  
  ('Contador de Palabras', 
   'Crea una función `contar_palabras(texto)` que devuelva un diccionario con la frecuencia de cada palabra (ignorando mayúsculas).',
   'easy', '"Hola mundo hola"', '{"hola": 2, "mundo": 1}', 180, 80),
  
  ('Ordenamiento Burbuja', 
   'Implementa el algoritmo de Bubble Sort sin usar `.sort()`. La función debe recibir una lista y devolver la lista ordenada.',
   'medium', '[5, 3, 8, 1, 2]', '[1, 2, 3, 5, 8]', 300, 100),
  
  ('Cifrado César', 
   'Crea una función `cifrar(texto, n)` que desplace cada letra `n` posiciones en el alfabeto. Mantener mayúsculas/minúsculas.',
   'medium', '"Hola", 3', '"Krod"', 300, 100),
  
  ('Números Primos', 
   'Crea una función `primos_hasta(n)` que devuelva una lista con todos los números primos menores o iguales a `n`.',
   'easy', 'primos_hasta(20)', '[2, 3, 5, 7, 11, 13, 17, 19]', 240, 80),
  
  ('Aplanar Lista', 
   'Crea una función `aplanar(lista)` que reciba una lista anidada (de cualquier profundidad) y devuelva una lista plana.',
   'hard', '[[1,[2,3]],[4,[5,[6]]]]', '[1, 2, 3, 4, 5, 6]', 360, 120),
  
  ('Validar Paréntesis', 
   'Crea una función `validar(texto)` que determine si los paréntesis `()`, corchetes `[]` y llaves `{}` están correctamente balanceados.',
   'medium', '"({[]})"', 'True', 300, 100)
ON CONFLICT DO NOTHING;


-- ============================================================
-- 8. CODE ROYALE: Tabla de matches para tracking
-- ============================================================

CREATE TABLE IF NOT EXISTS public.code_royale_matches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id UUID REFERENCES public.code_royale_problems(id),
  player1_id UUID NOT NULL REFERENCES public.profiles(id),
  player2_id UUID REFERENCES public.profiles(id),
  winner_id UUID REFERENCES public.profiles(id),
  status TEXT DEFAULT 'waiting' CHECK (status IN ('waiting', 'active', 'finished', 'cancelled')),
  player1_file TEXT,  -- Ruta del archivo .py subido
  player2_file TEXT,
  started_at TIMESTAMPTZ,
  finished_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.code_royale_matches ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads royale matches" ON public.code_royale_matches
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "User creates royale match" ON public.code_royale_matches
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = player1_id);

CREATE POLICY "Players update their match" ON public.code_royale_matches
  FOR UPDATE TO authenticated 
  USING (auth.uid() = player1_id OR auth.uid() = player2_id);


-- ============================================================
-- 9. NUEVO LOGRO: Quiz Master
-- ============================================================
INSERT INTO public.achievements_catalog (id, title, description, icon, xp_reward)
VALUES 
  ('quiz_master', 'Quiz Master', 'Completa 5 quizzes interactivos con 70% o más.', 'quiz_badge', 50),
  ('royale_champion', 'Royale Champion', 'Gana tu primera batalla en Code Royale.', 'royale_badge', 50),
  ('dojo_warrior', 'Dojo Warrior', 'Sube 10 soluciones en competencias/dojos.', 'dojo_badge', 75)
ON CONFLICT (id) DO NOTHING;


-- ============================================================
-- 10. FUNCIÓN: Verificar logros automáticos de quiz
-- ============================================================
CREATE OR REPLACE FUNCTION public.check_quiz_achievements()
RETURNS TRIGGER AS $$
DECLARE
  quiz_count INTEGER;
  v_user_id UUID;
BEGIN
  v_user_id := NEW.user_id;
  
  -- Contar quizzes completados con >= 70%
  SELECT COUNT(*) INTO quiz_count
  FROM public.quiz_completions
  WHERE user_id = v_user_id AND percentage >= 70;
  
  IF quiz_count >= 5 THEN
    PERFORM public.award_xp_and_badge(v_user_id, 0, 'quiz_master');
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_quiz_completion_badge ON public.quiz_completions;
CREATE TRIGGER on_quiz_completion_badge
  AFTER INSERT OR UPDATE ON public.quiz_completions
  FOR EACH ROW EXECUTE FUNCTION public.check_quiz_achievements();


-- ============================================================
-- 11. FUNCIÓN: Verificar logro dojo_warrior (10 submissions)
-- ============================================================
CREATE OR REPLACE FUNCTION public.check_dojo_warrior()
RETURNS TRIGGER AS $$
DECLARE
  sub_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO sub_count
  FROM public.competition_submissions
  WHERE user_id = NEW.user_id;
  
  IF sub_count >= 10 THEN
    PERFORM public.award_xp_and_badge(NEW.user_id, 0, 'dojo_warrior');
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_submission_dojo_warrior ON public.competition_submissions;
CREATE TRIGGER on_submission_dojo_warrior
  AFTER INSERT ON public.competition_submissions
  FOR EACH ROW EXECUTE FUNCTION public.check_dojo_warrior();


-- ============================================================
-- ✅ FIN DEL PARCHE
-- ============================================================
-- Después de ejecutar este archivo:
-- 1. Los triggers de XP funcionarán correctamente
-- 2. Los dojos tendrán puntos exclusivos (dojo_xp)
-- 3. Los quizzes otorgarán XP real
-- 4. Code Royale tendrá un pool de problemas
-- 5. Nuevos logros: quiz_master, royale_champion, dojo_warrior
-- ============================================================
