# 🚀 Plan de Mejoras — Academia Hachimaki 2026

**Estado:** Draft  
**Última actualización:** 7 Mayo 2026  
**Prioridad:** Alta (impacto directo en engagement)

---

## 📋 Resumen Ejecutivo

Tres iniciativas estratégicas para transformar la plataforma de **plataforma educativa** a **comunidad social de aprendizaje**:

1. **🔗 Navegación por Perfil** — Clic en avatar → Perfil público del usuario
2. **💬 Comentarios en Feed** — Habilitar comentarios vivos (sustituir mock)
3. **⚔️ Sala de Facciones Interactiva** — Gamificación de rivalidad entre secciones

---

## ✅ INICIATIVA 1: Navegación por Perfil

### 🎯 Objetivo
Clics en avatares de usuarios en cualquier sección (feed, facciones, competencias) redirigen al perfil público.

### 📊 Estado Actual
- ✅ Perfil público existe en `profile.html`
- ❌ **No hay navegación desde avatares**
- ❌ No hay sistema consistente de "click usuario" en la plataforma

### 🔧 Implementación

#### Paso 1: Crear componente reutilizable `UserCard.js`
```js
// Clase para manejar clics en cualquier elemento de usuario
class UserCardHandler {
  static navigateTo(userId) {
    window.location.href = `profile.html?user=${userId}`;
  }
  
  static makeClickable(element, userId) {
    element.style.cursor = 'pointer';
    element.addEventListener('click', (e) => {
      e.stopPropagation();
      this.navigateTo(userId);
    });
  }
}
```

#### Paso 2: Integrar en Dashboard
- **Feed:** Clic en avatar del autor → Perfil
- **Comentarios:** Clic en avatar del comentarista → Perfil
- **Sidebar Notifications:** Clic en usuario → Perfil

#### Paso 3: Integrar en Facciones
- **Miembros grid:** Cada avatar es clickable
- **Top comentarios:** Avatares conducen al perfil

#### Paso 4: Actualizar `profile.html`
- Parsear parámetro `?user=UUID` en query string
- Cargar perfil dinámicamente desde URL

### 🎨 Design System
Mantener consistencia con social-dashboard.css:
- Transición suave: `hover:opacity-80 transition`
- Cursor: `cursor-pointer`
- Overlay pattern: `.sd-av:hover { opacity: 0.8 }`

### ✨ Bonus Features
- Share de perfil: `profile.html?ref=dashboard`
- Dark mode en perfil (ya existe `theme-engine.js`)

---

## 💬 INICIATIVA 2: Comentarios en Feed (MVP)

### 🎯 Objetivo
Reemplazar mock de comentarios con sistema funcional en tiempo real.

### 📊 Estado Actual
- ✅ Tabla `diary_comments` existe en Supabase
- ✅ RLS policies configuradas
- ❌ **No hay UI para escribir comentarios**
- ❌ **No hay validación en frontend**
- ❌ **Mock solo muestra preview, no interacción**

### 🔧 Implementación

#### Fase 1: UI Comentarios (1-2h)
```html
<!-- Añadir a cada post en feed -->
<div class="sd-comment-form" v-if="expandedComments[item._key]">
  <div class="sd-input-group">
    <input 
      v-model="newComments[item._key]" 
      type="text" 
      placeholder="Añade un comentario..."
      @keyup.enter="submitComment(item)"
      class="sd-input"
    />
    <button 
      @click="submitComment(item)"
      :disabled="!newComments[item._key]?.trim()"
      class="sd-btn-primary"
    >
      Enviar
    </button>
  </div>
</div>
```

#### Fase 2: Métodos en JavaScript (1-2h)
```js
// En dashboard-app.js
async submitComment(item) {
  const content = this.newComments[item._key];
  if (!content?.trim()) return;
  
  try {
    const { data } = await client.from('diary_comments').insert([{
      entry_id: item.id,
      user_id: this.profile.id,
      content: content,
    }]).select('*, profiles(*)').single();
    
    // Actualizar feed
    item._comments.push(data);
    item._commentsCount++;
    this.newComments[item._key] = '';
  } catch (e) {
    console.error('Error posting comment', e);
  }
}
```

#### Fase 3: Validación
- Min length: 2 caracteres
- Max length: 500 caracteres
- Sanitizar HTML (usar `DOMPurify.sanitize()`)
- Debounce en submit (max 1 comentario/segundo)

#### Fase 4: Respuestas en Tiempo Real
- Usar Supabase Realtime para actualizaciones vivas
- Mostrar "Nueva respuesta" floating

### 🎨 Design System
Seguir `.sd-inline-comment` but interactive:
```css
.sd-comment-form {
  padding: 12px;
  background: var(--t-surface-hover);
  border-radius: 8px;
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.sd-comment-form input {
  flex: 1;
  border: 1px solid var(--t-border);
  border-radius: 4px;
  padding: 8px 12px;
  font-size: 12px;
}
```

### ✨ Bonus Features
- Menciones: `@usuario` with autocomplete
- Reacciones emoji: 👍 ❤️ 🔥
- Editar/Eliminar comentarios propios
- Marcar comentarios como "inapropiados"

---

## ⚔️ INICIATIVA 3: Sala de Facciones Interactiva

### 🎯 Objetivo
Transformar la "Sala de Facciones" de demo estática a **hub interactivo** con:
- 📊 Dashboard de actividades en vivo
- 🏆 Tablero de desafíos intra-facción
- 💬 Chat/Mural de facción
- 📈 Estadísticas detalladas

