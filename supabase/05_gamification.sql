-- ============================================================
-- 🎮 05 — GAMIFICATION MIGRATION
-- ============================================================
-- Ejecutar en SQL Editor de Supabase para añadir soporte de XP, 
-- Niveles y Logros a los perfiles existentes.
-- ============================================================

ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS xp INTEGER DEFAULT 0,
ADD COLUMN IF NOT EXISTS level INTEGER DEFAULT 1,
ADD COLUMN IF NOT EXISTS achievements TEXT[] DEFAULT '{}';

-- Trigger para auto-calcular el nivel basado en XP
-- Fórmula simple: nivel = 1 + floor(sqrt(xp / 100))
-- Ej: 0-99 XP = Lvl 1. 100-399 XP = Lvl 2. 400-899 XP = Lvl 3.
CREATE OR REPLACE FUNCTION public.update_user_level()
RETURNS TRIGGER AS $$
BEGIN
  NEW.level := 1 + floor(sqrt(NEW.xp / 100.0));
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS on_xp_change ON public.profiles;
CREATE TRIGGER on_xp_change
  BEFORE UPDATE OF xp ON public.profiles
  FOR EACH ROW
  WHEN (OLD.xp IS DISTINCT FROM NEW.xp)
  EXECUTE FUNCTION public.update_user_level();

-- ============================================================
-- 🏆 TABLA DE LOGROS (ACHIEVEMENTS DICTIONARY)
-- ============================================================
-- Catálogo de logros que se pueden obtener.

CREATE TABLE IF NOT EXISTS public.achievements_catalog (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  icon TEXT NOT NULL,
  xp_reward INTEGER DEFAULT 0
);

-- Insertar logros iniciales
INSERT INTO public.achievements_catalog (id, title, description, icon, xp_reward)
VALUES 
  ('first_blood', 'First Blood', 'Completa tu primer problema en una competencia.', 'first_blood_badge', 50),
  ('diarist', 'Querido Diario', 'Escribe tu primera entrada en el diario de clases.', 'diarist_badge', 20),
  ('social_butterfly', 'Social Butterfly', 'Recibe 5 likes en tus soluciones de código.', 'social_badge', 30),
  ('hacker_level_1', 'Script Kiddie', 'Alcanza el Nivel 2.', 'level2_badge', 10),
  ('hacker_level_5', 'Code Ninja', 'Alcanza el Nivel 5.', 'level5_badge', 100)
ON CONFLICT (id) DO NOTHING;
