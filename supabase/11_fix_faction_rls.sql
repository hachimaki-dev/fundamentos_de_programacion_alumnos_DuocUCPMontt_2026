-- ═══════════════════════════════════════════════════════════════
-- 🔧 FIX: RLS Policies para github_sync_history y factions
-- ═══════════════════════════════════════════════════════════════

-- PROBLEMA: El RLS original en github_sync_history solo permite ver tus propios registros
-- SOLUCIÓN: Permitir que usuarios autenticados vean TODOS los registros (necesario para dashboard de facciones)

DROP POLICY IF EXISTS "Users can view their own github history" ON public.github_sync_history;
CREATE POLICY "Authenticated users can view all github history"
  ON public.github_sync_history FOR SELECT TO authenticated
  USING (true); -- Permitir a todos los usuarios autenticados

DROP POLICY IF EXISTS "Users can insert their own github history" ON public.github_sync_history;
CREATE POLICY "Users can insert their own github history"
  ON public.github_sync_history FOR INSERT TO authenticated
  WITH CHECK (auth.uid() = user_id);

-- También asegurar que factions es readable por todos
CREATE POLICY "Authenticated users can view factions"
  ON public.factions FOR SELECT TO authenticated
  USING (true);

-- Crear una VIEW para recent activity si la needs a ser más performante
CREATE OR REPLACE VIEW public.faction_activity_feed AS
SELECT 
  'github_sync' as activity_type,
  g.id,
  g.user_id,
  p.faction_id,
  p.nickname,
  p.avatar_id,
  p.avatar_source,
  p.avatar_custom_url,
  g.repo_name,
  g.xp_awarded,
  g.created_at,
  CONCAT('Commits en ', g.repo_name) as activity_text
FROM public.github_sync_history g
JOIN public.profiles p ON g.user_id = p.id
WHERE g.created_at > now() - interval '7 days'
ORDER BY g.created_at DESC
LIMIT 50;
