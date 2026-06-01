# 🔍 AUDITORÍA DASHBOARD — Academia Hachimaki 2026

**Fecha:** 14 de mayo de 2026  
**Estado:** En revisión  
**Responsable:** Sistema de auditoría automática

---

## 📊 PROBLEMAS CRÍTICOS ENCONTRADOS

### 1. ❌ **LIKES NO FUNCIONAN**

#### Problema
- El botón de likes en el feed del dashboard NO es funcional
- No existe método `toggleLike()` en `dashboard-app.js`
- No hay tabla `diary_likes` en la base de datos para rastrear likes individuales

#### Detalles Técnicos
- **Archivo:** `pages/dashboard.html` línea 254
- **Código:** `<button class="sd-action" :class="{liked: item._liked}">♥ {{ item.likes_count || 0 }}</button>`
- **Problema:** Botón sin `@click` handler
- **Estado en DB:** Existe columna `likes_count` en `diary_entries` pero no es actualizable por usuario

#### Impacto
- **Severidad:** 🔴 CRÍTICA (Engagement feature no funcional)
- **Usuarios afectados:** Todos los usuarios del dashboard
- **Impacto en UX:** Usuarios ven que pueden hacer click pero nada sucede

---

### 2. ⚠️ **AVATARES NO CLICKEABLES EN VARIOS LUGARES**

#### Problemas de Navegación
Los siguientes lugares tienen avatares/fotos de perfil que NO navegan al perfil del usuario:

| Ubicación | Línea HTML | Componente | Estado |
|-----------|-----------|-----------|--------|
| Leaderboard | ~424 | `<img :src="getAvatar(p.avatar_id)" />` | ❌ NO clickeable |
| Sugerencias para seguir | ~438 | `<img :src="getAvatar(s.avatar_id)" />` | ❌ NO clickeable |
| Banner de competencias | ~484 | `<img :src="getAvatar(avId)" />` | ❌ NO clickeable |
| Feed de posts | ~220 | `data-feed-avatar` | ✅ Clickeable |
| Comentarios | ~260 | `data-comment-avatar` | ✅ Clickeable |

#### Causa Raíz
- Faltan atributos `data-user-id` y `data-feed-avatar` (u otros)
- El método `setupProfileNavigation()` no se llama para estos elementos
- Los avatares del leaderboard/sugerencias se generan dinámicamente pero sin atributos de navegación

#### Impacto
- **Severidad:** 🟡 ALTA (Inconsistencia de UX)
- **Usuarios afectados:** Todos al intentar acceder a perfiles desde leaderboard
- **Impacto en discoverabilidad:** Los usuarios no pueden descubrir fácilmente otros perfiles

---

## 📋 AUDITORÍA DE COMPONENTES

### ✅ Calidad de Frontend
- **Vue.js 3:** Correctamente implementado
- **Estructura componentes:** Buena (sidebar left/center/right)
- **Responsividad:** Implementada con mobile tabs
- **Gestión de estado:** Correcta en data() pero incompleta en métodos

### ⚠️ Problemas en Estructura
| Elemento | Actual | Esperado | Brecha |
|----------|--------|----------|--------|
| Manejo de likes | No existe | Tabla + RPC + Frontend | 100% |
| Avatar navigation | Parcial (2/5) | Global (5/5) | 60% |
| Comentarios | ✅ Completo | ✅ Completo | 0% |
| Feed rendering | ✅ Completo | ✅ Completo | 0% |

---

## 🎯 PLAN DE SOLUCIONES

### FASE 1: Implementar Sistema de Likes (Prioridad 🔴 CRÍTICA)

#### Paso 1.1: Crear tabla `diary_likes` en Supabase
```sql
CREATE TABLE IF NOT EXISTS public.diary_likes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
  entry_id UUID NOT NULL REFERENCES public.diary_entries(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(user_id, entry_id)
);

ALTER TABLE public.diary_likes ENABLE ROW LEVEL SECURITY;

-- RLS Policies
CREATE POLICY "Anyone reads diary likes" ON public.diary_likes
  FOR SELECT TO authenticated USING (true);
CREATE POLICY "User creates own diary like" ON public.diary_likes
  FOR INSERT TO authenticated WITH CHECK (auth.uid() = user_id);
CREATE POLICY "User deletes own diary like" ON public.diary_likes
  FOR DELETE TO authenticated USING (auth.uid() = user_id);
```

