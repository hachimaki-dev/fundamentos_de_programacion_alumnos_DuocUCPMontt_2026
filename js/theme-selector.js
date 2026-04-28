// ═══════════════════════════════════════════════════════════════
//  🎛️ Theme Selector — Componente UI de selección de tema
//  ─────────────────────────────────────────────────────────────
//  Floating action button + panel. Pure CSS + vanilla JS.
//  Works independently of Vue — just needs theme-engine.js.
// ═══════════════════════════════════════════════════════════════

(function () {
  'use strict';

  function createSelector() {
    const themes = ThemeEngine.getThemes();

    // Build HTML
    const wrapper = document.createElement('div');
    wrapper.id = 'theme-selector';
    wrapper.innerHTML = `
      <button class="ts-fab" id="ts-fab" aria-label="Cambiar tema" title="Cambiar tema">
        🎨
      </button>
      <div class="ts-panel" id="ts-panel">
        <p class="ts-panel-title">Elige tu tema</p>
        <div class="ts-options">
          ${themes.map(t => `
            <button class="ts-option" data-theme-id="${t.id}" title="${t.description}">
              <span class="ts-preview" style="background:${t.preview};">
                <span class="ts-preview-dot" style="background:${t.accentPreview};"></span>
              </span>
              <span class="ts-label">
                <span class="ts-name">${t.name}</span>
                <span class="ts-desc">${t.description}</span>
              </span>
              <span class="ts-check" aria-hidden="true">✓</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    document.body.appendChild(wrapper);

    // References
    const fab = document.getElementById('ts-fab');
    const panel = document.getElementById('ts-panel');
    let isOpen = false;

    // Highlight active
    function updateActive() {
      const current = ThemeEngine.getTheme();
      wrapper.querySelectorAll('.ts-option').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.themeId === current);
      });
    }

    // Toggle panel
    fab.addEventListener('click', (e) => {
      e.stopPropagation();
      isOpen = !isOpen;
      panel.classList.toggle('open', isOpen);
      fab.classList.toggle('open', isOpen);
      if (isOpen) updateActive();
    });

    // Theme selection
    wrapper.querySelectorAll('.ts-option').forEach(btn => {
      btn.addEventListener('click', () => {
        ThemeEngine.setTheme(btn.dataset.themeId);
        updateActive();
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (isOpen && !wrapper.contains(e.target)) {
        isOpen = false;
        panel.classList.remove('open');
        fab.classList.remove('open');
      }
    });

    // Listen for theme changes from other sources
    window.addEventListener('theme-changed', updateActive);

    updateActive();
  }

  // Inject styles
  const style = document.createElement('style');
  style.textContent = `
    #theme-selector {
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      z-index: 9999;
      font-family: var(--t-font-main, 'Quicksand'), sans-serif;
    }

    .ts-fab {
      width: 3.2rem;
      height: 3.2rem;
      border-radius: 50%;
      border: 2px solid var(--t-glass-border);
      background: var(--t-surface, rgba(255,255,255,0.8));
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      cursor: pointer;
      font-size: 1.4rem;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px var(--t-shadow, rgba(0,0,0,0.1));
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      z-index: 2;
    }
    .ts-fab:hover {
      transform: scale(1.1);
      box-shadow: 0 6px 25px var(--t-shadow-hover, rgba(0,0,0,0.15));
    }
    .ts-fab.open {
      transform: rotate(45deg) scale(1.1);
    }

    .ts-panel {
      position: absolute;
      bottom: calc(100% + 0.75rem);
      right: 0;
      width: 280px;
      background: var(--t-surface-solid, #fff);
      border: 2px solid var(--t-glass-border);
      border-radius: var(--t-radius, 1rem);
      box-shadow: 0 12px 40px var(--t-shadow, rgba(0,0,0,0.15));
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 1rem;
      opacity: 0;
      visibility: hidden;
      transform: translateY(10px) scale(0.95);
      transition: opacity 0.25s ease, transform 0.25s ease, visibility 0.25s;
      z-index: 1;
    }
    .ts-panel.open {
      opacity: 1;
      visibility: visible;
      transform: translateY(0) scale(1);
    }

    .ts-panel-title {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--t-text-muted);
      margin-bottom: 0.75rem;
      padding-left: 0.25rem;
    }

    .ts-options {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .ts-option {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.6rem 0.75rem;
      border-radius: 0.75rem;
      border: 2px solid transparent;
      background: transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      width: 100%;
      text-align: left;
      font-family: inherit;
    }
    .ts-option:hover {
      background: var(--t-surface-alt);
      border-color: var(--t-surface-border);
    }
    .ts-option.active {
      background: var(--t-accent-bg, rgba(173,20,87,0.08));
      border-color: var(--t-accent-subtle);
    }

    .ts-preview {
      width: 2.2rem;
      height: 2.2rem;
      border-radius: 0.5rem;
      flex-shrink: 0;
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;
      padding: 0.2rem;
      border: 1px solid var(--t-surface-border);
    }
    .ts-preview-dot {
      width: 0.6rem;
      height: 0.6rem;
      border-radius: 50%;
    }

    .ts-label {
      flex: 1;
      min-width: 0;
    }
    .ts-name {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--t-text);
      line-height: 1.3;
    }
    .ts-desc {
      display: block;
      font-size: 0.7rem;
      color: var(--t-text-muted);
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .ts-check {
      font-size: 0.9rem;
      color: var(--t-correct, #66bb6a);
      opacity: 0;
      transition: opacity 0.2s ease;
    }
    .ts-option.active .ts-check {
      opacity: 1;
    }

    @media (max-width: 480px) {
      #theme-selector {
        bottom: 1rem;
        right: 1rem;
      }
      .ts-panel {
        width: 250px;
      }
      .ts-fab {
        width: 2.8rem;
        height: 2.8rem;
        font-size: 1.2rem;
      }
    }
  `;
  document.head.appendChild(style);

  // Create on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createSelector);
  } else {
    createSelector();
  }
})();
