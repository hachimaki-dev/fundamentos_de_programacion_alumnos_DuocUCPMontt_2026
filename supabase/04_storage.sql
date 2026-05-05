-- ============================================================
-- 📁 04 — STORAGE BUCKET & POLICIES
-- ============================================================
-- Ejecuta esto en el SQL Editor de Supabase para crear el
-- bucket de soluciones y configurar los permisos de acceso.
-- ============================================================

-- 1. Crear el bucket "competition-solutions" (si no existe)
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'competition-solutions', 
  'competition-solutions', 
  false, -- Privado, requiere auth
  51200, -- 50KB en bytes
  ARRAY['text/x-python', 'text/plain', 'application/x-python-code']
)
ON CONFLICT (id) DO UPDATE SET 
  public = false, 
  file_size_limit = 51200, 
  allowed_mime_types = ARRAY['text/x-python', 'text/plain', 'application/x-python-code'];

-- 2. Asegurarse de que RLS está habilitado en storage.objects
ALTER TABLE storage.objects ENABLE ROW LEVEL SECURITY;

-- 3. Política para permitir SUBIR archivos (INSERT) a cualquier usuario autenticado
DROP POLICY IF EXISTS "Permitir subida a usuarios logueados" ON storage.objects;
CREATE POLICY "Permitir subida a usuarios logueados" 
ON storage.objects FOR INSERT TO authenticated 
WITH CHECK (bucket_id = 'competition-solutions');

-- 4. Política para permitir ACTUALIZAR archivos (UPDATE) al re-subir
DROP POLICY IF EXISTS "Permitir actualizar a usuarios logueados" ON storage.objects;
CREATE POLICY "Permitir actualizar a usuarios logueados" 
ON storage.objects FOR UPDATE TO authenticated 
USING (bucket_id = 'competition-solutions');

-- 5. Política para permitir DESCARGAR archivos (SELECT) a cualquier usuario autenticado
DROP POLICY IF EXISTS "Permitir descarga a usuarios logueados" ON storage.objects;
CREATE POLICY "Permitir descarga a usuarios logueados" 
ON storage.objects FOR SELECT TO authenticated 
USING (bucket_id = 'competition-solutions');
