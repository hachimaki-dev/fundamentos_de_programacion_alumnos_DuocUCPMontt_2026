// ═══════════════════════════════════════════════════════════════
//  ✏️ Profile Editor — Vue App
// ═══════════════════════════════════════════════════════════════

const { createApp } = Vue;

createApp({
  data() {
    return {
      loading: true,
      isAuthenticated: false,
      saving: false,
      dragOver: false,
      activeTab: 'basic',

      currentUser: null,
      originalProfile: null,

      // Form data
      form: {
        full_name: '',
        nickname: '',
        section: '',
        birth_date: '',
        bio: '',
        avatar_custom_url: null,
        avatar_id: 'python-01',
        avatar_source: 'catalog', // 'catalog' | 'custom'
        visibility: 'public',
        social_links: {
          github: '',
          twitter: '',
          youtube: '',
          portfolio: ''
        },
        custom_html: '',
        custom_css: '',
        myspace_theme: 'default'
      },

      // Validation
      nicknameError: '',
      uploadError: '',
      uploadSuccess: '',
      uploading: false,

      // UI
      toast: {
        show: false,
        message: '',
        type: 'success' // 'success' | 'error'
      },

      // Analytics
      followerCount: 0,
      profileCompleteness: 0,

      // Avatar catalog
      avatarCatalog: SupabaseManager.getAvatarCatalog()
    };
  },

  computed: {
    currentAvatarUrl() {
      if (!this.form.avatar_source) return this.avatarCatalog[0].src;

      if (this.form.avatar_source === 'custom' && this.form.avatar_custom_url) {
        return this.form.avatar_custom_url;
      }

      // Fallback a catalog
      const found = this.avatarCatalog.find(a => a.id === this.form.avatar_id);
      return found ? found.src : this.avatarCatalog[0].src;
    },

    visibilityLabel() {
      const labels = {
        'public': '🌍 Público',
        'followers_only': '👥 Seguidores',
        'private': '🔒 Privado'
      };
      return labels[this.form.visibility] || 'Público';
    }
  },

  watch: {
    // Recalcular progress cuando cambie el form
    form: {
      handler() {
        this.calculateProfileCompleteness();
      },
      deep: true
    }
  },

  async mounted() {
    // Verificar autenticación
    this.currentUser = await SupabaseManager.getUser();

    if (!this.currentUser) {
      this.isAuthenticated = false;
      this.loading = false;
      return;
    }

    this.isAuthenticated = true;

    // Cargar perfil actual
    await this.loadProfile();
    this.loading = false;
  },

  methods: {
    // ═══ PROFILE LOADING & SAVING ═══

    async loadProfile() {
      try {
        const { profile, error } = await SupabaseManager.getProfile();

        if (error) {
          console.error('Error loading profile:', error);
          this.showToast('Error al cargar tu perfil', 'error');
          return;
        }

        this.originalProfile = JSON.parse(JSON.stringify(profile));

        // Mapear al formulario
        this.form.full_name = profile.full_name || '';
        this.form.nickname = profile.nickname || '';
        this.form.section = profile.section || '';
        this.form.birth_date = profile.birth_date || '';
        this.form.bio = profile.bio || '';
        this.form.avatar_source = profile.avatar_source || 'catalog';
        this.form.avatar_custom_url = profile.avatar_custom_url || null;
        this.form.avatar_id = profile.avatar_id || 'python-01';
        this.form.visibility = profile.visibility || 'public';
        this.form.custom_html = profile.custom_html || '';
        this.form.custom_css = profile.custom_css || '';
        this.form.myspace_theme = profile.myspace_theme || 'default';

        // Social links
        if (profile.social_links && typeof profile.social_links === 'object') {
          this.form.social_links = {
            github: profile.social_links.github || '',
            twitter: profile.social_links.twitter || '',
            youtube: profile.social_links.youtube || '',
            portfolio: profile.social_links.portfolio || ''
          };
        }

        // Cargar follower count
        await this.loadFollowerCount();

      } catch (err) {
        console.error('Unexpected error loading profile:', err);
        this.showToast('Error inesperado', 'error');
      }
    },

    async loadFollowerCount() {
      try {
        const client = SupabaseManager.getClient();
        const { count, error } = await client
          .from('profile_followers')
          .select('*', { count: 'exact', head: true })
          .eq('following_id', this.currentUser.id);

        if (!error) {
          this.followerCount = count || 0;
        }
      } catch (err) {
        console.error('Error loading follower count:', err);
      }
    },

    async saveProfile() {
      // Validaciones básicas
      if (!this.form.nickname || this.form.nickname.length < 3) {
        this.showToast('El nickname debe tener al menos 3 caracteres', 'error');
        return;
      }

      if (this.nicknameError) {
        this.showToast(this.nicknameError, 'error');
        return;
      }

      this.saving = true;

      try {
        const updates = {
          full_name: this.form.full_name,
          nickname: this.form.nickname,
          section: this.form.section,
          birth_date: this.form.birth_date || null,
          bio: this.form.bio,
          avatar_source: this.form.avatar_source,
          avatar_custom_url: this.form.avatar_custom_url,
          avatar_id: this.form.avatar_id,
          visibility: this.form.visibility,
          social_links: this.form.social_links,
          custom_html: DOMPurify.sanitize(this.form.custom_html, {
            ALLOWED_TAGS: ['h1', 'h2', 'h3', 'p', 'a', 'img', 'div', 'span', 'strong', 'em', 'u', 'br', 'hr', 'ul', 'ol', 'li', 'iframe'],
            ALLOWED_ATTR: ['href', 'src', 'alt', 'title', 'class', 'id', 'allow', 'allowfullscreen', 'frameborder', 'style'],
            KEEP_CONTENT: true
          }),
          custom_css: this.form.custom_css, // CSS se sanitiza en el display, no aquí
          myspace_theme: this.form.myspace_theme,
          profile_completed: true
        };

        const { data, error } = await SupabaseManager.updateProfile(updates);

        if (error) {
          console.error('Update error:', error);
          this.showToast('Error al guardar: ' + error.message, 'error');
          this.saving = false;
          return;
        }

        // Success
        this.originalProfile = JSON.parse(JSON.stringify(this.form));
        this.showToast('✅ Perfil guardado correctamente', 'success');
        this.saving = false;

        // Redirigir a perfil después de 1.5s
        setTimeout(() => {
          window.location.href = `profile.html?nickname=${this.form.nickname}`;
        }, 1500);

      } catch (err) {
        console.error('Unexpected error:', err);
        this.showToast('Error inesperado al guardar', 'error');
        this.saving = false;
      }
    },

    // ═══ AVATAR UPLOAD ═══

    handleFileSelect(event) {
      const file = event.target.files?.[0];
      if (file) {
        this.uploadAvatar(file);
      }
    },

    handleDrop(event) {
      const file = event.dataTransfer?.files?.[0];
      this.dragOver = false;
      if (file && file.type.startsWith('image/')) {
        this.uploadAvatar(file);
      } else {
        this.uploadError = 'Por favor sube un archivo de imagen válido';
      }
    },

    async uploadAvatar(file) {
      this.uploadError = '';
      this.uploadSuccess = '';

      // Validaciones
      if (!file.type.startsWith('image/')) {
        this.uploadError = 'El archivo debe ser una imagen (JPG, PNG, WebP, GIF)';
        return;
      }

      if (file.size > 5 * 1024 * 1024) {
        this.uploadError = 'La imagen debe ser menor a 5MB';
        return;
      }

      this.uploading = true;

      try {
        const ext = file.name.split('.').pop() || 'jpg';
        const timestamp = Date.now();
        const filename = `${this.currentUser.id}/${timestamp}.${ext}`;

        const client = SupabaseManager.getClient();

        // Subir a Storage
        const { error: uploadError } = await client.storage
          .from('profile-avatars')
          .upload(filename, file, { upsert: true });

        if (uploadError) {
          console.error('Storage upload error:', uploadError);
          this.uploadError = 'Error al subir la imagen: ' + uploadError.message;
          this.uploading = false;
          return;
        }

        // Obtener URL pública
        const { data } = client.storage
          .from('profile-avatars')
          .getPublicUrl(filename);

        const publicUrl = data.publicUrl;

        // Actualizar form
        this.form.avatar_custom_url = publicUrl;
        this.form.avatar_source = 'custom';

        // Persistir inmediatamente en la DB para evitar confusiones
        const { error: dbError } = await client.from('profiles').update({
            avatar_source: 'custom',
            avatar_custom_url: publicUrl,
            updated_at: new Date().toISOString()
        }).eq('id', this.currentUser.id);

        if (dbError) {
            console.error('Error updating profile with new avatar:', dbError);
            this.uploadError = 'Imagen subida, pero no se pudo actualizar el perfil: ' + dbError.message;
            this.uploading = false;
            return;
        }

        this.uploadSuccess = '✅ Imagen subida y guardada correctamente';
        this.uploading = false;

        // Actualizar originalProfile para que no pida confirmación al salir
        if (this.originalProfile) {
            this.originalProfile.avatar_source = 'custom';
            this.originalProfile.avatar_custom_url = publicUrl;
        }

      } catch (err) {
        console.error('Avatar upload error:', err);
        this.uploadError = 'Error al subir la imagen';
        this.uploading = false;
      }
    },

    async revertToDefaultAvatar() {
      this.form.avatar_source = 'catalog';
      this.form.avatar_custom_url = null;

      const client = SupabaseManager.getClient();
      await client.from('profiles').update({
          avatar_source: 'catalog',
          avatar_custom_url: null,
          updated_at: new Date().toISOString()
      }).eq('id', this.currentUser.id);

      this.uploadSuccess = '↩️ Avatar revertido al catálogo';
      setTimeout(() => {
        this.uploadSuccess = '';
      }, 3000);
      
      if (this.originalProfile) {
          this.originalProfile.avatar_source = 'catalog';
          this.originalProfile.avatar_custom_url = null;
      }
    },

    // ═══ VALIDATION ═══

    async validateNickname() {
      const nickname = this.form.nickname.trim();
      this.nicknameError = '';

      // Validación básica
      if (!nickname) {
        return;
      }

      if (nickname.length < 3 || nickname.length > 30) {
        this.nicknameError = 'Debe tener entre 3 y 30 caracteres';
        return;
      }

      if (!/^[a-zA-Z0-9_]+$/.test(nickname)) {
        this.nicknameError = 'Solo letras, números y guiones bajos (_)';
        return;
      }

      // Si no ha cambiado, no validar
      if (nickname === this.originalProfile?.nickname) {
        return;
      }

      // Validar uniqueness
      try {
        const isTaken = await SupabaseManager.isNicknameTaken(nickname);
        if (isTaken) {
          this.nicknameError = 'Este nickname ya está en use';
        }
      } catch (err) {
        console.error('Error validating nickname:', err);
      }
    },

    calculateProfileCompleteness() {
      let score = 0;

      // Avatar (10%)
      if (this.form.avatar_source === 'custom' || this.form.avatar_custom_url) {
        score += 10;
      } else if (this.originalProfile?.avatar_id) {
        score += 5;
      }

      // Full name (10%)
      if (this.form.full_name) score += 10;

      // Bio (10%)
      if (this.form.bio && this.form.bio.length > 10) score += 10;

      // Nickname (15%)
      if (this.form.nickname && !this.nicknameError) score += 15;

      // Section (10%)
      if (this.form.section) score += 10;

      // Birth date (10%)
      if (this.form.birth_date) score += 10;

      // Social links (25% total)
      const socialCount = Object.values(this.form.social_links).filter(v => v).length;
      score += Math.min(25, socialCount * 6);

      // Custom MySpace (10% extra)
      if ((this.form.custom_html && this.form.custom_html.length > 20) ||
        (this.form.custom_css && this.form.custom_css.length > 20)) {
        score += 5;
      }

      this.profileCompleteness = Math.min(100, score);
    },

    // ═══ UI HELPERS ═══

    discardChanges() {
      if (JSON.stringify(this.form) === JSON.stringify(this.originalProfile)) {
        window.history.back();
        return;
      }

      if (confirm('¿Descartar cambios sin guardar?')) {
        this.form = JSON.parse(JSON.stringify(this.originalProfile));
        window.history.back();
      }
    },

    showToast(message, type = 'success') {
      this.toast.message = message;
      this.toast.type = type;
      this.toast.show = true;

      setTimeout(() => {
        this.toast.show = false;
      }, 3000);
    }
  }
}).mount('#app');

// ═══════════════════════════════════════════════════════════════
// Handlers globales
// ═══════════════════════════════════════════════════════════════

async function handleLogout() {
  const { error } = await SupabaseManager.signOut();
  if (!error) {
    window.location.href = '../index.html';
  }
}