### 📊 Estado Actual
- ✅ Tabla `factions` existe
- ✅ Miembros listados
- ✅ XP total por facción
- ❌ **Sin interactividad**
- ❌ **Sin desafíos entre facciones**
- ❌ **Sin feed de actividades de facción**

### 🔧 Implementación (Roadmap)

#### **Fase 1 (MVP):** Tablero Vivo (2-3h)
**Features:**
- Real-time XP updates (Supabase Realtime)
- "Actividad reciente" actual (no hardcoded)
- Botón **"Ver Miembros"** con avatares clickables
- Estadísticas mejores:
  - XP promedio por nivel
  - % de participación en competencias
  - Actividad última semana

**Backend:**
```sql
-- Crear vista para actividades de facción
CREATE VIEW faction_activity AS
SELECT f.id, f.faction_name, COUNT(DISTINCT p.id) as active_members,
       SUM(p.xp) as total_xp, MAX(p.updated_at) as last_update
FROM factions f
LEFT JOIN profiles p ON f.id = p.faction_id
GROUP BY f.id, f.faction_name;
```

#### **Fase 2:** Desafíos Intra-Facción (4-6h)
**Table:**
```sql
CREATE TABLE faction_challenges (
  id UUID PRIMARY KEY,
  faction_id UUID REFERENCES factions(id),
  title TEXT,
  description TEXT,
  target_xp INTEGER, -- Ej: ganar 500 XP en 3 días
  deadline TIMESTAMPTZ,
  reward_xp INTEGER,
  status TEXT, -- 'active', 'completed', 'failed'
);
```

**Features:**
- Crear desafío por profesor o líder de facción
- Progreso visual (barra de XP)
- Notificaciones automáticas
- Bonus XP si completado antes de deadline

#### **Fase 3:** Mural de Facción (Chat Asincrónico) (4h)
```sql
CREATE TABLE faction_wall (
  id UUID PRIMARY KEY,
  faction_id UUID REFERENCES factions(id),
  user_id UUID REFERENCES profiles(id),
  message TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
);
```

**UI:**
- Sección "Mural" en sidebar de facciones
- Mensajes chronológicos
- Reacciones emoji
- Menciones inteligentes (@usuario)

#### **Fase 4:** Leaderboard Expandido (2h)
Mostrar top 10 de cada facción:
- Por XP individual
- Por contribuciones (commits, comentarios)
- Por participación en competencias

---

## 🛠️ Plan de Ejecución

### Orden Recomendado
| # | Iniciativa | Esfuerzo | Dependencias | Deadline |
|---|-----------|----------|-------------|----------|
| 1 | **Navegación Perfil** | 1-2h | Ninguna | 7 Mayo |
| 2 | **Feed Comentarios MVP** | 2-3h | + test DB | 8 Mayo |
| 3 | **Facciones Dashboard** | 3-4h | Realtime setup | 10 Mayo |
| 4 | **Desafíos Intra-Facción** | 4-6h | + UI avanzada | 12-14 Mayo |

### Milestones
- ✅ **Hito 1 (7 Mayo):** Navegación perfil funciona en 3+ secciones
- ✅ **Hito 2 (8-9 Mayo):** Comentarios vivos en feed (MVP sin menciones)
- ✅ **Hito 3 (10-11 Mayo):** Facciones dashboard + Realtime
- ✅ **Hito 4 (12-14 Mayo):** Desafíos intra-facción completos

---

## 🎨 Principios de Diseño

### Mantener Consistencia
Todos los cambios siguen **social-dashboard.css**:
- Color scheme: CSS custom properties (`--t-accent`, `--t-text`, etc.)
- Spacing: `8px`, `12px`, `16px` múltiplos
- Bordes: `border: 1px solid var(--t-border)`
- Transiciones: `transition: all 0.2s ease`

### Mobile-First
- Tabs en móvil: ya existen `.sd-mobile-tabs`
- Responsive: `@media (max-width: 768px)`

### Performance
- Lazy load avatares
- Debounce search/filter (300ms)
- Virtualización si >50 items

### Accessibility
- Labels en inputs
- ARIA labels en botones
- Keyboard navigation (Tab, Enter)

---

## 📝 Notas Técnicas

### Supabase Setup Requerido
- ✅ Tablas ya existen (diary_comments, factions, etc.)
- ⚠️ Necesita: Configurar Realtime en `diary_comments`
- ⚠️ Necesita: Crear vistas SQL para actividades

### Dependencies
- Vue.js 3: ✅ Ya instalado
- Supabase JS: ✅ Ya configurado
- DOMPurify: ✅ Cargado en profile.html

### Testing
- Probar con múltiples usuarios en paralelo
- Verificar RLS policies
- Test en temas light/dark

---

## 🤔 Preguntas Abiertas

1. ¿Deseas **notificaciones push** cuando alguien comenta en mi post?
2. ¿Mostrar **solo comentarios de seguidores** o todos públicos?
3. ¿Límite de menciones en comentarios?  
4. ¿Moderación automática de comentarios (profanity filter)?
5. ¿Los desafíos de facciones son semanales o ad-hoc?
6. ¿Premios reales (badges, roles) para ganadores de desafíos?

---

**Autor:** GitHub Copilot  
**Proyecto:** Academia Hachimaki 2026  
**Sistema:** Gamificación + Social Learning
