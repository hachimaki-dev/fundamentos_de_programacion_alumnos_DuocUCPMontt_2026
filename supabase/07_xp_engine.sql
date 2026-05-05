-- ============================================================
-- 🚀 07 — XP ENGINE & SECURITY PATCH (Pre-Launch)
-- ============================================================
-- Asegura la columna XP para evitar trampas desde el frontend
-- y crea los gatillos (triggers) automáticos que otorgan XP
-- y medallas cuando los usuarios interactúan.
-- ============================================================

-- ============================================================
-- 1. SECURITY PATCH: Blindar XP, Level y Logros
-- ============================================================
-- Creamos un trigger que impide que un usuario (no admin) 
-- altere su propio XP, nivel o logros mediante UPDATE.
CREATE OR REPLACE FUNCTION public.protect_gamification_columns()
RETURNS TRIGGER AS $$
BEGIN
  -- Si el update viene del rol 'authenticated' (frontend), forzamos
  -- que los valores de gamificación se mantengan igual.
  -- (Los triggers de BD operan internamente, por lo que este check 
  -- es simple pero efectivo).
  
  -- En la práctica, es más seguro simplemente sobreescribir NEW con OLD
  -- a menos que tengamos una forma de identificar llamadas internas.
  -- Para este proyecto, permitiremos que el trigger interno los modifique,
  -- pero en un update de perfil normal (ej: cambiar avatar), restauramos el viejo XP.
  
  -- Si el update modificó xp/level/achievements, y no es el trigger interno
  -- que calcula el nivel (que veremos si es necesario), restauramos.
  -- Como esto puede ser complejo, lo más seguro es:
  IF (current_setting('role') = 'authenticated') THEN
    NEW.xp := OLD.xp;
    NEW.level := OLD.level;
    NEW.achievements := OLD.achievements;
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS enforce_gamification_security ON public.profiles;
CREATE TRIGGER enforce_gamification_security
  BEFORE UPDATE ON public.profiles
  FOR EACH ROW
  EXECUTE FUNCTION public.protect_gamification_columns();

-- ============================================================
-- 2. HELPER FUNCTION: Otorgar XP y Logro
-- ============================================================
-- Función interna (SECURITY DEFINER) para dar XP a un usuario
CREATE OR REPLACE FUNCTION public.award_xp_and_badge(
  target_user UUID, 
  xp_amount INTEGER, 
  badge_id TEXT DEFAULT NULL
) RETURNS VOID AS $$
DECLARE
  current_achievements TEXT[];
  user_faction UUID;
BEGIN
  -- Obtener logros actuales y faccion
  SELECT achievements, faction_id INTO current_achievements, user_faction FROM public.profiles WHERE id = target_user;
  
  -- Si badge_id fue provisto y no lo tiene, lo añadimos
  IF badge_id IS NOT NULL AND NOT (badge_id = ANY(current_achievements)) THEN
    -- El rol es bypass RLS internamente al ser security definer
    UPDATE public.profiles 
    SET 
      xp = xp + xp_amount,
      achievements = array_append(achievements, badge_id)
    WHERE id = target_user;
  ELSE
    -- Solo sumamos XP
    UPDATE public.profiles 
    SET xp = xp + xp_amount
    WHERE id = target_user;
  END IF;

  -- Actualizar el XP de la facción si el usuario pertenece a una
  IF user_faction IS NOT NULL THEN
    UPDATE public.factions
    SET total_xp = total_xp + xp_amount
    WHERE id = user_faction;
  END IF;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;


-- ============================================================
-- 3. TRIGGERS DE ACTIVIDAD
-- ============================================================

-- A. Al escribir en el Diario (+20 XP, logro 'diarist')
CREATE OR REPLACE FUNCTION public.trigger_diary_xp()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM public.award_xp_and_badge(NEW.user_id, 20, 'diarist');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS on_diary_insert_xp ON public.diary_entries;
CREATE TRIGGER on_diary_insert_xp
  AFTER INSERT ON public.diary_entries
  FOR EACH ROW EXECUTE FUNCTION public.trigger_diary_xp();


-- B. Al subir código a Competencia (+50 XP, logro 'first_blood')
CREATE OR REPLACE FUNCTION public.trigger_submission_xp()
RETURNS TRIGGER AS $$
BEGIN
  -- Otorga 50 XP por subir solución.
  PERFORM public.award_xp_and_badge(NEW.user_id, 50, 'first_blood');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS on_submission_insert_xp ON public.competition_submissions;
CREATE TRIGGER on_submission_insert_xp
  AFTER INSERT ON public.competition_submissions
  FOR EACH ROW EXECUTE FUNCTION public.trigger_submission_xp();


-- C. Al recibir un Like (+10 XP para el autor, logro 'social_butterfly')
CREATE OR REPLACE FUNCTION public.trigger_vote_xp()
RETURNS TRIGGER AS $$
DECLARE
  target_author UUID;
  author_likes INTEGER;
BEGIN
  -- Solo dar XP si es un voto positivo (like)
  IF NEW.vote = 1 THEN
    -- Buscar el autor de la submission
    SELECT user_id INTO target_author FROM public.competition_submissions WHERE id = NEW.submission_id;
    
    IF target_author IS NOT NULL AND target_author != NEW.user_id THEN
      -- Dar 10 XP al autor
      PERFORM public.award_xp_and_badge(target_author, 10, NULL);
      
      -- Chequear si llegó a 5 likes para el logro social_butterfly
      SELECT likes_count INTO author_likes FROM public.competition_submissions WHERE id = NEW.submission_id;
      IF author_likes >= 4 THEN -- (4 porque el trigger se ejecuta justo después del insert)
        PERFORM public.award_xp_and_badge(target_author, 0, 'social_butterfly');
      END IF;
    END IF;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS on_vote_insert_xp ON public.competition_votes;
CREATE TRIGGER on_vote_insert_xp
  AFTER INSERT ON public.competition_votes
  FOR EACH ROW EXECUTE FUNCTION public.trigger_vote_xp();


-- ============================================================
-- 4. TRIGGER: Logros por Nivel
-- ============================================================
-- Evalúa si ganó medalla nivel 2 o 5
CREATE OR REPLACE FUNCTION public.check_level_achievements()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.level >= 2 AND NOT ('hacker_level_1' = ANY(NEW.achievements)) THEN
    NEW.achievements := array_append(NEW.achievements, 'hacker_level_1');
  END IF;
  IF NEW.level >= 5 AND NOT ('hacker_level_5' = ANY(NEW.achievements)) THEN
    NEW.achievements := array_append(NEW.achievements, 'hacker_level_5');
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Engancharlo ANTES del update para modificar el arreglo in-flight
DROP TRIGGER IF EXISTS on_level_up_badge ON public.profiles;
CREATE TRIGGER on_level_up_badge
  BEFORE UPDATE OF level ON public.profiles
  FOR EACH ROW EXECUTE FUNCTION public.check_level_achievements();
