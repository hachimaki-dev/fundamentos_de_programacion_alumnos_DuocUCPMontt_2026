-- ============================================================
-- 15 — POST EDIT & DELETE + AUDIT TRAIL
-- ============================================================
-- Permite editar/eliminar posts propios y rastrea cambios.
-- ============================================================

-- 1. Agregar campos de auditoría a diary_entries
ALTER TABLE public.diary_entries
ADD COLUMN IF NOT EXISTS edited_at TIMESTAMPTZ,
ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ,
ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN DEFAULT false,
ADD COLUMN IF NOT EXISTS original_content TEXT;

-- 2. Actualizar policy de SELECT para posts borrados
DROP POLICY IF EXISTS "Anyone reads public diaries" ON public.diary_entries;
CREATE POLICY "Anyone reads public diaries"
  ON public.diary_entries FOR SELECT TO authenticated
  USING (
    (is_public = true AND is_deleted = false) 
    OR (auth.uid() = user_id)
  );

-- 3. Policy para UPDATE (solo dueño)
DROP POLICY IF EXISTS "User updates own diary" ON public.diary_entries;
CREATE POLICY "User updates own diary"
  ON public.diary_entries FOR UPDATE TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- 4. Policy para DELETE lógico (soft delete)
DROP POLICY IF EXISTS "User deletes own diary" ON public.diary_entries;
CREATE POLICY "User deletes own diary"
  ON public.diary_entries FOR DELETE TO authenticated
  USING (auth.uid() = user_id);

-- 5. Trigger para registrar cuando se edita un post
CREATE OR REPLACE FUNCTION register_diary_edit()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.content != OLD.content THEN
    NEW.original_content = OLD.content;
    NEW.edited_at = now();
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_diary_edit_audit ON public.diary_entries;
CREATE TRIGGER trg_diary_edit_audit
BEFORE UPDATE ON public.diary_entries
FOR EACH ROW EXECUTE FUNCTION register_diary_edit();

-- 6. Trigger para soft delete (mantener registros históricos)
CREATE OR REPLACE FUNCTION soft_delete_diary()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.is_deleted = true AND OLD.is_deleted = false THEN
    NEW.deleted_at = now();
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_diary_soft_delete ON public.diary_entries;
CREATE TRIGGER trg_diary_soft_delete
BEFORE UPDATE ON public.diary_entries
FOR EACH ROW EXECUTE FUNCTION soft_delete_diary();

-- 7. También aplicar al soft delete para comentarios
ALTER TABLE public.diary_comments
ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN DEFAULT false,
ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ;

CREATE OR REPLACE FUNCTION soft_delete_comment()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.is_deleted = true AND OLD.is_deleted = false THEN
    NEW.deleted_at = now();
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_comment_soft_delete ON public.diary_comments;
CREATE TRIGGER trg_comment_soft_delete
BEFORE UPDATE ON public.diary_comments
FOR EACH ROW EXECUTE FUNCTION soft_delete_comment();

-- 8. Actualizar policy de comentarios para excluir borrados
DROP POLICY IF EXISTS "Anyone reads diary comments" ON public.diary_comments;
CREATE POLICY "Anyone reads diary comments"
  ON public.diary_comments FOR SELECT TO authenticated
  USING (is_deleted = false OR auth.uid() = user_id);
