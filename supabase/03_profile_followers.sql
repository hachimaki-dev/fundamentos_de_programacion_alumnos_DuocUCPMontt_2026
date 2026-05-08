-- ============================================================
-- 👥 03 — PROFILE FOLLOWERS (Sistema de Seguimiento)
-- ============================================================
-- Ejecutar TERCERO. Crea tabla de followers con RLS y triggers.
-- ============================================================

-- 1. Crear tabla de followers (relación M-to-M)
CREATE TABLE IF NOT EXISTS public.profile_followers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  follower_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  following_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  
  -- Asegurar que no se pueda seguir a uno mismo
  CONSTRAINT no_self_follow CHECK (follower_id != following_id),
  
  -- Asegurar That no hay duplicados
  UNIQUE(follower_id, following_id)
);

-- 2. Crear índices para queries rápidas
CREATE INDEX IF NOT EXISTS idx_followers_follower_id ON public.profile_followers(follower_id);
CREATE INDEX IF NOT EXISTS idx_followers_following_id ON public.profile_followers(following_id);
CREATE INDEX IF NOT EXISTS idx_followers_created_at ON public.profile_followers(created_at);

-- 3. Habilitar RLS
ALTER TABLE public.profile_followers ENABLE ROW LEVEL SECURITY;

-- 4. RLS Policies

-- SELECT: Todos pueden ver followers (stats públicas)
DROP POLICY IF EXISTS "Anyone can view followers" ON public.profile_followers;
CREATE POLICY "Anyone can view followers"
  ON public.profile_followers FOR SELECT
  USING (true);

-- INSERT: Usuarios autenticados pueden seguir
DROP POLICY IF EXISTS "Users can follow others" ON public.profile_followers;
CREATE POLICY "Users can follow others"
  ON public.profile_followers FOR INSERT TO authenticated
  WITH CHECK (auth.uid() = follower_id);

-- UPDATE: No se permite actualizar (relaciones exist/no exist)
-- (Si quieres permitir UPDATE, descomentar)
DROP POLICY IF EXISTS "No updates on followers" ON public.profile_followers;
CREATE POLICY "No updates on followers"
  ON public.profile_followers FOR UPDATE
  USING (false);

-- DELETE: Solo el follower puede dejar de seguir
DROP POLICY IF EXISTS "Users can unfollow" ON public.profile_followers;
CREATE POLICY "Users can unfollow"
  ON public.profile_followers FOR DELETE TO authenticated
  USING (auth.uid() = follower_id);

-- ============================================================
-- 5. Views helpers (queries útiles)
-- ============================================================

-- Vista: Conteo de followers por usuario
CREATE OR REPLACE VIEW public.v_follower_counts AS
  SELECT 
    profiles.id,
    profiles.nickname,
    COUNT(pf_followers.id) as follower_count,
    COUNT(pf_following.id) as following_count
  FROM public.profiles
  LEFT JOIN public.profile_followers pf_followers ON pf_followers.following_id = profiles.id
  LEFT JOIN public.profile_followers pf_following ON pf_following.follower_id = profiles.id
  GROUP BY profiles.id, profiles.nickname;

-- Vista: Top usuarios más seguidos
CREATE OR REPLACE VIEW public.v_top_followed AS
  SELECT 
    p.id,
    p.nickname,
    p.avatar_id,
    COUNT(pf.id) as follower_count
  FROM public.profiles p
  LEFT JOIN public.profile_followers pf ON pf.following_id = p.id
  WHERE p.visibility = 'public'
  GROUP BY p.id, p.nickname, p.avatar_id
  ORDER BY follower_count DESC
  LIMIT 50;

-- ============================================================
-- 6. Función helper: Check if user follows another
-- ============================================================
CREATE OR REPLACE FUNCTION public.is_following(
  p_follower_id UUID,
  p_following_id UUID
)
RETURNS BOOLEAN AS $$
  SELECT EXISTS(
    SELECT 1 FROM public.profile_followers
    WHERE follower_id = p_follower_id AND following_id = p_following_id
  );
$$ LANGUAGE sql STABLE;

-- ============================================================
-- 7. Función helper: Get follower count
-- ============================================================
CREATE OR REPLACE FUNCTION public.get_follower_count(p_profile_id UUID)
RETURNS BIGINT AS $$
  SELECT COUNT(*) FROM public.profile_followers
  WHERE following_id = p_profile_id;
$$ LANGUAGE sql STABLE;

-- ============================================================
-- 8. Función helper: Get following count
-- ============================================================
CREATE OR REPLACE FUNCTION public.get_following_count(p_profile_id UUID)
RETURNS BIGINT AS $$
  SELECT COUNT(*) FROM public.profile_followers
  WHERE follower_id = p_profile_id;
$$ LANGUAGE sql STABLE;

COMMIT;
