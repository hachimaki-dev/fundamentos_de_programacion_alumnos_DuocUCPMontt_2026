// ═══════════════════════════════════════════════════════════════
//  🔗 USER NAVIGATION SYSTEM — códigos listos para implementar
// ═══════════════════════════════════════════════════════════════

// ──────────────────────────────────────────────────────────────
// 1️⃣  USER CARD HANDLER (copiar a js/user-navigation.js)
// ──────────────────────────────────────────────────────────────

/**
 * Sistema centralizado para navegación a perfiles de usuarios
 * Uso: UserNav.makeClickable(element, userId);
 */
class UserNavigation {
  /**
   * Navega al perfil de un usuario
   * @param {string} userId - UUID del usuario
   * @param {string} fromPage - (Opcional) Página de origen para breadcrumb
   */
  static navigateToProfile(userId, fromPage = '') {
    const params = new URLSearchParams();
    params.set('user', userId);
    if (fromPage) params.set('from', fromPage);
    window.location.href = `profile.html?${params.toString()}`;
  }

  /**
   * Hace un elemento clickable para navegar al perfil
   * @param {HTMLElement} element - El elemento (avatar, nombre, etc.)
   * @param {string} userId - UUID del usuario
   * @param {string} fromPage - (Opcional) Página de origen
   */
  static makeClickable(element, userId, fromPage = '') {
    if (!element) return;
    element.style.cursor = 'pointer';
    element.style.transition = 'opacity 0.2s ease';
    
    element.addEventListener('mouseenter', () => {
      element.style.opacity = '0.75';
    });
    element.addEventListener('mouseleave', () => {
      element.style.opacity = '1';
    });
    
    element.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      this.navigateToProfile(userId, fromPage);
    });
  }

  /**
   * Hace múltiples avatares clickables en un contenedor
   * @param {string} containerSelector - CSS selector del contenedor
   * @param {string} avatarSelector - CSS selector de los avatares
   * @param {function} userIdCallback - Función que extrae userId del elemento
   * @param {string} fromPage - Página de origen
   */
  static makeContainerClickable(
    containerSelector,
    avatarSelector,
    userIdCallback,
    fromPage = ''
  ) {
    const container = document.querySelector(containerSelector);
    if (!container) return;

    container.querySelectorAll(avatarSelector).forEach(avatar => {
      const userId = userIdCallback(avatar);
      if (userId) {
        this.makeClickable(avatar, userId, fromPage);
      }
    });
  }
}

// Alias corto
const UserNav = UserNavigation;


// ──────────────────────────────────────────────────────────────
// 2️⃣  DASHBOARD-APP.JS CAMBIOS
// ──────────────────────────────────────────────────────────────
/*
PASO 1: Agregar a mounted() después de this.loading = false
*/

async mounted() {
  // ... código existente ...
  this.loading = false;
  
  // 🆕 Habilitar navegación a perfiles en feed
  this.$nextTick(() => {
    this.setupProfileNavigation();
  });
}

methods: {
  // 🆕 Nuevo método
  setupProfileNavigation() {
    // Feed posts - Avatar del autor
    document.querySelectorAll('[data-user-avatar]').forEach(avatar => {
      const userId = avatar.getAttribute('data-user-id');
      UserNav.makeClickable(avatar, userId, 'dashboard');
    });

    // Comentarios - Avatar del comentarista
    document.querySelectorAll('[data-comment-avatar]').forEach(avatar => {
      const userId = avatar.getAttribute('data-user-id');
      UserNav.makeClickable(avatar, userId, 'dashboard');
    });

    // Top comentarios preview
    document.querySelectorAll('[data-top-comment-avatar]').forEach(avatar => {
      const userId = avatar.getAttribute('data-user-id');
      UserNav.makeClickable(avatar, userId, 'dashboard');
    });
  },
  
  // ... resto de métodos existentes ...
}

/*
PASO 2: En la sección del feed HTML, agregar atributos
OLD:
<div class="sd-card">
  <div style="display:flex">
    <img :src="getAvatar(item.author)" />

NEW:
<div class="sd-card">
  <div style="display:flex">
    <img 
      :src="getAvatar(item.author)" 
      :data-user-id="item.author.id"
      data-user-avatar
    />
*/


// ──────────────────────────────────────────────────────────────
// 3️⃣  FACTIONS-APP.JS Y FACTIONS.HTML
// ──────────────────────────────────────────────────────────────

/*
PASO 1: En factions-app.js mounted()
*/

