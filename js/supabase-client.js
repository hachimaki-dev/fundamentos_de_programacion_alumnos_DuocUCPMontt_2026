// ═══════════════════════════════════════════════════════════════
//  🔐 Supabase Client — Motor de Autenticación
//  ─────────────────────────────────────────────────────────────
//  Singleton que inicializa Supabase y expone helpers de auth.
//  Debe cargarse DESPUÉS del CDN de Supabase.
// ═══════════════════════════════════════════════════════════════

const SupabaseManager = (() => {
  'use strict';

  // ── Config ──
  const SUPABASE_URL = 'https://fokqmosaomsdytsghnsc.supabase.co';
  const SUPABASE_KEY = 'sb_publishable_eIX-ZaE-AUx4eaMguDdf2w_xxpCHcM-';

  // ── Singleton client ──
  let _client = null;

  function getClient() {
    if (!_client) {
      if (typeof supabase === 'undefined' || !supabase.createClient) {
        console.error('[SupabaseManager] Supabase JS SDK not loaded. Include the CDN script first.');
        return null;
      }
      _client = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
    }
    return _client;
  }

  // ═══════════════════════════════════════════
  //  AUTH HELPERS
  // ═══════════════════════════════════════════

  /** Sign up with email + password */
  async function signUp(email, password) {
    const client = getClient();
    const { data, error } = await client.auth.signUp({
      email,
      password,
    });
    return { data, error };
  }

  /** Sign in with email + password */
  async function signIn(email, password) {
    const client = getClient();
    const { data, error } = await client.auth.signInWithPassword({
      email,
      password,
    });
    return { data, error };
  }

  /** Sign out */
  async function signOut() {
    const client = getClient();
    const { error } = await client.auth.signOut();
    return { error };
  }

  /** Get current session (null if not logged in) */
  async function getSession() {
    const client = getClient();
    const { data: { session }, error } = await client.auth.getSession();
    return { session, error };
  }

  /** Get current user (null if not logged in) */
  async function getUser() {
    const { session } = await getSession();
    return session?.user || null;
  }

  // ═══════════════════════════════════════════
  //  PROFILE HELPERS
  // ═══════════════════════════════════════════

  /** Get the profile for the current user */
  async function getProfile() {
    const user = await getUser();
    if (!user) return { profile: null, error: 'Not authenticated' };

    const client = getClient();
    const { data, error } = await client
      .from('profiles')
      .select('*')
      .eq('id', user.id)
      .single();

    return { profile: data, error };
  }

  /** Update profile fields */
  async function updateProfile(updates) {
    const user = await getUser();
    if (!user) return { error: 'Not authenticated' };

    const client = getClient();
    const { data, error } = await client
      .from('profiles')
      .update({ ...updates, updated_at: new Date().toISOString() })
      .eq('id', user.id)
      .select()
      .single();

    return { data, error };
  }

  /** Check if a nickname is already taken */
  async function isNicknameTaken(nickname) {
    const user = await getUser();
    const client = getClient();
    const { data, error } = await client
      .from('profiles')
      .select('id')
      .eq('nickname', nickname)
      .neq('id', user?.id || '')
      .limit(1);

    if (error) return true; // Assume taken on error (safe side)
    return data && data.length > 0;
  }

  // ═══════════════════════════════════════════
  //  GUARDS (page-level redirects)
  // ═══════════════════════════════════════════

  /**
   * Require authentication.
   * If not logged in → redirect to login.html
   * Returns the user if authenticated.
   */
  async function requireAuth(loginPath = 'login.html') {
    const user = await getUser();
    if (!user) {
      window.location.href = loginPath;
      return null;
    }
    return user;
  }

  /**
   * Require a completed profile.
   * If profile is incomplete → redirect to setup-profile.html
   * Returns the profile if complete.
   */
  async function requireProfile(setupPath = 'setup-profile.html') {
    const user = await requireAuth();
    if (!user) return null;

    const { profile } = await getProfile();
    if (!profile || !profile.profile_completed) {
      window.location.href = setupPath;
      return null;
    }
    return profile;
  }

  /**
   * Redirect away if already logged in.
   * Use on login page to skip it for authenticated users.
   */
  async function redirectIfAuth(dashboardPath = 'dashboard.html') {
    const user = await getUser();
    if (user) {
      const { profile } = await getProfile();
      if (profile && profile.profile_completed) {
        window.location.href = dashboardPath;
      } else {
        window.location.href = 'setup-profile.html';
      }
      return true;
    }
    return false;
  }

  // ═══════════════════════════════════════════
  //  AUTH STATE LISTENER
  // ═══════════════════════════════════════════

  /** Subscribe to auth state changes */
  function onAuthStateChange(callback) {
    const client = getClient();
    return client.auth.onAuthStateChange((event, session) => {
      callback(event, session);
    });
  }

  // ═══════════════════════════════════════════
  //  TOAST NOTIFICATION SYSTEM
  // ═══════════════════════════════════════════

  function showToast(message, type = 'info', duration = 4000) {
    // Remove existing toast
    const existing = document.getElementById('sb-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'sb-toast';
    toast.className = `sb-toast sb-toast-${type}`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'polite');

    const icons = { success: '✅', error: '❌', info: 'ℹ️', warning: '⚠️' };
    toast.innerHTML = `
      <span class="sb-toast-icon">${icons[type] || 'ℹ️'}</span>
      <span class="sb-toast-msg">${message}</span>
    `;

    document.body.appendChild(toast);

    // Trigger entrance animation
    requestAnimationFrame(() => {
      toast.classList.add('sb-toast-visible');
    });

    // Auto dismiss
    setTimeout(() => {
      toast.classList.remove('sb-toast-visible');
      toast.classList.add('sb-toast-exit');
      setTimeout(() => toast.remove(), 350);
    }, duration);
  }

  // ═══════════════════════════════════════════
  //  AVATAR CATALOG
  // ═══════════════════════════════════════════

  const AVATAR_CATALOG = [
    { id: 'python-01', src: '../assets/avatars/python-01.webp', category: 'python', label: 'Python Snake' },
    { id: 'python-02', src: '../assets/avatars/python-02.webp', category: 'python', label: 'Python Logo' },
    { id: 'python-03', src: '../assets/avatars/python-03.webp', category: 'python', label: 'Code Snake' },
    { id: 'python-04', src: '../assets/avatars/python-04.webp', category: 'python', label: 'Python Master' },
    { id: 'dev-01', src: '../assets/avatars/dev-01.webp', category: 'dev', label: 'Developer' },
    { id: 'dev-02', src: '../assets/avatars/dev-02.svg', category: 'dev', label: 'Hacker' },
    { id: 'dev-03', src: '../assets/avatars/dev-03.webp', category: 'dev', label: 'Code Ninja' },
    { id: 'dev-04', src: '../assets/avatars/dev-04.svg', category: 'dev', label: 'Full Stack' },
    { id: 'gaming-01', src: '../assets/avatars/gaming-01.svg', category: 'gaming', label: 'Gamer' },
    { id: 'gaming-02', src: '../assets/avatars/gaming-02.svg', category: 'gaming', label: 'Pixel Hero' },
    { id: 'gaming-03', src: '../assets/avatars/gaming-03.svg', category: 'gaming', label: 'Controller' },
    { id: 'gaming-04', src: '../assets/avatars/gaming-04.svg', category: 'gaming', label: 'Arcade' },
    { id: 'kawaii-01', src: '../assets/avatars/kawaii-01.svg', category: 'kawaii', label: 'Kawaii Cat' },
    { id: 'kawaii-02', src: '../assets/avatars/kawaii-02.svg', category: 'kawaii', label: 'Kawaii Bot' },
    { id: 'kawaii-03', src: '../assets/avatars/kawaii-03.svg', category: 'kawaii', label: 'Kawaii Star' },
    { id: 'kawaii-04', src: '../assets/avatars/kawaii-04.svg', category: 'kawaii', label: 'Kawaii Cloud' },
    { id: 'robot-01', src: '../assets/avatars/robot-01.svg', category: 'robot', label: 'Robot Coder' },
    { id: 'robot-02', src: '../assets/avatars/robot-02.svg', category: 'robot', label: 'AI Bot' },
    { id: 'robot-03', src: '../assets/avatars/robot-03.svg', category: 'robot', label: 'Mech Dev' },
    { id: 'robot-04', src: '../assets/avatars/robot-04.svg', category: 'robot', label: 'Cyber Bot' },
    { id: 'space-01', src: '../assets/avatars/space-01.svg', category: 'space', label: 'Astronaut' },
    { id: 'space-02', src: '../assets/avatars/space-02.svg', category: 'space', label: 'Rocket' },
    { id: 'space-03', src: '../assets/avatars/space-03.svg', category: 'space', label: 'Planet' },
    { id: 'space-04', src: '../assets/avatars/space-04.svg', category: 'space', label: 'Galaxy' },
  ];

  function getAvatarCatalog() {
    return AVATAR_CATALOG;
  }

  function getAvatarById(id) {
    return AVATAR_CATALOG.find(a => a.id === id) || AVATAR_CATALOG[0];
  }

  function getAvatarCategories() {
    return [
      { id: 'python', label: '🐍 Python', icon: '🐍' },
      { id: 'dev', label: '💻 Dev', icon: '💻' },
      { id: 'gaming', label: '🎮 Gaming', icon: '🎮' },
      { id: 'kawaii', label: '🌸 Kawaii', icon: '🌸' },
      { id: 'robot', label: '🤖 Bots', icon: '🤖' },
      { id: 'space', label: '🚀 Espacio', icon: '🚀' },
    ];
  }

  // ═══════════════════════════════════════════
  //  SECTIONS CATALOG
  // ═══════════════════════════════════════════

  const SECTIONS = [
    { value: '001D', label: '001D — Diurno' },
    { value: '001V', label: '001V — Vespertino' },
    { value: '005V', label: '005V — Vespertino' },
  ];

  function getSections() {
    return SECTIONS;
  }

  // ═══════════════════════════════════════════
  //  PUBLIC API
  // ═══════════════════════════════════════════

  return {
    getClient,
    // Auth
    signUp,
    signIn,
    signOut,
    getSession,
    getUser,
    onAuthStateChange,
    // Profile
    getProfile,
    updateProfile,
    isNicknameTaken,
    // Guards
    requireAuth,
    requireProfile,
    redirectIfAuth,
    // UI
    showToast,
    // Data
    getAvatarCatalog,
    getAvatarById,
    getAvatarCategories,
    getSections,
  };
})();
