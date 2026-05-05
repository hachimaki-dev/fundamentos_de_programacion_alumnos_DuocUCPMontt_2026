-- ============================================================
-- 💬 09 — MURO SOCIAL DE COMPETENCIAS (Dojo Wall)
-- ============================================================
-- Permite a los participantes publicar mensajes en el muro
-- de cada competencia. Incluye likes y otorga XP.
-- ============================================================

-- ── 1. Posts del Muro ──
CREATE TABLE IF NOT EXISTS public.competition_wall_posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  content TEXT NOT NULL CHECK (char_length(content) <= 500),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ── 2. Likes en Posts del Muro ──
CREATE TABLE IF NOT EXISTS public.competition_wall_likes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  post_id UUID NOT NULL REFERENCES public.competition_wall_posts(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(post_id, user_id)  -- 1 like por usuario por post
);

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================

-- Wall Posts: autenticados leen todo, crean las suyas, borran las suyas
ALTER TABLE public.competition_wall_posts ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads wall posts" ON public.competition_wall_posts
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "User creates wall post" ON public.competition_wall_posts
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);

CREATE POLICY "User deletes own wall post" ON public.competition_wall_posts
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- Wall Likes: autenticados leen todo, gestionan las suyas
ALTER TABLE public.competition_wall_likes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone reads wall likes" ON public.competition_wall_likes
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "User creates wall like" ON public.competition_wall_likes
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);

CREATE POLICY "User removes own wall like" ON public.competition_wall_likes
  FOR DELETE TO authenticated USING (auth.uid() = user_id);

-- ============================================================
-- XP TRIGGER: +5 XP por publicar en el muro (fomentar social)
-- ============================================================
CREATE OR REPLACE FUNCTION public.trigger_wall_post_xp()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM public.award_xp_and_badge(NEW.user_id, 5, NULL);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_wall_post_insert_xp ON public.competition_wall_posts;
CREATE TRIGGER on_wall_post_insert_xp
  AFTER INSERT ON public.competition_wall_posts
  FOR EACH ROW EXECUTE FUNCTION public.trigger_wall_post_xp();
