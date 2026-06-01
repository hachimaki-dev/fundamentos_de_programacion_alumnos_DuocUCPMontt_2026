// ═══════════════════════════════════════════════════════════════
//  ⚔️ Sala de Facciones — Vue App
// ═══════════════════════════════════════════════════════════════

const { createApp } = Vue;

createApp({
  data() {
    return {
      loading: true,
      profile: null,
      factions: [],
      rawVictories: [],
      avatarCatalog: SupabaseManager.getAvatarCatalog(),
      
      // 🔄 FASE 2: Desafíos Intra-Facción
      activeTab: 'overview', // 'overview', 'challenges', 'wall'
      challenges: [],
      newChallenge: {
        title: '',
        description: '',
        target_xp: 500,
        days: 3,
      },
      showNewChallengeForm: false,
      
      // 🔄 FASE 3: Mural de Facción
      wallMessages: [],
      newWallMessage: '',
      loadingWall: false,
      loadingChallenges: false,
    };
  },

  computed: {
    myFaction() {
      if (!this.profile || !this.profile.faction_id) return null;
      return this.factions.find(f => f.id === this.profile.faction_id) || null;
    },
    recentVictories() {
      if (!this.rawVictories) return [];
      return this.rawVictories.map(v => {
        const faction = this.factions.find(f => f.id === v.faction_id);
        return {
          ...v,
          factionName: faction ? faction.faction_name : 'Facción Desconocida',
          timeAgo: this.formatTimeAgo(v.createdAt)
        };
      }).slice(0, 5); // top 5 recent
    }
  },

  async mounted() {
    const profile = await SupabaseManager.requireProfile('setup-profile.html');
    if (!profile) return;
    this.profile = profile;

    const client = SupabaseManager.getClient();

    // 🔧 Promise with timeout to prevent infinite loading
    const timeoutPromise = new Promise((_, reject) => 
      setTimeout(() => reject(new Error('Load timeout')), 10000)
    );

    try {
      await Promise.race([
        Promise.allSettled([
          this.loadFactions(client),
          this.loadRecentActivity(client),
          this.loadChallenges(client),
          this.loadWallMessages(client)
        ]),
        timeoutPromise
      ]);
    } catch (e) {
      console.warn('[Factions] Loading timeout or error:', e);
      // Continue anyway - show what we have
    }

    this.loading = false;

    // 🔗 Setup profile navigation
    this.$nextTick(() => {
      this.setupProfileNavigation();
    });

    // 🔄 Setup real-time updates
    this.$nextTick(() => {
      this.setupRealtimeUpdates(client);
    });
  },

  methods: {
    // 🔗 Enable profile navigation on faction member avatars
    setupProfileNavigation() {
      document.querySelectorAll('[data-faction-member]').forEach(avatar => {
        const userId = avatar.getAttribute('data-user-id');
        if (userId) {
          UserNav.makeClickable(avatar, userId, 'factions');
        }
      });
    },
    async loadFactions(client) {
      try {
        // Fetch all factions
        const { data: factionsData } = await client
          .from('factions')
          .select('*')
          .order('total_xp', { ascending: false });

        // Fetch all profiles
        const { data: profilesData } = await client
          .from('profiles')
          .select('id, nickname, avatar_id, avatar_source, avatar_custom_url, xp, level, github_username, faction_id')
          .order('xp', { ascending: false });

        if (factionsData) {
          this.factions = factionsData.map(f => {
            const members = (profilesData || []).filter(p => p.faction_id === f.id);
            return {
              ...f,
              members: members
            };
          });
        }
      } catch (e) {
        console.error('Error loading factions', e);
      }
    },

    async loadRecentActivity(client) {
      // Get recent github syncs with graceful fallback
      try {
        // Try to use the view first (faster, better RLS)
        const { data, error } = await client
          .from('faction_activity_feed')
          .select('*')
          .order('created_at', { ascending: false })
          .limit(10);
        
        if (!error && data && data.length) {
          this.rawVictories = data.map(row => ({
            id: 'gh-' + row.id,
            faction_id: row.faction_id,
            xp: row.xp_awarded,
            reason: row.activity_text,
            createdAt: new Date(row.created_at),
            nickname: row.nickname,
            avatar_id: row.avatar_id
          }));
          return;
        }
      } catch (e) {
        console.warn('[Factions] faction_activity_feed not available, fallback to direct query', e);
      }

      // Fallback: Query github_sync_history directly with proper joins
      try {
        const { data } = await client
          .from('github_sync_history')
          .select('id, user_id, repo_name, xp_awarded, created_at, profiles:user_id(faction_id, nickname, avatar_id)')
          .order('created_at', { ascending: false })
          .limit(10);
          
        if (data && data.length) {
          this.rawVictories = data.map(row => ({
            id: 'gh-' + row.id,
            faction_id: row.profiles?.faction_id,
            xp: row.xp_awarded,
            reason: 'Commits en ' + row.repo_name,
            createdAt: new Date(row.created_at),
            nickname: row.profiles?.nickname
          })).filter(v => v.faction_id); // Solo mostrar si tiene facción
        }
      } catch (e) {
        console.error('[Factions] Error loading recent activity', e);
        // Silently fail - show empty activity
        this.rawVictories = [];
      }
    },

    // Resolves raw victories into renderable objects
    // MOVIDO A COMPUTED

    getAvatar(profileOrId) {
      if (typeof profileOrId === 'object' && profileOrId !== null) {
        if (profileOrId.avatar_source === 'custom' && profileOrId.avatar_custom_url) {
          return profileOrId.avatar_custom_url;
        }
        profileOrId = profileOrId.avatar_id;
      }
      const av = this.avatarCatalog.find(a => a.id === profileOrId);
      return av ? av.src : this.avatarCatalog[0].src;
    },

    getXpPercent(xp) {
      if (!this.factions.length) return 0;
      const max = Math.max(...this.factions.map(f => f.total_xp || 0), 1);
      return Math.max(5, Math.round(((xp || 0) / max) * 100)); // min 5% for visual bar
    },

    getFactionRank(factionId) {
      const index = this.factions.findIndex(f => f.id === factionId);
      return index !== -1 ? index + 1 : '-';
    },

    getFactionColorByName(name) {
      if (!name) return 'var(--t-accent)';
      const lower = name.toLowerCase();
      if (lower.includes('fuego')) return '#D4537E'; // Red/Pink
      if (lower.includes('agua') || lower.includes('hielo')) return '#457b9d'; // Blue
      if (lower.includes('tierra') || lower.includes('eléctrico') || lower.includes('bits')) return '#1D9E75'; // Green
      return 'var(--t-accent)';
    },

    getFactionBadge(name) {
      if (!name) return '../assets/factions/fire_badge.png';
      const lower = name.toLowerCase();
      if (lower.includes('fuego')) return '../assets/factions/fire_badge.png';
      if (lower.includes('agua') || lower.includes('hielo')) return '../assets/factions/water_badge.png';
      if (lower.includes('tierra') || lower.includes('eléctrico') || lower.includes('bits')) return '../assets/factions/earth_badge.png';
      return '../assets/factions/fire_badge.png';
    },

    formatTimeAgo(dateObj) {
      const now = new Date();
      const diffMs = now - dateObj;
      const mins = Math.floor(diffMs / 60000);
      if (mins < 1) return 'ahora';
      if (mins < 60) return `${mins} min`;
      const hours = Math.floor(mins / 60);
      if (hours < 24) return `${hours} h`;
      const days = Math.floor(hours / 24);
      return `${days} d`;
    },

    // 🔄 FASE 1: Real-time Dashboard Updates
    setupRealtimeUpdates(client) {
      if (!client) return;

      // Subscribe to faction XP changes
      const subscription = client
        .channel('public:factions')
        .on(
          'postgres_changes',
          { event: 'UPDATE', schema: 'public', table: 'factions' },
          (payload) => {
            const idx = this.factions.findIndex(f => f.id === payload.new.id);
            if (idx !== -1) {
              this.$set(this.factions, idx, { 
                ...this.factions[idx], 
                total_xp: payload.new.total_xp 
              });
            }
          }
        )
        .subscribe();

      // Subscribe to new github syncs for activity feed
      client
        .channel('public:github_sync_history')
        .on(
          'postgres_changes',
          { event: 'INSERT', schema: 'public', table: 'github_sync_history' },
          (payload) => {
            // Reload recent activity to show new entries
            this.loadRecentActivity(client);
          }
        )
        .subscribe();
    },

    // 🔧 FASE 2: Desafíos Intra-Facción
    async loadChallenges(client) {
      if (!this.myFaction) return;
      
      this.loadingChallenges = true;
      try {
        const { data, error } = await client
          .from('faction_challenges_with_progress')
          .select('*')
          .eq('faction_id', this.myFaction.id)
          .order('created_at', { ascending: false });
        
        if (!error && data) {
          this.challenges = data;
        }
      } catch (e) {
        console.error('[Factions] Error loading challenges', e);
      } finally {
        this.loadingChallenges = false;
      }
    },

    async submitChallenge(client) {
      if (!this.myFaction || !this.newChallenge.title.trim()) {
        alert('Título requerido');
        return;
      }

      try {
        const deadline = new Date();
        deadline.setDate(deadline.getDate() + this.newChallenge.days);

        const { error } = await client.from('faction_challenges').insert([{
          faction_id: this.myFaction.id,
          created_by: this.profile.id,
          title: this.newChallenge.title,
          description: this.newChallenge.description,
          target_xp: parseInt(this.newChallenge.target_xp),
          deadline: deadline.toISOString(),
          reward_xp: Math.max(50, Math.floor(parseInt(this.newChallenge.target_xp) / 10)),
        }]);

        if (error) throw error;

        // Reset form and reload
        this.newChallenge = { title: '', description: '', target_xp: 500, days: 3 };
        this.showNewChallengeForm = false;
        await this.loadChallenges(client);
      } catch (e) {
        console.error('[Factions] Error creating challenge', e);
        alert('Error al crear desafío');
      }
    },

    // 🔧 FASE 3: Mural de Facción
    async loadWallMessages(client) {
      if (!this.myFaction) return;
      
      this.loadingWall = true;
      try {
        const { data, error } = await client
          .from('faction_wall_feed')
          .select('*')
          .eq('faction_id', this.myFaction.id)
          .order('created_at', { ascending: false })
          .limit(50);
        
        if (!error && data) {
          this.wallMessages = data;
        }
      } catch (e) {
        console.error('[Factions] Error loading wall messages', e);
      } finally {
        this.loadingWall = false;
      }
    },

    async submitWallMessage(client) {
      if (!this.myFaction || !this.newWallMessage.trim()) {
        alert('Mensaje requerido');
        return;
      }

      if (this.newWallMessage.trim().length > 500) {
        alert('Máximo 500 caracteres');
        return;
      }

      try {
        const { error } = await client.from('faction_wall').insert([{
          faction_id: this.myFaction.id,
          user_id: this.profile.id,
          message: this.newWallMessage.trim(),
        }]);

        if (error) throw error;

        // Reset and reload
        this.newWallMessage = '';
        await this.loadWallMessages(client);
      } catch (e) {
        console.error('[Factions] Error posting wall message', e);
        alert('Error al publicar mensaje');
      }
    },

    deleteWallMessage(client, messageId) {
      if (!confirm('¿Eliminar este mensaje?')) return;

      client.from('faction_wall')
        .delete()
        .eq('id', messageId)
        .then(() => {
          this.loadWallMessages(client);
        })
        .catch(e => {
          console.error('[Factions] Error deleting message', e);
          alert('Error al eliminar');
        });
    }
  },
}).mount('#app');
