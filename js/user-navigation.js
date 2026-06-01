// ═══════════════════════════════════════════════════════════════
//  🔗 USER NAVIGATION SYSTEM — Global Profile Navigation
// ═══════════════════════════════════════════════════════════════

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

// Alias corto para uso en consola y scripting
const UserNav = UserNavigation;