#### Paso 1.2: Crear trigger para mantener `likes_count`
```sql
-- Trigger para cuando se LikE una entrada
CREATE OR REPLACE FUNCTION update_diary_likes_count()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    UPDATE public.diary_entries 
    SET likes_count = likes_count + 1 
    WHERE id = NEW.entry_id;
    RETURN NEW;
  ELSIF TG_OP = 'DELETE' THEN
    UPDATE public.diary_entries 
    SET likes_count = GREATEST(0, likes_count - 1) 
    WHERE id = OLD.entry_id;
    RETURN OLD;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_diary_likes_count_update
AFTER INSERT OR DELETE ON public.diary_likes
FOR EACH ROW EXECUTE FUNCTION update_diary_likes_count();
```

#### Paso 1.3: Frontend - Añadir método `toggleLike()`
En `js/dashboard-app.js`, agregar en la sección `methods`:
```javascript
async toggleLike(item) {
  if (item._type !== 'diary') return; // Solo para diarios
  
  const client = SupabaseManager.getClient();
  
  try {
    if (item._liked) {
      // Remover like
      await client.from('diary_likes')
        .delete()
        .eq('user_id', this.profile.id)
        .eq('entry_id', item.id);
      
      item._liked = false;
      item.likes_count = Math.max(0, (item.likes_count || 0) - 1);
    } else {
      // Agregar like
      await client.from('diary_likes')
        .insert({
          user_id: this.profile.id,
          entry_id: item.id,
        });
      
      item._liked = true;
      item.likes_count = (item.likes_count || 0) + 1;
    }
  } catch (e) {
    console.error('Error en like:', e);
    SupabaseManager.showToast('Error al procesar like', 'error');
  }
}
```

#### Paso 1.4: Frontend - Actualizar feed para cargar estado de likes
En `loadFeed()`, después de cargar las entradas:
```javascript
// Cargar likes del usuario actual
if (profile.id) {
  try {
    const { data: userLikes } = await client.from('diary_likes')
      .select('entry_id')
      .eq('user_id', profile.id);
    
    if (userLikes) {
      const likedIds = new Set(userLikes.map(l => l.entry_id));
      items.forEach(item => {
        if (item._type === 'diary') {
          item._liked = likedIds.has(item.id);
        }
      });
    }
  } catch (e) { /* */ }
}
```

#### Paso 1.5: HTML - Agregar @click al botón de likes
En `pages/dashboard.html` línea ~254, cambiar:
```html
<button class="sd-action" :class="{liked: item._liked}">♥ {{ item.likes_count || 0 }}</button>
```

A:
```html
<button class="sd-action" :class="{liked: item._liked}" @click="toggleLike(item)" :disabled="postingNew">♥ {{ item.likes_count || 0 }}</button>
```

---

### FASE 2: Hacer Avatares Clickeables en Todos Lados (Prioridad 🟡 ALTA)

#### Paso 2.1: Leaderboard - Agregar data attributes
En `pages/dashboard.html` línea ~427, cambiar:
```html
<div class="sd-av" style="width:24px;height:24px"><img :src="getAvatar(p.avatar_id)" /></div>
```

A:
```html
<div class="sd-av" style="width:24px;height:24px"><img :src="getAvatar(p.avatar_id)" :data-user-id="p.id" data-feed-avatar /></div>
```

#### Paso 2.2: Sugerencias - Agregar data attributes  
En `pages/dashboard.html` línea ~441, cambiar:
```html
<div class="sd-av" style="width:28px;height:28px"><img :src="getAvatar(s.avatar_id)" /></div>
```

A:
```html
<div class="sd-av" style="width:28px;height:28px"><img :src="getAvatar(s.avatar_id)" :data-user-id="s.id" data-feed-avatar /></div>
```

