-- ============================================================
-- 📸 02 — PROFILES ENHANCEMENT (Personalización Completa)
-- ============================================================
-- Ejecutar SEGUNDO. Agrega campos para foto custom, bio, 
-- social links y configuraciones de visibilidad.
-- ============================================================

-- 1. Agregar columnas nuevas a profiles
ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS avatar_custom_url TEXT,
ADD COLUMN IF NOT EXISTS avatar_source TEXT DEFAULT 'catalog' CHECK (avatar_source IN ('catalog', 'custom')),
ADD COLUMN IF NOT EXISTS bio TEXT,
ADD COLUMN IF NOT EXISTS social_links JSONB DEFAULT '{}' :: JSONB,
ADD COLUMN IF NOT EXISTS visibility TEXT DEFAULT 'public' CHECK (visibility IN ('public', 'private', 'followers_only')),
ADD COLUMN IF NOT EXISTS myspace_theme TEXT DEFAULT 'default',
ADD COLUMN IF NOT EXISTS profile_completed BOOLEAN DEFAULT false;

-- Agregar index para búsquedas de nickname (ya debería existir, pero asegurar)
CREATE INDEX IF NOT EXISTS idx_profiles_nickname ON public.profiles(nickname);
CREATE INDEX IF NOT EXISTS idx_profiles_visibility ON public.profiles(visibility);

-- Comentarios de documentación
COMMENT ON COLUMN public.profiles.avatar_custom_url IS 'URL de Storage para foto custom subida por usuario';
COMMENT ON COLUMN public.profiles.avatar_source IS 'Origen del avatar: catalog (predefinido) o custom (subido)';
COMMENT ON COLUMN public.profiles.bio IS 'Biografía corta del usuario (~160 caracteres)';
COMMENT ON COLUMN public.profiles.social_links IS 'JSON con links sociales: {github, twitter, youtube, portfolio, etc}';
COMMENT ON COLUMN public.profiles.visibility IS 'Control de privacidad del perfil';
COMMENT ON COLUMN public.profiles.myspace_theme IS 'Tema seleccionado para MySpace (extensible para futuras plantillas)';
COMMENT ON COLUMN public.profiles.profile_completed IS 'Flag para saber si el usuario completó setup';

-- 2. Update RLS policies para nuevas columnas

-- Política para SELECT (usuarios pueden ver perfiles públicos, su propio, o si siguen)
DROP POLICY IF EXISTS "Users read own profile" ON public.profiles;
CREATE POLICY "Users read own profile"
  ON public.profiles FOR SELECT TO authenticated
  USING (
    auth.uid() = id
    OR visibility = 'public'
  );

-- Política abierta para perfiles públicos (anónimo puede ver)
DROP POLICY IF EXISTS "Public profiles visible to all" ON public.profiles;
CREATE POLICY "Public profiles visible to all"
  ON public.profiles FOR SELECT TO anon
  USING (visibility = 'public');

-- UPDATE: solo usuario puede editar su propio perfil
DROP POLICY IF EXISTS "Users update own profile" ON public.profiles;
CREATE POLICY "Users update own profile"
  ON public.profiles FOR UPDATE TO authenticated
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- ============================================================
-- Extra: Crear tabla de audit_changes (opcional, para logs)
-- ============================================================
/*
CREATE TABLE IF NOT EXISTS public.profile_changes_audit (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  changed_by UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  changed_fields TEXT[],
  old_values JSONB,
  new_values JSONB,
  changed_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.profile_changes_audit ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users read own audit"
  ON public.profile_changes_audit FOR SELECT TO authenticated
  USING (changed_by = auth.uid());
*/

-- ============================================================
-- Trigger para actualizar updated_at automáticamente
-- ============================================================
CREATE OR REPLACE FUNCTION public.update_profiles_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS update_profiles_updated_at_trigger ON public.profiles;
CREATE TRIGGER update_profiles_updated_at_trigger
  BEFORE UPDATE ON public.profiles
  FOR EACH ROW
  EXECUTE FUNCTION public.update_profiles_updated_at();

COMMIT;
