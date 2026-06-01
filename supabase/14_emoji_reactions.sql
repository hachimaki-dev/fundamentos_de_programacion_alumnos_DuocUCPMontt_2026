-- ============================================================
-- 14 — EMOJI REACTIONS SYSTEM 
-- ============================================================
-- Reemplaza el sistema simple de likes con reacciones emoji.
-- Permite múltiples reacciones por usuario por entrada.
-- ============================================================

-- 1. Crear tabla de reacciones emoji
CREATE TABLE IF NOT EXISTS public.diary_reactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  entry_id UUID NOT NULL REFERENCES public.diary_entries(id) ON DELETE CASCADE,
  reaction VARCHAR(10) NOT NULL DEFAULT '❤️', -- emoji reaction
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(user_id, entry_id, reaction)  -- Un usuario, una reaction por tipo por entrada
);

ALTER TABLE public.diary_reactions ENABLE ROW LEVEL SECURITY;

-- RLS Policies
DROP POLICY IF EXISTS "Anyone reads diary reactions" ON public.diary_reactions;
CREATE POLICY "Anyone reads diary reactions"
  ON public.diary_reactions FOR SELECT TO authenticated
  USING (true);

DROP POLICY IF EXISTS "User creates own diary reaction" ON public.diary_reactions;
CREATE POLICY "User creates own diary reaction"
  ON public.diary_reactions FOR INSERT TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "User deletes own diary reaction" ON public.diary_reactions;
CREATE POLICY "User deletes own diary reaction"
  ON public.diary_reactions FOR DELETE TO authenticated
  USING (auth.uid() = user_id);

-- Índices
CREATE INDEX IF NOT EXISTS idx_diary_reactions_user_id ON public.diary_reactions(user_id);
CREATE INDEX IF NOT EXISTS idx_diary_reactions_entry_id ON public.diary_reactions(entry_id);
CREATE INDEX IF NOT EXISTS idx_diary_reactions_type ON public.diary_reactions(reaction);

-- 2. Actualizar tabla diary_entries para contador por tipo
ALTER TABLE public.diary_entries
DROP COLUMN IF EXISTS likes_count;

ALTER TABLE public.diary_entries
ADD COLUMN IF NOT EXISTS reactions_data JSONB DEFAULT '{}'::jsonb;

-- 3. Function para actualizar reactions_data
CREATE OR REPLACE FUNCTION update_diary_reactions_count()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    UPDATE public.diary_entries 
    SET reactions_data = COALESCE(reactions_data, '{}'::jsonb) || 
        jsonb_build_object(
          NEW.reaction, 
          COALESCE((reactions_data->NEW.reaction)::int, 0) + 1
        )
    WHERE id = NEW.entry_id;
    RETURN NEW;
  ELSIF TG_OP = 'DELETE' THEN
    UPDATE public.diary_entries 
    SET reactions_data = 
        CASE 
          WHEN (reactions_data->OLD.reaction)::int > 1 THEN
            reactions_data || jsonb_build_object(OLD.reaction, (reactions_data->OLD.reaction)::int - 1)
          ELSE
            reactions_data - OLD.reaction
        END
    WHERE id = OLD.entry_id;
    RETURN OLD;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_diary_reactions_count_update ON public.diary_reactions;
CREATE TRIGGER trg_diary_reactions_count_update
AFTER INSERT OR DELETE ON public.diary_reactions
FOR EACH ROW EXECUTE FUNCTION update_diary_reactions_count();

-- 4. Data migration: convertir likes_count a reactions_data
UPDATE public.diary_entries
SET reactions_data = 
  CASE 
    WHEN likes_count > 0 THEN jsonb_build_object('❤️', likes_count)
    ELSE '{}'::jsonb
  END;

-- 5. Function helper: obtener total de reacciones por entrada
CREATE OR REPLACE FUNCTION get_reactions_count(entry_id UUID)
RETURNS INTEGER AS $$
SELECT COALESCE(SUM((value)::int), 0)
FROM public.diary_entries, jsonb_each(reactions_data)
WHERE diary_entries.id = $1;
$$ LANGUAGE SQL;