#### Paso 2.3: Banner de Competencias - Agregar data attributes
En `pages/dashboard.html` línea ~487, cambiar:
```html
<img :src="getAvatar(avId)" />
```

A requires access to user_id. Necesita refactor:
```html
<img :src="getAvatar(avId)" :data-user-id="avId" data-feed-avatar />
```

**Nota:** El banner actual usa `avId` directamente del avatar, pero debería usar el `user_id` del submitter. Ver paso 2.3b.

#### Paso 2.3b: Dashboard-app.js - Refactor loadActiveCompetitionsBanner
Cambiar la estructura para guardar `user_id` además de avatar:
```javascript
comp._submitters = submitters.map(s => ({
  user_id: s.user_id,
  profiles: s.profiles,
}));
```

Luego en HTML:
```html
<div v-for="(submitter, i) in comp._submitters.slice(0, 5)" :key="i" 
  class="sd-av sd-banner-av"
  :style="{ zIndex: 5 - i }">
  <img :src="getAvatar(submitter.profiles)" 
    :data-user-id="submitter.user_id" 
    data-feed-avatar />
</div>
```

#### Paso 2.4: Llamar setupProfileNavigation después de actualizar
En `loadSidebarRight()` y `loadActiveCompetitionsBanner()`, al final agregar:
```javascript
this.$nextTick(() => {
  this.setupProfileNavigation();
});
```

---

### FASE 3: Comparativa Frontend vs Backend (Auditoría)

#### Checklist de Sincronización
- [ ] **Profiles**: ✅ Frontend y Backend sincronizados
- [ ] **Diary Entries**: ✅ Frontend y Backend sincronizados
- [ ] **Diary Comments**: ✅ Frontend y Backend sincronizados  
- [ ] **Diary Likes**: ❌ Backend existe (propuesto), Frontend incompleto
- [ ] **Followers/Following**: ✅ Frontend y Backend sincronizados
- [ ] **Leaderboard**: ✅ Frontend y Backend sincronizados
- [ ] **Achievements**: ✅ Frontend y Backend sincronizados
- [ ] **Factions**: ✅ Frontend y Backend sincronizados
- [ ] **Competitions**: ✅ Frontend y Backend sincronizados
- [ ] **GitHub Sync**: ✅ Frontend y Backend sincronizados

---

## 🚀 SUGERENCIAS DE MEJORAS/REWORKS

### PRIORITARIAS (Impacto Alto)

#### 1. **Implementar Real-time Updates con Supabase Subscriptions**
- **Problema actual:** El feed se carga una sola vez
- **Mejora:** Usar `client.realtime` para actualizaciones en vivo
- **Beneficio:** Los likes, comentarios y nuevas entradas aparecen en tiempo real sin refresh
- **Esfuerzo:** 🎯 Medio (2-3 horas)

#### 2. **Sistema de Notificaciones Mejora**
- **Problema actual:** Notificaciones calculadas (no event-driven)
- **Mejora:** Tabla `notifications` con RLS, actualizaciones en tiempo real
- **Beneficio:** Notificaciones instantáneas cuando alguien comenta o sigue
- **Esfuerzo:** 🎯 Medio (3-4 horas)

#### 3. **Reacciones en lugar de solo "Likes"**
- **Problema actual:** Solo ❤️ likes
- **Mejora:** Agregar emojis: 🔥 ❤️ 👏 😱 🤔
- **Beneficio:** Mayor engagement, expresión más granular
- **Esfuerzo:** 🎯 Bajo-Medio (3-4 horas)

#### 4. **Feed Algorithm / Personalización**
- **Problema actual:** Feed es solo cronológico
- **Mejora:** 
  - Priorizar posts de gente que sigues
  - Priorizar posts con más engagement
  - Filtrar por tags/tópicos
- **Beneficio:** Feed más relevante, mejor engagement
- **Esfuerzo:** 🎯 Alto (6-8 horas)

---

### IMPORTANTES (Impacto Medio)

