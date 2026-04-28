// ═══════════════════════════════════════════════════════════════
//  🎨 Theme Engine — Motor de Temas
//  ─────────────────────────────────────────────────────────────
//  Manages theme selection, localStorage persistence, and
//  dynamic font loading. Must be loaded BEFORE Vue.
// ═══════════════════════════════════════════════════════════════

const ThemeEngine = (() => {
  const STORAGE_KEY = 'preferred-theme';
  const DEFAULT_THEME = 'city-pop';

  const THEMES = [
    {
      id: 'city-pop',
      name: 'City Pop 🌃',
      description: 'Retro-futurista japonés de los 80',
      icon: '🌃',
      preview: 'linear-gradient(45deg, #0d0221, #1a0a3e, #0f2027)',
      accentPreview: '#ff6b9d',
      fonts: 'Outfit:wght@400;500;600;700;800',
    },
    {
      id: 'legacy',
      name: 'Kawaii 🌸',
      description: 'El tema viejito con gradientes suaves',
      icon: '🌸',
      preview: 'linear-gradient(135deg, #fce4ec, #e1bee7, #b3e5fc)',
      accentPreview: '#ad1457',
      fonts: 'Quicksand:wght@400;500;600;700',
    },
    {
      id: 'post-textual',
      name: 'Minimal 📐',
      description: 'Reducción de carga cognitiva',
      icon: '📐',
      preview: '#0a0a0a',
      accentPreview: '#e0e0e0',
      fonts: 'Inter:wght@400;500;600;700;800',
    },
    {
      id: 'bento',
      name: 'Bento 🍱',
      description: 'Grilla modular moderna',
      icon: '🍱',
      preview: '#f5f0eb',
      accentPreview: '#1a1a2e',
      fonts: 'DM+Sans:wght@400;500;600;700',
    },
  ];

  // Font links cache
  let _currentFontLink = null;

  /**
   * Load Google Font for the given theme.
   */
  function _loadFonts(themeId) {
    const theme = THEMES.find(t => t.id === themeId);
    if (!theme) return;

    // Always keep Fira Code (code font) + JetBrains Mono for post-textual
    const baseFonts = 'Fira+Code:wght@400;500';
    const extraCode = themeId === 'post-textual' ? '&family=JetBrains+Mono:wght@400;500' : '';
    const href = `https://fonts.googleapis.com/css2?family=${theme.fonts}&family=${baseFonts}${extraCode}&display=swap`;

    // Remove previous dynamic font link
    if (_currentFontLink && _currentFontLink.parentNode) {
      _currentFontLink.parentNode.removeChild(_currentFontLink);
    }

    // Create new link
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    link.id = 'theme-fonts';
    document.head.appendChild(link);
    _currentFontLink = link;
  }

  /**
   * Apply the theme to the document.
   */
  function setTheme(themeId) {
    if (!THEMES.find(t => t.id === themeId)) {
      themeId = DEFAULT_THEME;
    }
    document.documentElement.setAttribute('data-theme', themeId);
    localStorage.setItem(STORAGE_KEY, themeId);
    _loadFonts(themeId);
    // Dispatch custom event for Vue reactivity
    window.dispatchEvent(new CustomEvent('theme-changed', { detail: { theme: themeId } }));
  }

  /**
   * Get the current active theme id.
   */
  function getTheme() {
    return document.documentElement.getAttribute('data-theme') || DEFAULT_THEME;
  }

  /**
   * Get list of available themes with metadata.
   */
  function getThemes() {
    return THEMES;
  }

  /**
   * Initialize theme on page load.
   * Call this as early as possible to avoid FOUC.
   */
  function init() {
    const saved = localStorage.getItem(STORAGE_KEY);
    const themeId = saved || DEFAULT_THEME;
    document.documentElement.setAttribute('data-theme', themeId);
    _loadFonts(themeId);
  }

  // Auto-init immediately
  init();

  return { setTheme, getTheme, getThemes, init };
})();