async mounted() {
  const profile = await SupabaseManager.requireProfile('setup-profile.html');
  if (!profile) return;
  this.profile = profile;

  const client = SupabaseManager.getClient();

  await Promise.allSettled([
    this.loadFactions(client),
    this.loadRecentActivity(client)
  ]);

  this.loading = false;
  
  // 🆕 Habilitar navegación
  this.$nextTick(() => {
    this.setupProfileNavigation();
  });
}

methods: {
  // 🆕 Nuevo método
  setupProfileNavigation() {
    // Miembros en grid de facciones
    document.querySelectorAll('[data-faction-member]').forEach(avatar => {
      const userId = avatar.getAttribute('data-user-id');
      UserNav.makeClickable(avatar, userId, 'factions');
    });
  },
  
  // ... resto de métodos ...
}

/*
PASO 2: En factions.html, cambiar la sección de miembros:

OLD:
<div v-for="m in f.members" :key="m.id" class="fh-member">
  <img :src="getAvatar(m)" />

NEW:
<div v-for="m in f.members" :key="m.id" class="fh-member">
  <img 
    :src="getAvatar(m)" 
    :data-user-id="m.id"
    data-faction-member
  />
*/


// ──────────────────────────────────────────────────────────════════════════════════════════════
//  💬 COMENTARIOS EN FEED — Cambios para dashboard-app.js y dashboard.html
// ═══════════════════════════════════════════════════════════════════════════════════════════════

/*
PASO 1: En data() añadir nuevas propiedades
*/

data() {
  return {
    // ... propiedades existentes ...
    
    // 🆕 Para comentarios
    expandedComments: {}, // { [item._key]: boolean }
    newCommentText: {}, // { [item._key]: string }
    loadingSubmit: {}, // { [item._key]: boolean }
    comments: {}, // { [item._key]: [] }
  };
}

/*
PASO 2: En loadFeed() después de cargar comentarios
*/

async loadFeed(client, profile) {
  this.feedItems = [];
  
  try {
    // Cargar diarios públicos
    const { data: entries } = await client
      .from('diary_entries')
      .select('*')
      .eq('is_public', true)
      .order('created_at', { ascending: false })
      .limit(20);

    if (entries && entries.length) {
      // 🆕 Load comments para estos entries
      let commentsMap = {};
      try {
        const entryIds = entries.map(e => e.id);
        const { data: comments } = await client
          .from('diary_comments')
          .select('*, profiles(id, nickname, avatar_id, avatar_source, avatar_custom_url)')
          .in('entry_id', entryIds)
          .order('created_at', { ascending: false });

        if (comments) {
          comments.forEach(c => {
            if (!commentsMap[c.entry_id]) commentsMap[c.entry_id] = [];
            commentsMap[c.entry_id].push(c);
          });
        }
      } catch (e) { console.error('Error loading comments:', e); }

      // Cargar autor de cada entry
      const authorIds = [...new Set(entries.map(e => e.user_id))];
      const { data: authors } = await client
        .from('profiles')
        .select('*')
        .in('id', authorIds);

      const authorsMap = {};
      if (authors) {
        authors.forEach(a => authorsMap[a.id] = a);
      }

      entries.forEach(entry => {
        const entryComments = commentsMap[entry.id] || [];
        this.feedItems.push({
          id: entry.id,
          _key: entry.id,
          author: authorsMap[entry.user_id] || { id: entry.user_id },
          title: entry.title,
          content: entry.content,
          created_at: entry.created_at,
          is_public: entry.is_public,
          _comments: entryComments,
          _commentsCount: entryComments.length,
          _topComment: entryComments[0] || null,
        });
      });
    }
  } catch (e) {
    console.error('Error loading feed:', e);
  }
}

/*
PASO 3: Agregar nuevos métodos
*/

methods: {
  // 🆕 Alternar expansión de comentarios
  toggleCommentForm(itemKey) {
    this.expandedComments[itemKey] = !this.expandedComments[itemKey];
    if (this.expandedComments[itemKey]) {
      this.$nextTick(() => {
        const input = document.querySelector(`[data-comment-input="${itemKey}"]`);
        if (input) input.focus();
      });
    }
  },

  // 🆕 Enviar nuevo comentario
  async submitComment(item) {
    const text = this.newCommentText[item._key];
    if (!text?.trim() || text.length > 500) return;

    this.loadingSubmit[item._key] = true;

    try {
      const { data, error } = await SupabaseManager.getClient()
        .from('diary_comments')
        .insert([{
          entry_id: item.id,
          user_id: this.profile.id,
          content: text,
        }])
        .select('*, profiles(id, nickname, avatar_id, avatar_source, avatar_custom_url)')
        .single();

      if (error) throw error;

      // Actualizar feed
      if (!item._comments) item._comments = [];
      item._comments.unshift(data);
      item._commentsCount = item._comments.length;
      
      // Limpiar input
      this.newCommentText[item._key] = '';
      
      // Mostrar feedback
      console.log('✅ Comentario enviado');
    } catch (e) {
      console.error('❌ Error enviando comentario:', e);
      alert('Error al enviar comentario. Intenta de nuevo.');
    } finally {
      this.loadingSubmit[item._key] = false;
    }
  },

  // 🆕 Método helper: Si la entrada excede max chars
  getRemainingChars(itemKey) {
    const text = this.newCommentText[itemKey] || '';
    return Math.max(0, 500 - text.length);
  },

  // ... resto de métodos ...
}