#### 5. **Lazy Loading de Feed**
- **Problema actual:** Carga todos los items de una vez
- **Mejora:** Pagination + infinite scroll
- **Beneficio:** Mejor performance en conexiones lentas
- **Esfuerzo:** 🎯 Medio (3-4 horas)

#### 6. **Draft System para Posts**
- **Mejora:** Guardar borradores localmente + en DB
- **Beneficio:** Usuarios no pierden texto si cierran pestaña
- **Esfuerzo:** 🎯 Bajo (2-3 horas)

#### 7. **Editar/Eliminar Posts Propios**
- **Mejora:** Añadir botones en posts del usuario actual
- **Beneficio:** Control sobre contenido publicado
- **Esfuerzo:** 🎯 Bajo (2 horas)

#### 8. **Expandir Vista Previa de Comentarios**
- **Problema actual:** Solo muestra 1 comentario
- **Mejora:** Mostrar últimos 3 comentarios o contador
- **Beneficio:** Mejor preview del engagement
- **Esfuerzo:** 🎯 Bajo (1-2 horas)

---

### OPCIONALES (Nice-to-Have)

#### 9. **Menciones (@usuario) en comentarios**
- **Beneficio:** Notificaciones dirigidas + engagement directo
- **Esfuerzo:** 🎯 Medio-Alto (4-5 horas)

#### 10. **Threads/Replies directas a comentarios**
- **Beneficio:** Conversaciones más organizadas
- **Esfuerzo:** 🎯 Alto (5-6 horas)

#### 11. **Favoritos/Bookmarks**
- **Beneficio:** Guardar posts para leer después
- **Esfuerzo:** 🎯 Bajo (2 horas)

#### 12. **Share a TikTok/Instagram integration**
- **Beneficio:** Viralidad, alcance externo
- **Esfuerzo:** 🎯 Medio (4 horas)

---

## 📊 COMPARACIÓN FRONTEND vs BACKEND

### Tablas Supabase vs Funcionalidad Frontend

| Tabla | Exists | Frontend | Sync | Status |
|-------|--------|----------|------|--------|
| `profiles` | ✅ | ✅ | ✅ | Completo |
| `diary_entries` | ✅ | ✅ | ✅ | Completo |
| `diary_comments` | ✅ | ✅ | ✅ | Completo |
| `diary_likes` | ❌ Propuesto | ❌ | N/A | Falta implementar |
| `follows` (follow-system) | ✅ | ✅ | ✅ | Completo |
| `notifications` | ❌ Manual | ⚠️ Partial | ❌ | Mejora sugerida |
| `achievements_catalog` | ✅ | ✅ | ✅ | Completo |
| `competitions` | ✅ | ✅ | ✅ | Completo |
| `competition_submissions` | ✅ | ✅ | ✅ | Completo |
| `factions` | ✅ | ✅ | ✅ | Completo |
| `github_sync_history` | ✅ | ✅ | ✅ | Completo |

---

## 🎬 ORDEN DE IMPLEMENTACIÓN RECOMENDADO

### Sprint 1 (Hoy - Crítico)
1. ✅ **Crear tabla `diary_likes`** + RLS + trigger
2. ✅ **Implementar `toggleLike()` en frontend**
3. ✅ **Hacer avatares clickeables en leaderboard/sugerencias/banner**

### Sprint 2 (Esta semana - Alta Prioridad)
4. Real-time updates con Supabase subscriptions
5. Mejorar sistema de notificaciones
6. Agregar reacciones emoji

### Sprint 3 (Próximas 2 semanas)
7. Feed personalization algorithm
8. Lazy loading + infinite scroll
9. Draft system
10. Editar/eliminar posts

---

## 🔗 REFERENCIAS DE CÓDIGO

- Dashboard App: [js/dashboard-app.js](js/dashboard-app.js)
- Dashboard HTML: [pages/dashboard.html](pages/dashboard.html)
- User Navigation: [js/user-navigation.js](js/user-navigation.js)
- Supabase Client: [js/supabase-client.js](js/supabase-client.js)
- Social Learning Schema: [supabase/06_social_learning.sql](supabase/06_social_learning.sql)

---

**Fin de Auditoría**

---
