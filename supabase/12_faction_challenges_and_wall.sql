-- ═══════════════════════════════════════════════════════════════
-- ⚔️ FASE 2 & 3: Desafíos Intra-Facción y Mural de Facción
-- ═══════════════════════════════════════════════════════════════

-- ─────────────────────────────────────────────────────────────
-- TABLA 1: Desafíos Intra-Facción (Fase 2)
-- ─────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.faction_challenges (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  faction_id UUID NOT NULL REFERENCES public.factions(id) ON DELETE CASCADE,
  created_by UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT,
  target_xp INTEGER NOT NULL DEFAULT 500,
  deadline TIMESTAMPTZ NOT NULL,
  reward_xp INTEGER NOT NULL DEFAULT 100,
  status TEXT DEFAULT 'active', -- 'active', 'completed', 'failed', 'archived'
  current_xp INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_faction_challenges_faction_id ON public.faction_challenges(faction_id);
CREATE INDEX idx_faction_challenges_status ON public.faction_challenges(status);
CREATE INDEX idx_faction_challenges_deadline ON public.faction_challenges(deadline);

ALTER TABLE public.faction_challenges ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated users can view faction challenges"
  ON public.faction_challenges FOR SELECT TO authenticated
  USING (true);

CREATE POLICY "Authenticated users can create challenges for their faction"
  ON public.faction_challenges FOR INSERT TO authenticated
  WITH CHECK (
    created_by = auth.uid() AND
    EXISTS (
      SELECT 1 FROM public.profiles
      WHERE id = auth.uid() AND faction_id = faction_challenges.faction_id
    )
  );

CREATE POLICY "Challenge creators can update their challenges"
  ON public.faction_challenges FOR UPDATE TO authenticated
  USING (created_by = auth.uid());

-- ─────────────────────────────────────────────────────────────
-- TABLA 2: Mural de Facción (Fase 3)
-- ─────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS public.faction_wall (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  faction_id UUID NOT NULL REFERENCES public.factions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  message TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_faction_wall_faction_id ON public.faction_wall(faction_id);
CREATE INDEX idx_faction_wall_user_id ON public.faction_wall(user_id);
CREATE INDEX idx_faction_wall_created_at ON public.faction_wall(created_at);

ALTER TABLE public.faction_wall ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated users can view faction wall"
  ON public.faction_wall FOR SELECT TO authenticated
  USING (true);

CREATE POLICY "Authenticated users can post to their faction wall"
  ON public.faction_wall FOR INSERT TO authenticated
  WITH CHECK (
    user_id = auth.uid() AND
    EXISTS (
      SELECT 1 FROM public.profiles
      WHERE id = auth.uid() AND faction_id = faction_wall.faction_id
    )
  );

CREATE POLICY "Users can update their own wall posts"
  ON public.faction_wall FOR UPDATE TO authenticated
  USING (user_id = auth.uid());

CREATE POLICY "Users can delete their own wall posts"
  ON public.faction_wall FOR DELETE TO authenticated
  USING (user_id = auth.uid());

-- ─────────────────────────────────────────────────────────────
-- VISTAS HELPER
-- ─────────────────────────────────────────────────────────────

-- Vista: Desafíos activos con progreso
CREATE OR REPLACE VIEW public.faction_challenges_with_progress AS
SELECT 
  fc.id,
  fc.faction_id,
  fc.title,
  fc.description,
  fc.target_xp,
  fc.current_xp,
  fc.reward_xp,
  fc.deadline,
  fc.status,
  ROUND(CAST(fc.current_xp AS NUMERIC) / CAST(fc.target_xp AS NUMERIC) * 100)::INT as progress_percent,
  (fc.deadline > now()) as is_active,
  EXTRACT(HOUR FROM (fc.deadline - now()))::INT as hours_remaining,
  fc.created_at,
  p.nickname as creator_name,
  p.avatar_id as creator_avatar_id,
  f.faction_name
FROM public.faction_challenges fc
JOIN public.profiles p ON fc.created_by = p.id
JOIN public.factions f ON fc.faction_id = f.id
ORDER BY fc.created_at DESC;

-- Vista: Mural con datos de usuarios
CREATE OR REPLACE VIEW public.faction_wall_feed AS
SELECT 
  fw.id,
  fw.faction_id,
  fw.user_id,
  fw.message,
  fw.created_at,
  p.nickname,
  p.avatar_id,
  p.avatar_source,
  p.avatar_custom_url,
  p.level,
  f.faction_name
FROM public.faction_wall fw
JOIN public.profiles p ON fw.user_id = p.id
JOIN public.factions f ON fw.faction_id = f.id
ORDER BY fw.created_at DESC;

-- ─────────────────────────────────────────────────────────────
-- TRIGGERS: Auto-update XP cuando se completa desafío
-- ─────────────────────────────────────────────────────────────

CREATE OR REPLACE FUNCTION update_faction_challenge_xp()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.status = 'completed' AND OLD.status != 'completed' THEN
    -- Dar reward XP a todos los miembros de la facción
    UPDATE public.profiles
    SET xp = xp + NEW.reward_xp
    WHERE faction_id = NEW.faction_id;
    
    -- Actualizar XP total de la facción
    UPDATE public.factions
    SET total_xp = (SELECT COALESCE(SUM(xp), 0) FROM public.profiles WHERE faction_id = NEW.faction_id)
    WHERE id = NEW.faction_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_faction_challenge_xp ON public.faction_challenges;
CREATE TRIGGER trigger_faction_challenge_xp
AFTER UPDATE ON public.faction_challenges
FOR EACH ROW
EXECUTE FUNCTION update_faction_challenge_xp();
