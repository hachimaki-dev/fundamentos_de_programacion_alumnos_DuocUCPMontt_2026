-- ============================================================
-- 💬 06 — SOCIAL LEARNING (Fase 3)
-- ============================================================
-- Añade diarios públicos, comentarios de diarios y 
-- comentarios en código de competencias (Code Review).
-- ============================================================

-- 1. Actualizar Diarios
ALTER TABLE public.diary_entries
ADD COLUMN IF NOT EXISTS is_public BOOLEAN DEFAULT false,
ADD COLUMN IF NOT EXISTS likes_count INTEGER DEFAULT 0;

-- Permitir lectura de diarios públicos
DROP POLICY IF EXISTS "Anyone reads public diaries" ON public.diary_entries;
CREATE POLICY "Anyone reads public diaries"
  ON public.diary_entries FOR SELECT TO authenticated
  USING (is_public = true OR auth.uid() = user_id);

-- 2. Comentarios en Diarios Públicos
CREATE TABLE IF NOT EXISTS public.diary_comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  entry_id UUID NOT NULL REFERENCES public.diary_entries(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.diary_comments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads diary comments" ON public.diary_comments
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User creates diary comment" ON public.diary_comments
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User updates own diary comment" ON public.diary_comments
  FOR UPDATE TO authenticated USING (auth.uid() = user_id);
CREATE POLICY "User deletes own diary comment" ON public.diary_comments
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- 3. Code Reviews (Comentarios en Soluciones de Competencias)
CREATE TABLE IF NOT EXISTS public.submission_comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  submission_id UUID NOT NULL REFERENCES public.competition_submissions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  line_number INTEGER, -- Opcional, para comentar en una línea específica
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.submission_comments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads submission comments" ON public.submission_comments
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User creates submission comment" ON public.submission_comments
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User updates own submission comment" ON public.submission_comments
  FOR UPDATE TO authenticated USING (auth.uid() = user_id);
CREATE POLICY "User deletes own submission comment" ON public.submission_comments
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- ============================================================
-- Opcional: Tabla de Feed (Activity Feed)
-- Alternativamente, el feed puede ser una consulta UNION ALL
-- entre diary_entries públicas, submission_comments, etc.
-- ============================================================
