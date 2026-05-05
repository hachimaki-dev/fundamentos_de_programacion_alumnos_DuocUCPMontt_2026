-- ============================================================
-- 🔐 08 — FACCIONES Y MYSPACE (PERFILES PUBLICOS)
-- ============================================================

-- 1. Tabla de Facciones (Secciones)
CREATE TABLE IF NOT EXISTS public.factions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  section_code TEXT UNIQUE NOT NULL, -- Ej: '001D', '005V'
  faction_name TEXT NOT NULL,        -- Ej: 'Los Algoritmos de Fuego'
  leader_id UUID REFERENCES public.profiles(id), -- El profesor o estudiante líder
  total_xp INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Alterar Perfiles para la era "MySpace" y Facciones
ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS custom_html TEXT,
ADD COLUMN IF NOT EXISTS custom_css TEXT,
ADD COLUMN IF NOT EXISTS title TEXT,
ADD COLUMN IF NOT EXISTS faction_id UUID REFERENCES public.factions(id);

-- 3. Políticas de RLS para Facciones
ALTER TABLE public.factions ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Factions are viewable by everyone" ON public.factions;
CREATE POLICY "Factions are viewable by everyone"
  ON public.factions FOR SELECT TO authenticated
  USING (true);

-- 4. Permitir a cualquiera ver el perfil de otros para la vista pública
DROP POLICY IF EXISTS "Profiles are viewable by everyone" ON public.profiles;
CREATE POLICY "Profiles are viewable by everyone"
  ON public.profiles FOR SELECT TO authenticated
  USING (true);

-- 5. Tabla para historial de sincronización con GitHub
CREATE TABLE IF NOT EXISTS public.github_sync_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES public.profiles(id),
  github_event_id TEXT UNIQUE NOT NULL,
  event_type TEXT,
  repo_name TEXT,
  xp_awarded INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.github_sync_history ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view their own github history" ON public.github_sync_history;
CREATE POLICY "Users can view their own github history"
  ON public.github_sync_history FOR SELECT TO authenticated
  USING (auth.uid() = user_id);

-- 6. Trigger o Función para actualizar XP de facción (opcional)
CREATE OR REPLACE FUNCTION update_faction_xp()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.faction_id IS NOT NULL THEN
    UPDATE public.factions
    SET total_xp = (
      SELECT COALESCE(SUM(xp), 0)
      FROM public.profiles
      WHERE faction_id = NEW.faction_id
    )
    WHERE id = NEW.faction_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- 7. Tabla de Seguidores (Follows)
CREATE TABLE IF NOT EXISTS public.follows (
  follower_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
  following_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (follower_id, following_id)
);

ALTER TABLE public.follows ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Everyone can view follows" ON public.follows;
CREATE POLICY "Everyone can view follows"
  ON public.follows FOR SELECT TO authenticated
  USING (true);

DROP POLICY IF EXISTS "Users can insert their own follows" ON public.follows;
CREATE POLICY "Users can insert their own follows"
  ON public.follows FOR INSERT TO authenticated
  WITH CHECK (auth.uid() = follower_id);

DROP POLICY IF EXISTS "Users can delete their own follows" ON public.follows;
CREATE POLICY "Users can delete their own follows"
  ON public.follows FOR DELETE TO authenticated
  USING (auth.uid() = follower_id);

-- (Opcional: puedes adjuntar el trigger a la tabla profiles cuando cambie su XP)
-- Pero como XP está en user_stats, hay que cruzar tablas.
-- Para simplificar, la vista del ranking puede sumar en tiempo real, o adaptamos user_stats.
