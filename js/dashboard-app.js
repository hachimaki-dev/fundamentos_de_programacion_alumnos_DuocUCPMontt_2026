// ═══════════════════════════════════════════════════════════════
//  📰 Dashboard Social V2 — Vue App
// ═══════════════════════════════════════════════════════════════

const { createApp } = Vue;

createApp({
  data() {
    return {
      loading: true,
      profile: null,
      mobileView: 'feed',

      // Sidebar Left
      faction: null,
      factionRanking: [],
      allAchievements: [],
      streakDays: [],
      streakCount: 0,
      followersCount: 0,
      diaryCount: 0,
      compsJoined: 0,
      activeComps: 0,

      // Feed
      activeTab: 'foryou',
      feedItems: [],
      newPostContent: '',
      postingNew: false,

      // Sidebar Right
      activeCompData: null,
      notifications: [],
      leaderboard: [],
      suggestions: [],
      githubXp: 0,
      syncingGithub: false,
      
      // Floating Banner
      activeCompetitionsList: [],

      avatarCatalog: SupabaseManager.getAvatarCatalog(),
    };
  },

  computed: {
    avatarSrc() {
      if (!this.profile) return '';
      return this.getAvatar(this.profile.avatar_id);
    },
    nextLevelXp() {
      const lv = (this.profile?.level || 1);
      return lv * lv * 100;
    },
    xpPercent() {
      if (!this.profile) return 0;
      const xp = this.profile.xp || 0;
      const prev = Math.pow((this.profile.level || 1) - 1, 2) * 100;
      const next = this.nextLevelXp;
      if (next <= prev) return 100;
      return Math.min(100, Math.round(((xp - prev) / (next - prev)) * 100));
    },
    factionInitials() {
      if (!this.faction) return '?';
      return this.faction.faction_name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
    },
    factionXpPercent() {
      if (!this.factionRanking.length) return 50;
      const maxXp = Math.max(...this.factionRanking.map(f => f.total_xp || 0), 1);
      return Math.round(((this.faction?.total_xp || 0) / maxXp) * 100);
    },
    unlockedCount() {
      return this.allAchievements.filter(a => a.unlocked).length;
    },
    compDeadlinePercent() {
      if (!this.activeCompData?.deadline) return 0;
      const now = Date.now();
      const deadline = new Date(this.activeCompData.deadline).getTime();
      const created = new Date(this.activeCompData.created_at).getTime();
      const total = deadline - created;
      const elapsed = now - created;
      if (total <= 0) return 100;
      return Math.min(100, Math.max(0, Math.round((elapsed / total) * 100)));
    },
  },

  async mounted() {
    const profile = await SupabaseManager.requireProfile('setup-profile.html');
    if (!profile) return;
    this.profile = profile;

    const client = SupabaseManager.getClient();

    // Fire all queries in parallel
    await Promise.allSettled([
      this.loadSidebarLeft(client, profile),
      this.loadFeed(client, profile),
      this.loadSidebarRight(client, profile),
      this.loadActiveCompetitionsBanner(client),
    ]);

    this.loading = false;
  },

  methods: {
    // ─── Sidebar Left ───
    async loadSidebarLeft(client, profile) {
      // Diary count
      try {
        const { count } = await client.from('diary_entries').select('*', { count: 'exact', head: true }).eq('user_id', profile.id);
        this.diaryCount = count || 0;
      } catch (e) { /* */ }

      // Comps joined
      try {
        const { count } = await client.from('competition_participants').select('*', { count: 'exact', head: true }).eq('user_id', profile.id);
        this.compsJoined = count || 0;
      } catch (e) { /* */ }

      // Active comps count
      try {
        const { count } = await client.from('competitions').select('*', { count: 'exact', head: true }).eq('status', 'active');
        this.activeComps = count || 0;
      } catch (e) { /* */ }

      // Followers
      try {
        const { count } = await client.from('follows').select('*', { count: 'exact', head: true }).eq('following_id', profile.id);
        this.followersCount = count || 0;
      } catch (e) { /* */ }

      // Faction
      if (profile.faction_id) {
        try {
          const { data } = await client.from('factions').select('*').eq('id', profile.faction_id).single();
          if (data) this.faction = data;
        } catch (e) { /* */ }
      }

      // Faction ranking
      try {
        const { data } = await client.from('factions').select('*').order('total_xp', { ascending: false }).limit(5);
        if (data) this.factionRanking = data;
      } catch (e) { /* */ }

      // Achievements
      const emojiMap = { 'first_blood': '🩸', 'diarist': '📖', 'social_butterfly': '🦋', 'hacker_level_1': '🥷', 'hacker_level_5': '👑' };
      try {
        const { data } = await client.from('achievements_catalog').select('*');
        if (data) {
          const userAch = profile.achievements || [];
          this.allAchievements = data.map(a => ({
            ...a,
            unlocked: userAch.includes(a.id),
            icon_emoji: emojiMap[a.id] || '🏅',
          }));
        }
      } catch (e) {
        // Fallback
        const userAch = profile.achievements || [];
        this.allAchievements = Object.entries(emojiMap).map(([id, emoji]) => ({
          id, title: id.replace(/_/g, ' '), icon_emoji: emoji,
          unlocked: userAch.includes(id),
        }));
      }

      // Streak
      this.computeStreak(client, profile);
    },

    async computeStreak(client, profile) {
      const dayNames = ['D', 'L', 'M', 'M', 'J', 'V', 'S'];
      const fullNames = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
      const today = new Date();
      const todayDay = today.getDay();

      // Monday-based week
      const monday = new Date(today);
      monday.setDate(today.getDate() - ((todayDay + 6) % 7));
      monday.setHours(0, 0, 0, 0);

      let entryDays = new Set();
      try {
        const { data } = await client.from('diary_entries')
          .select('created_at')
          .eq('user_id', profile.id)
          .gte('created_at', monday.toISOString())
          .order('created_at', { ascending: true });
        if (data) {
          data.forEach(e => {
            const d = new Date(e.created_at);
            entryDays.add(d.toDateString());
          });
        }
      } catch (e) { /* */ }

      // Build 7 days starting Monday
      const days = [];
      let streak = 0;
      for (let i = 0; i < 7; i++) {
        const d = new Date(monday);
        d.setDate(monday.getDate() + i);
        const isToday = d.toDateString() === today.toDateString();
        const done = entryDays.has(d.toDateString());
        const dayIdx = d.getDay();
        days.push({
          letter: dayNames[dayIdx],
          name: fullNames[dayIdx],
          done: done && !isToday,
          today: isToday,
        });
        if (done || isToday) {
          // only count consecutive from start
        }
      }

      // Count streak (consecutive done from Monday)
      for (let i = 0; i < days.length; i++) {
        if (days[i].done || days[i].today) streak++;
        else break;
      }

      this.streakDays = days;
      this.streakCount = streak;
    },

    // ─── Feed ───
    async loadFeed(client, profile) {
      this.feedItems = [];
      const items = [];

      if (this.activeTab === 'foryou' || this.activeTab === 'blogs') {
        // Public diary entries
        let q = client.from('diary_entries')
          .select('*, profiles(nickname, avatar_id, level, section)')
          .eq('is_public', true)
          .order('created_at', { ascending: false })
          .limit(20);

        if (this.activeTab === 'section' && profile.section) {
          // Not used here but placeholder
        }

        try {
          const { data } = await q;
          if (data) {
            // Load comments for these entries
            const ids = data.map(e => e.id);
            let commentsMap = {};
            if (ids.length) {
              try {
                const { data: comments } = await client.from('diary_comments')
                  .select('*, profiles(nickname, avatar_id)')
                  .in('entry_id', ids)
                  .order('created_at', { ascending: false });
                if (comments) {
                  comments.forEach(c => {
                    if (!commentsMap[c.entry_id]) commentsMap[c.entry_id] = [];
                    commentsMap[c.entry_id].push(c);
                  });
                }
              } catch (e) { /* */ }
            }

            data.forEach(entry => {
              const entryComments = commentsMap[entry.id] || [];
              items.push({
                ...entry,
                _type: 'diary',
                _key: 'diary-' + entry.id,
                _sortDate: new Date(entry.created_at).getTime(),
                _commentsCount: entryComments.length,
                _topComment: entryComments[0] || null,
                _liked: false,
              });
            });
          }
        } catch (e) { /* */ }
      }

      if (this.activeTab === 'foryou' || this.activeTab === 'section') {
        // Section diary entries (including private ones from same section)
        if (this.activeTab === 'section' && profile.section) {
          try {
            const { data } = await client.from('diary_entries')
              .select('*, profiles!inner(nickname, avatar_id, level, section)')
              .eq('is_public', true)
              .eq('profiles.section', profile.section)
              .order('created_at', { ascending: false })
              .limit(20);
            if (data && this.activeTab === 'section') {
              data.forEach(entry => {
                if (!items.find(i => i.id === entry.id)) {
                  items.push({
                    ...entry,
                    _type: 'diary',
                    _key: 'diary-' + entry.id,
                    _sortDate: new Date(entry.created_at).getTime(),
                    _commentsCount: 0,
                    _topComment: null,
                    _liked: false,
                  });
                }
              });
            }
          } catch (e) { /* */ }
        }
      }

      if (this.activeTab === 'foryou' || this.activeTab === 'comps') {
        // Competition results
        try {
          const { data } = await client.from('competitions')
            .select('*')
            .order('created_at', { ascending: false })
            .limit(5);
          if (data) {
            for (const comp of data) {
              // Get participant count
              let pCount = 0;
              try {
                const { count } = await client.from('competition_participants')
                  .select('*', { count: 'exact', head: true })
                  .eq('competition_id', comp.id);
                pCount = count || 0;
              } catch (e) { /* */ }

              // Get top submitters by likes
              let topSubmitters = [];
              try {
                const { data: subs } = await client.from('competition_submissions')
                  .select('user_id, likes_count, profiles(nickname)')
                  .eq('competition_id', comp.id)
                  .order('likes_count', { ascending: false })
                  .limit(4);
                if (subs) {
                  topSubmitters = subs.map(s => ({
                    name: s.user_id === profile.id ? 'Tú' : (s.profiles?.nickname || '?'),
                    likes: s.likes_count || 0,
                    isYou: s.user_id === profile.id,
                  }));
                }
              } catch (e) { /* */ }

              items.push({
                ...comp,
                _type: 'comp',
                _key: 'comp-' + comp.id,
                _sortDate: new Date(comp.created_at).getTime(),
                _participantCount: pCount,
                _topSubmitters: topSubmitters,
              });
            }
          }
        } catch (e) { /* */ }
      }

      // GitHub activity (for foryou tab)
      if (this.activeTab === 'foryou') {
        try {
          const { data } = await client.from('github_sync_history')
            .select('*, profiles(nickname, avatar_id)')
            .order('created_at', { ascending: false })
            .limit(5);
          if (data) {
            data.forEach(gh => {
              items.push({
                ...gh,
                _type: 'github',
                _key: 'gh-' + gh.id,
                _sortDate: new Date(gh.created_at).getTime(),
              });
            });
          }
        } catch (e) { /* */ }
      }

      // Sort all by date desc
      items.sort((a, b) => b._sortDate - a._sortDate);
      this.feedItems = items;
    },

    // ─── Sidebar Right ───
    async loadSidebarRight(client, profile) {
      // Active competition
      try {
        const { data } = await client.from('competitions')
          .select('*')
          .eq('status', 'active')
          .order('deadline', { ascending: true })
          .limit(1)
          .single();
        if (data) this.activeCompData = data;
      } catch (e) { /* */ }

      // Leaderboard
      try {
        const { data } = await client.from('profiles')
          .select('id, nickname, avatar_id, xp, level')
          .eq('section', profile.section)
          .order('xp', { ascending: false })
          .limit(10);
        if (data) this.leaderboard = data;
      } catch (e) { /* */ }

      // Suggestions (same section, not already following)
      try {
        // Get who I follow
        const { data: myFollows } = await client.from('follows')
          .select('following_id')
          .eq('follower_id', profile.id);
        const followingIds = (myFollows || []).map(f => f.following_id);
        followingIds.push(profile.id); // exclude self

        const { data: candidates } = await client.from('profiles')
          .select('id, nickname, avatar_id, xp, level')
          .eq('section', profile.section)
          .order('xp', { ascending: false })
          .limit(20);

        if (candidates) {
          this.suggestions = candidates
            .filter(c => !followingIds.includes(c.id))
            .slice(0, 5)
            .map(c => ({ ...c, _followed: false }));
        }
      } catch (e) { /* */ }

      // Notifications (calculated)
      await this.loadNotifications(client, profile);

      // GitHub XP
      try {
        const { data } = await client.from('github_sync_history')
          .select('xp_awarded')
          .eq('user_id', profile.id);
        if (data) {
          this.githubXp = data.reduce((sum, r) => sum + (r.xp_awarded || 0), 0);
        }
      } catch (e) { /* */ }
    },

    async loadNotifications(client, profile) {
      const notifs = [];

      // Recent comments on my diary entries
      try {
        const { data: myEntries } = await client.from('diary_entries')
          .select('id').eq('user_id', profile.id);
        if (myEntries && myEntries.length) {
          const ids = myEntries.map(e => e.id);
          const { data: comments } = await client.from('diary_comments')
            .select('*, profiles(nickname)')
            .in('entry_id', ids)
            .neq('user_id', profile.id)
            .order('created_at', { ascending: false })
            .limit(3);
          if (comments) {
            comments.forEach(c => {
              notifs.push({
                _key: 'notif-comment-' + c.id,
                html: `<strong>${c.profiles?.nickname || '?'}</strong> comentó en tu diario`,
                date: c.created_at,
                read: false,
              });
            });
          }
        }
      } catch (e) { /* */ }

      // Recent follows
      try {
        const { data: follows } = await client.from('follows')
          .select('*, profiles:follower_id(nickname)')
          .eq('following_id', profile.id)
          .order('created_at', { ascending: false })
          .limit(3);
        if (follows) {
          follows.forEach(f => {
            notifs.push({
              _key: 'notif-follow-' + f.follower_id,
              html: `<strong>${f.profiles?.nickname || '?'}</strong> te empezó a seguir`,
              date: f.created_at,
              read: true,
            });
          });
        }
      } catch (e) { /* */ }

      // Recent XP from GitHub
      try {
        const { data: syncs } = await client.from('github_sync_history')
          .select('xp_awarded, created_at')
          .eq('user_id', profile.id)
          .order('created_at', { ascending: false })
          .limit(2);
        if (syncs) {
          syncs.forEach(s => {
            notifs.push({
              _key: 'notif-gh-' + s.created_at,
              html: `Ganaste <strong style="color:var(--t-correct-text)">+${s.xp_awarded} XP</strong> por tu commit`,
              date: s.created_at,
              read: true,
            });
          });
        }
      } catch (e) { /* */ }

      // Sort by date desc
      notifs.sort((a, b) => new Date(b.date) - new Date(a.date));
      this.notifications = notifs.slice(0, 6);
    },

    // ─── Floating Banner ───
    async loadActiveCompetitionsBanner(client) {
      try {
        const { data: comps } = await client.from('competitions')
          .select('*, profiles!created_by(nickname)')
          .eq('status', 'active')
          .order('deadline', { ascending: true })
          .limit(3);
          
        if (comps && comps.length > 0) {
          for (let comp of comps) {
             const { data: subs } = await client.from('competition_submissions')
               .select('user_id, profiles!user_id(avatar_id)')
               .eq('competition_id', comp.id);
               
             if (subs) {
               const uniqueAvatars = [...new Set(subs.map(s => s.profiles?.avatar_id).filter(id => id))];
               comp._submitters = uniqueAvatars;
             } else {
               comp._submitters = [];
             }
             comp._timeLeft = this.calculateTimeLeft(comp.deadline);
          }
          this.activeCompetitionsList = comps;
        }
      } catch (e) {
         console.error('Error loading active competitions banner', e);
      }
    },

    // ─── Actions ───
    switchTab(tab) {
      this.activeTab = tab;
      const client = SupabaseManager.getClient();
      this.loadFeed(client, this.profile);
    },

    async publishQuickPost() {
      const content = this.newPostContent.trim();
      if (!content) return;
      this.postingNew = true;

      try {
        const client = SupabaseManager.getClient();
        const { data, error } = await client.from('diary_entries').insert({
          user_id: this.profile.id,
          title: 'Publicación rápida',
          content: content,
          is_public: true,
          tags: ['quick-post'],
        }).select('*, profiles(nickname, avatar_id, level, section)').single();

        if (error) {
          SupabaseManager.showToast('Error al publicar: ' + error.message, 'error');
        } else {
          this.feedItems.unshift({
            ...data,
            _type: 'diary',
            _key: 'diary-' + data.id,
            _sortDate: Date.now(),
            _commentsCount: 0,
            _topComment: null,
            _liked: false,
          });
          this.newPostContent = '';
          this.diaryCount++;
          SupabaseManager.showToast('¡Publicado! +20 XP 🎉', 'success');
        }
      } catch (e) {
        SupabaseManager.showToast(e.message, 'error');
      }

      this.postingNew = false;
    },

    async toggleFollowSuggestion(user) {
      const client = SupabaseManager.getClient();
      if (user._followed) {
        await client.from('follows').delete()
          .eq('follower_id', this.profile.id)
          .eq('following_id', user.id);
        user._followed = false;
      } else {
        await client.from('follows').insert({
          follower_id: this.profile.id,
          following_id: user.id,
        });
        user._followed = true;
        SupabaseManager.showToast(`Ahora sigues a ${user.nickname}`, 'success');
      }
    },

    async syncGitHub() {
      if (!this.profile.github_username) {
        SupabaseManager.showToast('No tienes GitHub configurado en tu perfil', 'warning');
        return;
      }
      this.syncingGithub = true;
      try {
        const res = await fetch(`https://api.github.com/users/${this.profile.github_username}/events/public`);
        if (!res.ok) throw new Error('Error al conectar con GitHub.');
        const events = await res.json();
        const targetEvents = events.filter(e =>
          e.type === 'PushEvent' && e.repo && e.repo.name.toLowerCase().includes('fundamentos')
        );

        if (targetEvents.length === 0) {
          SupabaseManager.showToast('No tienes commits recientes en repos "fundamentos..."', 'info');
          this.syncingGithub = false;
          return;
        }

        const client = SupabaseManager.getClient();
        
        // Optimización: buscar todos los eventos existentes en una sola llamada
        const targetEventIds = targetEvents.map(e => e.id);
        const { data: existingRecords, error: selectError } = await client
          .from('github_sync_history')
          .select('github_event_id')
          .in('github_event_id', targetEventIds);

        if (selectError) throw new Error('Error al consultar historial: ' + selectError.message);

        const existingIds = new Set(existingRecords?.map(r => r.github_event_id) || []);
        const newEvents = targetEvents.filter(e => !existingIds.has(e.id));

        if (newEvents.length === 0) {
          SupabaseManager.showToast('Tus commits ya fueron sincronizados.', 'info');
          this.syncingGithub = false;
          return;
        }

        let newXp = newEvents.length * 50;
        
        // Optimización: insertar todos los eventos nuevos en una sola llamada (bulk insert)
        const rowsToInsert = newEvents.map(e => ({
          user_id: this.profile.id,
          github_event_id: e.id,
          event_type: e.type,
          repo_name: e.repo.name,
          xp_awarded: 50,
        }));

        const { error: insertError } = await client.from('github_sync_history').insert(rowsToInsert);
        if (insertError) throw new Error('Error al guardar historial: ' + insertError.message);

        // Otorgar XP al usuario mediante RPC
        const { error: rpcError } = await client.rpc('award_xp_and_badge', {
          target_user: this.profile.id,
          xp_amount: newXp,
        });

        if (!rpcError) {
          this.profile.xp = (this.profile.xp || 0) + newXp;
          this.githubXp += newXp;
          SupabaseManager.showToast(`¡Ganaste +${newXp} XP por tus commits! 🐙🔥`, 'success', 5000);
        } else {
           throw new Error('Error al asignar XP: ' + rpcError.message);
        }

      } catch (e) {
        SupabaseManager.showToast(e.message, 'error');
      }
      this.syncingGithub = false;
    },

    async handleSignOut() {
      await SupabaseManager.signOut();
      window.location.href = 'login.html';
    },

    // ─── Helpers ───
    getAvatar(id) {
      const av = this.avatarCatalog.find(a => a.id === id);
      return av ? av.src : this.avatarCatalog[0].src;
    },

    calculateTimeLeft(deadline) {
      if (!deadline) return 'Sin fecha límite';
      const now = new Date();
      const d = new Date(deadline);
      const diffMs = d - now;
      if (diffMs <= 0) return 'Finalizado';
      
      const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diffMs / (1000 * 60 * 60)) % 24);
      const mins = Math.floor((diffMs / 1000 / 60) % 60);
      
      if (days > 0) return `${days}d ${hours}h`;
      if (hours > 0) return `${hours}h ${mins}m`;
      return `${mins}m`;
    },

    formatTimeAgo(dateStr) {
      if (!dateStr) return '';
      const d = new Date(dateStr);
      const now = new Date();
      const diffMs = now - d;
      const mins = Math.floor(diffMs / 60000);
      if (mins < 1) return 'ahora';
      if (mins < 60) return `hace ${mins} min`;
      const hours = Math.floor(mins / 60);
      if (hours < 24) return `hace ${hours} h`;
      const days = Math.floor(hours / 24);
      if (days < 7) return `hace ${days} d`;
      const months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
      return `${d.getDate()} ${months[d.getMonth()]}`;
    },

    renderMd(text) {
      if (!text) return '';
      if (typeof marked !== 'undefined') {
        try { return marked.parse(text); } catch (e) { /* fallback */ }
      }
      return text.replace(/\n/g, '<br>');
    },
  },
}).mount('#app');
