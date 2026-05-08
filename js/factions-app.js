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

    await Promise.allSettled([
      this.loadFactions(client),
      this.loadRecentActivity(client)
    ]);

    this.loading = false;
  },

  methods: {
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
      // Get recent github syncs
      try {
        const { data } = await client
          .from('github_sync_history')
          .select('*, profiles(faction_id)')
          .order('created_at', { ascending: false })
          .limit(10);
          
        if (data && data.length) {
          const vics = [];
          for (let row of data) {
            const fId = row.profiles?.faction_id;
            if (fId) {
               // We need the faction name. For simplicity we'll resolve it via the state later.
               vics.push({
                 id: 'gh-' + row.id,
                 faction_id: fId,
                 xp: row.xp_awarded,
                 reason: 'Commits en ' + row.repo_name,
                 createdAt: new Date(row.created_at)
               });
            }
          }
          // We will resolve faction names after this.factions is loaded (since Promise.allSettled runs them concurrently, 
          // we wait until mounting finishes to render, but let's bind it safely)
          this.rawVictories = vics;
        }
      } catch (e) {
        console.error('Error loading recent activity', e);
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
    }
  },
}).mount('#app');
