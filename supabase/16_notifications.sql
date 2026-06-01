-- ============================================================
-- 16 — EVENT-DRIVEN NOTIFICATIONS SYSTEM
-- ============================================================
-- Notificaciones automáticas basadas en eventos:
-- - Cuando alguien da like/reacciona a tu post
-- - Cuando alguien comenta en tu post
-- - Cuando alguien te sigue
-- - Cuando alguien responde a tu comentario
-- ============================================================

-- 1. Crear tabla de notificaciones
CREATE TABLE IF NOT EXISTS public.notifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  actor_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  event_type VARCHAR(50) NOT NULL, -- 'like', 'comment', 'follow', 'reply'
  entry_id UUID REFERENCES public.diary_entries(id) ON DELETE CASCADE,
  comment_id UUID REFERENCES public.diary_comments(id) ON DELETE CASCADE,
  data JSONB, -- Extra data: reaction emoji, comment preview, etc
  read BOOLEAN DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE public.notifications ENABLE ROW LEVEL SECURITY;

-- 2. RLS Policies
CREATE POLICY "User reads own notifications" ON public.notifications
  FOR SELECT TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "System creates notifications" ON public.notifications
  FOR INSERT WITH CHECK (true);

CREATE POLICY "User updates own notification" ON public.notifications
  FOR UPDATE TO authenticated
  USING (auth.uid() = user_id);

-- 3. Índices
CREATE INDEX IF NOT EXISTS idx_notifications_user_id ON public.notifications(user_id);
CREATE INDEX IF NOT EXISTS idx_notifications_read ON public.notifications(user_id, read);
CREATE INDEX IF NOT EXISTS idx_notifications_created ON public.notifications(created_at DESC);

-- 4. Function: Notificar cuando hay reacción
CREATE OR REPLACE FUNCTION notify_on_reaction()
RETURNS TRIGGER AS $$
DECLARE
  entry_author UUID;
  actor_nickname TEXT;
BEGIN
  -- Get entry author
  SELECT user_id INTO entry_author FROM public.diary_entries WHERE id = NEW.entry_id;
  SELECT nickname INTO actor_nickname FROM public.profiles WHERE id = NEW.user_id;
  
  -- Don't notify self
  IF entry_author != NEW.user_id THEN
    INSERT INTO public.notifications (user_id, actor_id, event_type, entry_id, data)
    VALUES (
      entry_author,
      NEW.user_id,
      'reaction',
      NEW.entry_id,
      jsonb_build_object('reaction', NEW.reaction, 'actor', actor_nickname)
    );
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_notify_reaction
AFTER INSERT ON public.diary_reactions
FOR EACH ROW EXECUTE FUNCTION notify_on_reaction();

-- 5. Function: Notificar cuando hay comentario
CREATE OR REPLACE FUNCTION notify_on_comment()
RETURNS TRIGGER AS $$
DECLARE
  entry_author UUID;
  actor_nickname TEXT;
  comment_preview TEXT;
BEGIN
  -- Get entry author and comment preview
  SELECT user_id INTO entry_author FROM public.diary_entries WHERE id = NEW.entry_id;
  SELECT nickname INTO actor_nickname FROM public.profiles WHERE id = NEW.user_id;
  comment_preview := SUBSTRING(NEW.content, 1, 100);
  
  -- Don't notify self
  IF entry_author != NEW.user_id THEN
    INSERT INTO public.notifications (user_id, actor_id, event_type, entry_id, comment_id, data)
    VALUES (
      entry_author,
      NEW.user_id,
      'comment',
      NEW.entry_id,
      NEW.id,
      jsonb_build_object('preview', comment_preview, 'actor', actor_nickname)
    );
  END IF;
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_notify_comment
AFTER INSERT ON public.diary_comments
FOR EACH ROW EXECUTE FUNCTION notify_on_comment();

-- 6. Function: Notificar cuando alguien te sigue
CREATE OR REPLACE FUNCTION notify_on_follow()
RETURNS TRIGGER AS $$
DECLARE
  follower_nickname TEXT;
BEGIN
  SELECT nickname INTO follower_nickname FROM public.profiles WHERE id = NEW.follower_id;
  
  INSERT INTO public.notifications (user_id, actor_id, event_type, data)
  VALUES (
    NEW.following_id,
    NEW.follower_id,
    'follow',
    jsonb_build_object('actor', follower_nickname)
  );
  
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Asumir que tabla follows existe
DROP TRIGGER IF EXISTS trg_notify_follow ON public.follows;
CREATE TRIGGER trg_notify_follow
AFTER INSERT ON public.follows
FOR EACH ROW EXECUTE FUNCTION notify_on_follow();

-- 7. Función helper: obtener notificaciones por usuario
CREATE OR REPLACE FUNCTION get_user_notifications(target_user UUID, limit_count INT DEFAULT 20)
RETURNS TABLE(
  id UUID,
  actor_id UUID,
  actor_nickname TEXT,
  event_type VARCHAR,
  entry_id UUID,
  comment_id UUID,
  data JSONB,
  read BOOLEAN,
  created_at TIMESTAMPTZ
) AS $$
SELECT 
  n.id,
  n.actor_id,
  p.nickname,
  n.event_type,
  n.entry_id,
  n.comment_id,
  n.data,
  n.read,
  n.created_at
FROM public.notifications n
LEFT JOIN public.profiles p ON n.actor_id = p.id
WHERE n.user_id = target_user
ORDER BY n.created_at DESC
LIMIT limit_count;
$$ LANGUAGE SQL;

-- 8. Función helper: marknotifications as read
CREATE OR REPLACE FUNCTION mark_notifications_read(target_user UUID)
RETURNS INTEGER AS $$
  UPDATE public.notifications 
  SET read = true 
  WHERE user_id = target_user AND read = false
  RETURNING 1;
$$ LANGUAGE SQL;
