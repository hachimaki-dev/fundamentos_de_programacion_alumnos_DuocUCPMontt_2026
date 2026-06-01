# 🚀 Setup e Instalación — Iniciativa 3 Facciones

**Estado:** Listo para ejecutar en Supabase  
**Archivos SQL:** 2 (deben ejecutarse en orden)  
**Version:** 8 Mayo 2026

---

## 📋 Checklist Pre-Deploy

Antes de ejecutar los scripts SQL:

- [ ] Copia de seguridad de BD realizada
- [ ] Acceso a Supabase admin panel confirmado
- [ ] Scripts SQL revisados y entendidos
- [ ] No hay conflictos con otras migraciones en progreso

---

## 🔧 Paso 1: Ejecutar Script de Fix RLS

**Archivo:** `supabase/11_fix_faction_rls.sql`

```sql
-- En Supabase > SQL Editor, pega y ejecuta:
```

**¿Qué hace?**
- Arregla RLS policies en `github_sync_history` (permitir lectura a todos)
- Crea vista `faction_activity_feed` para actividad reciente
- Crea vista `faction_challenges_with_progress` para desafíos
- Crea vista `faction_wall_feed` para mural

**Resultado esperado:**
```
✓ 8 sentencias ejecutadas exitosamente
```

---

## 🔧 Paso 2: Ejecutar Script de Tablas y Mural

**Archivo:** `supabase/12_faction_challenges_and_wall.sql`

```sql
-- En Supabase > SQL Editor, pega y ejecuta:
```

**¿Qué hace?**
- Crea tabla `faction_challenges`
- Crea tabla `faction_wall`
- Crea índices para performance
- Configura RLS policies
- Crea trigger para auto-XP rewards
- Crea vistas helper

**Resultado esperado:**
```
✓ 15+ sentencias ejecutadas exitosamente
```

---

## ✅ Verificación Post-Deploy

### En Supabase Console (SQL):

```sql
-- 1. Verificar tablas existen
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public' AND table_name IN (
  'faction_challenges', 'faction_wall', 'factions'
);

-- Resultado esperado: 3 filas

-- 2. Verificar RLS está habilitado
SELECT schemaname, tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public' AND tablename IN (
  'faction_challenges', 'faction_wall'
);

-- Resultado esperado: todos "t" (true)

-- 3. Verificar vistas existen
SELECT table_name FROM information_schema.views
WHERE table_schema = 'public' AND table_name LIKE 'faction%';

-- Resultado esperado: 3+ vistas
```

### En Browser:

1. **Abre `pages/factions.html`**
   - ¿Carga sin hang? ✓
   - ¿Se ve el leaderboard? ✓

2. **Si eres miembro de una facción:**
   - ¿Ves el tab "⚔️ Desafíos"? ✓
   - ¿Ves el tab "💬 Mural"? ✓

3. **Tab Desafíos:**
   - Clic "+ Crear Desafío" → abre formulario ✓
   - Llena datos y clic "Crear" → aparece en lista ✓

4. **Tab Mural:**
   - Escribe mensaje → contador va 0/500 ✓
   - Clic "Publicar" → aparece en feed ✓
   - Clic avatar → navega a perfil ✓

---

## 🐛 Troubleshooting

### La página factions.html se queda cargando

**Causa:** RLS policy bloqueando queries  
**Solución:** Asegúrate de ejecutar `11_fix_faction_rls.sql` primero

**Verifica:**
```sql
SELECT * FROM pg_policies 
WHERE tablename = 'github_sync_history';

-- Debe mostrar política que permite authenticated
```

### Desafíos/Mural no aparecen

**Causa:** Tablas no creadas  
**Solución:** Ejecuta `12_faction_challenges_and_wall.sql`

**Verifica:**
```sql
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_name IN ('faction_challenges', 'faction_wall');

-- Resultado esperado: 2
```

### Error al crear desafío

**Causa:** RLS policy restrictiva o permisos  
**Solución:** Verifica estar logueado como miembro de una facción

```sql
-- En query:
SELECT * FROM public.faction_challenges LIMIT 1;

-- Si error 403: problema de RLS
```

### Mensajes no se guardan en mural

**Causa:** RLS policy o permiso INSERTO  
**Solución:** Verifica estar en una facción (faction_id != NULL)

```sql
SELECT faction_id FROM public.profiles WHERE id = auth.uid();

-- Debe mostrar un UUID
```

---

## 📡 Real-Time Setup

Los subscriptions en `factions-app.js` requieren que Supabase Realtime esté habilitado.

### Verificar en Supabase Console:

**Realtime > Tables:**
- [ ] `factions` — Habilitada INSERT/UPDATE
- [ ] `github_sync_history` — Habilitada INSERT
- [ ] `faction_challenges` — Habilitada INSERT/UPDATE
- [ ] `faction_wall` — Habilitada INSERT/UPDATE/DELETE

### Si no están habilitadas:

1. Ve a **Realtime** en Supabase
2. Busca cada tabla
3. Toggle ✓ para aquellos eventos que quieras

---

## 🔒 Security Checklist

Verificar RLS policies:

```sql
-- 1. Only authenticated users
SELECT policyname FROM pg_policies 
WHERE tablename = 'faction_challenges' AND DEFINITION LIKE '%authenticated%';

-- 2. Faction members only
SELECT DEFINITION FROM pg_policies
WHERE tablename = 'faction_wall' AND policyname LIKE '%faction%';

-- 3. Own data only
SELECT DEFINITION FROM pg_policies
WHERE tablename = 'faction_wall' AND policyname LIKE '%user%';
```

---

## 📧 Rollback Plan

Si algo sale mal:

```sql
-- Revert everything:
DROP TABLE IF EXISTS public.faction_wall;
DROP TABLE IF EXISTS public.faction_challenges;
DROP VIEW IF EXISTS public.faction_wall_feed;
DROP VIEW IF EXISTS public.faction_challenges_with_progress;
DROP VIEW IF EXISTS public.faction_activity_feed;
DROP FUNCTION IF EXISTS update_faction_challenge_xp();
DROP TRIGGER IF EXISTS trigger_faction_challenge_xp ON public.faction_challenges;

-- Revert RLS:
DROP POLICY IF EXISTS "Authenticated users can view all github history" ON public.github_sync_history;
CREATE POLICY "Users can view their own github history"
  ON public.github_sync_history FOR SELECT TO authenticated
  USING (auth.uid() = user_id);
```

---

## 🎯 Después del Deploy

1. **Backup del código:**
   ```bash
   git add .
   git commit -m "feat: faction challenges, wall, real-time dashboard (FASE 1-3)"
   git push
   ```

2. **Comunicar a estudiantes:**
   - Nueva sección de Desafíos
   - Nuevo Mural de Facción
   - Real-time stats

3. **Monitorear:**
   - Performance de queries
   - Errores en console
   - Feedback de usuarios

---

## 📞 Support

Si hay problemas:

1. Revisar DevTools > Console (errores JS)
2. Revisar DevTools > Network (fallos de query)
3. Revisar Supabase > Logs para errores de BD
4. Ejecutar queries de verificación arriba

✨ **¡Listo para deploy!**
