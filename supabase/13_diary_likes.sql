-- ============================================================
-- 13 — DIARY LIKES SYSTEM (Fix & Implementation)
-- ============================================================
-- Añade sistema de likes para diary_entries.
-- Rastrena qué usuario le dio like a cuál entrada.
-- Mantiene likes_count sincronizado automáticamente.
-- ============================================================

-- 1. Crear tabla diary_likes
CREATE TABLE IF NOT EXISTS public.diary_likes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  entry_id UUID NOT NULL REFERENCES public.diary_entries(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(user_id, entry_id)  -- Solo un like por usuario por entrada
);

ALTER TABLE public.diary_likes ENABLE ROW LEVEL SECURITY;

-- 2. RLS Policies para diary_likes
DROP POLICY IF EXISTS "Anyone reads diary likes" ON public.diary_likes;
CREATE POLICY "Anyone reads diary likes"
  ON public.diary_likes FOR SELECT TO authenticated
  USING (true);

DROP POLICY IF EXISTS "User creates own diary like" ON public.diary_likes;
CREATE POLICY "User creates own diary like"
  ON public.diary_likes FOR INSERT TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "User deletes own diary like" ON public.diary_likes;
CREATE POLICY "User deletes own diary like"
  ON public.diary_likes FOR DELETE TO authenticated
  USING (auth.uid() = user_id);

-- 3. Índices para performance
CREATE INDEX IF NOT EXISTS idx_diary_likes_user_id ON public.diary_likes(user_id);
CREATE INDEX IF NOT EXISTS idx_diary_likes_entry_id ON public.diary_likes(entry_id);

-- 4. Function para actualizar likes_count
CREATE OR REPLACE FUNCTION update_diary_likes_count()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    UPDATE public.diary_entries 
    SET likes_count = likes_count + 1 
    WHERE id = NEW.entry_id;
    RETURN NEW;
  ELSIF TG_OP = 'DELETE' THEN
    UPDATE public.diary_entries 
    SET likes_count = GREATEST(0, likes_count - 1) 
    WHERE id = OLD.entry_id;
    RETURN OLD;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- 5. Trigger para sincronizar likes_count
DROP TRIGGER IF EXISTS trg_diary_likes_count_update ON public.diary_likes;
CREATE TRIGGER trg_diary_likes_count_update
AFTER INSERT OR DELETE ON public.diary_likes
FOR EACH ROW EXECUTE FUNCTION update_diary_likes_count();

-- 6. Reset actual likes_count from table count (data consistency)
UPDATE public.diary_entries
SET likes_count = (SELECT COUNT(*) FROM public.diary_likes WHERE entry_id = diary_entries.id);
