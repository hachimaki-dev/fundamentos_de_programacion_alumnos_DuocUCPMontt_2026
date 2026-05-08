-- ============================================================
-- 📁 04 — PROFILE STORAGE (Bucket para Avatares Custom)
-- ============================================================
-- Ejecutar CUARTO. Crea el bucket de Storage y políticas RLS.
-- ============================================================

-- 1. Crear el bucket "profile-avatars" si no existe
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'profile-avatars', 
  'profile-avatars', 
  true, -- Público, permite acceso directo a avatares de perfil
  5242880, -- 5MB en bytes
  ARRAY['image/jpeg', 'image/png', 'image/webp', 'image/gif']
)
ON CONFLICT (id) DO UPDATE SET 
  public = true, 
  file_size_limit = 5242880, 
  allowed_mime_types = ARRAY['image/jpeg', 'image/png', 'image/webp', 'image/gif'];

-- 2. Nota: En Supabase, el esquema de Storage a veces no es propiedad del role SQL
--    que usa el editor, por lo que ALTER TABLE storage.objects puede fallar.
--    Si tu SQL falla aquí, omite esta línea y crea la política desde el panel de Storage.
-- ALTER TABLE storage.objects ENABLE ROW LEVEL SECURITY;

-- 3. Política: Permitir SUBIR (INSERT) a usuarios autenticados
DROP POLICY IF EXISTS "Allow authenticated to upload avatars" ON storage.objects;
CREATE POLICY "Allow authenticated to upload avatars" 
  ON storage.objects FOR INSERT TO authenticated 
  WITH CHECK (
    bucket_id = 'profile-avatars' 
    AND name LIKE auth.uid() || '/%'
  );

-- 4. Política: Permitir ACTUALIZAR (UPDATE) para reemplazar avatares
DROP POLICY IF EXISTS "Allow user to update own avatar" ON storage.objects;
CREATE POLICY "Allow user to update own avatar" 
  ON storage.objects FOR UPDATE TO authenticated 
  USING (
    bucket_id = 'profile-avatars' 
    AND name LIKE auth.uid() || '/%'
  );

-- 5. Política: Permitir DESCARGAR (SELECT) a usuarios autenticados
DROP POLICY IF EXISTS "Allow authenticated to read avatars" ON storage.objects;
CREATE POLICY "Allow authenticated to read avatars" 
  ON storage.objects FOR SELECT TO authenticated 
  USING (bucket_id = 'profile-avatars');

-- 6. Política: Permitir ELIMINAR AVATARES solo al propietario
DROP POLICY IF EXISTS "Allow delete own avatar" ON storage.objects;
CREATE POLICY "Allow delete own avatar" 
  ON storage.objects FOR DELETE TO authenticated 
  USING (
    bucket_id = 'profile-avatars' 
    AND name LIKE auth.uid() || '/%'
  );

-- ============================================================
-- Alternativa: Si quieres que avatares sean públicos (recomendado):
-- ============================================================
-- Crear bucket PUBLIC para avatares
/*
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'profile-avatars-public', 
  'profile-avatars-public', 
  true, -- Público, acceso directo sin auth
  5242880, 
  ARRAY['image/jpeg', 'image/png', 'image/webp', 'image/gif']
)
ON CONFLICT (id) DO UPDATE SET 
  public = true, 
  file_size_limit = 5242880;

-- RLS para bucket público (más permisivo)
DROP POLICY IF EXISTS "Public avatars upload" ON storage.objects;
CREATE POLICY "Public avatars upload" 
  ON storage.objects FOR INSERT TO authenticated 
  WITH CHECK (bucket_id = 'profile-avatars-public' AND auth.uid()::text = (storage.foldername(name))[1]);

DROP POLICY IF EXISTS "Public avatars delete" ON storage.objects;
CREATE POLICY "Public avatars delete" 
  ON storage.objects FOR DELETE TO authenticated 
  USING (bucket_id = 'profile-avatars-public' AND auth.uid()::text = (storage.foldername(name))[1]);
*/

-- ============================================================
-- Notas sobre la estructura de URLs:
-- ============================================================
-- Cuando subas una imagen a /profile-avatars/{user-id}/avatar.jpg
-- La URL sería:
-- https://fokqmosaomsdytsghnsc.supabase.co/storage/v1/object/public/profile-avatars/{user-id}/avatar.jpg
-- O usar signed URL con expiry para mayor seguridad

COMMIT;
