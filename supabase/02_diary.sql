-- ============================================================
-- 📖 02 — DIARY ENTRIES
-- ============================================================
-- Diario de clase personal de cada estudiante.
-- ============================================================

CREATE TABLE IF NOT EXISTS public.diary_entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  tags TEXT[] DEFAULT '{}',
  links TEXT[] DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.diary_entries ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users CRUD own diary" ON public.diary_entries;
CREATE POLICY "Users CRUD own diary"
  ON public.diary_entries FOR ALL TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Profesor puede leer todos los diarios
DROP POLICY IF EXISTS "Teacher reads all diaries" ON public.diary_entries;
CREATE POLICY "Teacher reads all diaries"
  ON public.diary_entries FOR SELECT TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM public.profiles
      WHERE id = auth.uid() AND role = 'teacher'
    )
  );
