-- ============================================================
-- 🏆 03 — COMPETITIONS SYSTEM (Codewars/Codeforces style)
-- ============================================================
-- Sistema completo de competencias de código.
-- Cualquier usuario puede crear competencias.
-- Soluciones bloqueadas hasta el deadline.
-- Votación pública (no anónima).
-- ============================================================

-- ── 1. Competencias ──
DROP TABLE IF EXISTS public.competition_votes CASCADE;
DROP TABLE IF EXISTS public.competition_submissions CASCADE;
DROP TABLE IF EXISTS public.competition_participants CASCADE;
DROP TABLE IF EXISTS public.competition_problems CASCADE;
DROP TABLE IF EXISTS public.competition_entries CASCADE;  -- tabla vieja
DROP TABLE IF EXISTS public.competitions CASCADE;

CREATE TABLE public.competitions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  description TEXT,
  rules TEXT,                                -- Markdown con reglas
  status TEXT DEFAULT 'active'
    CHECK (status IN ('active', 'finished', 'cancelled')),
  deadline TIMESTAMPTZ,                      -- Fecha límite de envío
  invite_code TEXT UNIQUE DEFAULT substr(md5(random()::text), 1, 8),
  created_by UUID NOT NULL REFERENCES public.profiles(id),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ── 2. Problemas por competencia ──
CREATE TABLE public.competition_problems (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT NOT NULL,                 -- Markdown: enunciado completo
  difficulty TEXT DEFAULT 'medium'
    CHECK (difficulty IN ('easy', 'medium', 'hard')),
  example_input TEXT,                        -- Ejemplo de entrada
  example_output TEXT,                       -- Ejemplo de salida esperada
  sort_order INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ── 3. Participantes ──
CREATE TABLE public.competition_participants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  joined_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(competition_id, user_id)
);

-- ── 4. Soluciones (.py subidos) ──
CREATE TABLE public.competition_submissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  problem_id UUID NOT NULL REFERENCES public.competition_problems(id) ON DELETE CASCADE,
  competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  file_path TEXT NOT NULL,                   -- Ruta en Supabase Storage
  file_name TEXT NOT NULL,                   -- Nombre original del archivo
  attempt_count INTEGER DEFAULT 1,           -- Conteo de intentos/resubmits
  submitted_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  likes_count INTEGER DEFAULT 0,
  dislikes_count INTEGER DEFAULT 0,
  UNIQUE(problem_id, user_id)                -- 1 solución activa por problema
);

-- ── 5. Votos (NO anónimos) ──
CREATE TABLE public.competition_votes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  submission_id UUID NOT NULL REFERENCES public.competition_submissions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  vote INTEGER NOT NULL CHECK (vote IN (1, -1)),  -- 1=like, -1=dislike
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(submission_id, user_id)             -- 1 voto por usuario por solución
);

-- ── 6. Trigger: auto-actualizar conteo de likes/dislikes ──
CREATE OR REPLACE FUNCTION update_vote_counts()
RETURNS TRIGGER AS $$
DECLARE
  target_id UUID;
BEGIN
  target_id := COALESCE(NEW.submission_id, OLD.submission_id);
  UPDATE public.competition_submissions SET
    likes_count = (
      SELECT COUNT(*) FROM public.competition_votes
      WHERE submission_id = target_id AND vote = 1
    ),
    dislikes_count = (
      SELECT COUNT(*) FROM public.competition_votes
      WHERE submission_id = target_id AND vote = -1
    )
  WHERE id = target_id;
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_vote_change ON public.competition_votes;
CREATE TRIGGER on_vote_change
  AFTER INSERT OR UPDATE OR DELETE ON public.competition_votes
  FOR EACH ROW EXECUTE FUNCTION update_vote_counts();

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================

-- Competitions: todos leen, creador gestiona
ALTER TABLE public.competitions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone reads comps" ON public.competitions
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "Users create comps" ON public.competitions
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = created_by);
CREATE POLICY "Creator updates comp" ON public.competitions
  FOR UPDATE TO authenticated USING (auth.uid() = created_by);

-- Problems: todos leen, creador de comp gestiona
ALTER TABLE public.competition_problems ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone reads problems" ON public.competition_problems
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "Creator manages problems" ON public.competition_problems
  FOR INSERT TO authenticated
  WITH CHECK (EXISTS (
    SELECT 1 FROM public.competitions
    WHERE id = competition_id AND created_by = auth.uid()
  ));
CREATE POLICY "Creator updates problems" ON public.competition_problems
  FOR UPDATE TO authenticated
  USING (EXISTS (
    SELECT 1 FROM public.competitions
    WHERE id = competition_id AND created_by = auth.uid()
  ));
CREATE POLICY "Creator deletes problems" ON public.competition_problems
  FOR DELETE TO authenticated
  USING (EXISTS (
    SELECT 1 FROM public.competitions
    WHERE id = competition_id AND created_by = auth.uid()
  ));

-- Participants: todos leen, usuario se une solo
ALTER TABLE public.competition_participants ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone reads participants" ON public.competition_participants
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User joins" ON public.competition_participants
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User leaves" ON public.competition_participants
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- Submissions: todos leen, usuario gestiona las suyas
ALTER TABLE public.competition_submissions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone reads submissions" ON public.competition_submissions
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User creates submission" ON public.competition_submissions
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User updates own sub" ON public.competition_submissions
  FOR UPDATE TO authenticated USING (auth.uid() = user_id);

-- Votes: todos leen (NO anónimo), usuario gestiona su voto
ALTER TABLE public.competition_votes ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Anyone reads votes" ON public.competition_votes
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User casts vote" ON public.competition_votes
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User changes vote" ON public.competition_votes
  FOR UPDATE TO authenticated USING (auth.uid() = user_id);
CREATE POLICY "User removes vote" ON public.competition_votes
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- ============================================================
-- STORAGE: Bucket para soluciones .py
-- ============================================================
-- IMPORTANTE: Crear manualmente en Supabase Dashboard:
-- Storage → New Bucket → "competition-solutions"
-- Access: Private (solo autenticados)
-- File size limit: 50KB
-- Allowed MIME types: text/x-python, text/plain
-- ============================================================