/*
PASO 4: En dashboard.html, reemplazar la sección de comentarios

OLD:
<button class="sd-action">💬 {{ item._commentsCount || 0 }} comentarios</button>
<!-- Inline comment preview -->
<div v-if="item._topComment" class="sd-inline-comment">
  ...
</div>

NEW:
*/
<div style="display:flex;gap:8px;margin-top:12px">
  <button 
    class="sd-action"
    @click="toggleCommentForm(item._key)"
  >
    💬 {{ item._commentsCount || 0 }}
  </button>
</div>

<!-- Comentarios expandidos (si está abierto) -->
<div v-if="expandedComments[item._key]" style="margin-top:12px;border-top:1px solid var(--t-border);padding-top:12px">
  
  <!-- Lista de comentarios -->
  <div v-if="item._comments && item._comments.length" style="margin-bottom:12px;max-height:300px;overflow-y:auto">
    <div 
      v-for="comment in item._comments" 
      :key="comment.id"
      class="sd-inline-comment"
      style="margin-bottom:10px"
    >
      <img 
        :src="getAvatar(comment.profiles)"
        :data-user-id="comment.profiles?.id"
        data-comment-avatar
      />
      <div class="sd-comment-bubble">
        <span class="sd-comment-author">{{ comment.profiles?.nickname }}</span>
        <span class="sd-comment-text">{{ comment.content }}</span>
        <div style="font-size:9px;color:var(--t-text-muted);margin-top:2px">
          {{ new Date(comment.created_at).toLocaleDateString() }}
        </div>
      </div>
    </div>
  </div>

  <!-- Form para nuevo comentario -->
  <div style="display:flex;gap:8px">
    <img :src="avatarSrc" style="width:32px;height:32px;border-radius:50%" />
    <div style="flex:1">
      <textarea
        v-model="newCommentText[item._key]"
        :data-comment-input="item._key"
        rows="2"
        placeholder="Añade un comentario..."
        maxlength="500"
        style="width:100%;padding:8px;border:1px solid var(--t-border);border-radius:4px;font-size:12px;font-family:inherit;resize:vertical"
      ></textarea>
      <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:10px;color:var(--t-text-muted)">
        <span>{{ getRemainingChars(item._key) }} caracteres</span>
        <button
          @click="submitComment(item)"
          :disabled="!newCommentText[item._key]?.trim() || loadingSubmit[item._key]"
          style="padding:4px 12px;background:var(--t-accent);color:white;border:none;border-radius:4px;font-size:11px;cursor:pointer;opacity:1"
          :style="{opacity: newCommentText[item._key]?.trim() ? 1 : 0.5}"
        >
          {{ loadingSubmit[item._key] ? '⏳...' : 'Enviar' }}
        </button>
      </div>
    </div>
  </div>
</div>

/* Si NO está expandido, mostrar preview del top comment */
<div v-else-if="item._topComment" class="sd-inline-comment" style="margin-top:12px">
  <img :src="getAvatar(item._topComment.profiles)" />
  <div class="sd-comment-bubble">
    <span class="sd-comment-author">{{ item._topComment.profiles?.nickname }} </span>
    <span class="sd-comment-text">{{ item._topComment.content }}</span>
  </div>
</div>


// ═══════════════════════════════════════════════════════════════
//  TESTING Y VALIDACIÓN
// ═══════════════════════════════════════════════════════════════

/*
Checklist de validación:
□ Comentarios se guardan en DB
□ Comentarios cargan al refrescar página
□ Se muestra count correcto
□ Avatar clickable navega a perfil
□ Validación de largo (2-500 chars)
□ Sanitización de XSS (DOMPurify)
□ Mobile responsive (textarea adapta altura)
□ Perfiles de otros usuarios son visitables
□ Volver atrás desde profile muestra breadcrumb (opcional)
*/
