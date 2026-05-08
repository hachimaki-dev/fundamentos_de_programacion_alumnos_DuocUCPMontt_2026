// ═══════════════════════════════════════════════════════════════
//  🌐 Dev Community Presence — "Quién está en línea"
//  ─────────────────────────────────────────────────────────────
//  Conecta con Supabase Realtime para mostrar devs online.
// ═══════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', async () => {
    if (typeof SupabaseManager === 'undefined') return;

    // Solo funciona si estamos autenticados
    const user = await SupabaseManager.getUser();
    if (!user) return;

    const { profile } = await SupabaseManager.getProfile();
    if (!profile) return;

    // Determinar actividad basada en la URL actual
    let activity = 'Viendo la plataforma 👀';
    const path = window.location.pathname;
    if (path.includes('competitions.html')) activity = 'En Competencia 🏆';
    else if (path.includes('diary.html')) activity = 'Escribiendo Diario 📝';
    else if (path.includes('dashboard.html')) activity = 'En Dashboard 🏠';
    else if (path.includes('banco-ejercicios.html') || path.includes('ejercicios')) activity = 'Resolviendo Ejercicios 💻';

    // Inyectar CSS
    const style = document.createElement('style');
    style.innerHTML = `
        #dev-presence-ui {
            position: fixed;
            z-index: 9999;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: white;
            font-family: 'Inter', system-ui, sans-serif;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
        }

        /* Desktop: Right Sidebar (Floating) */
        @media (min-width: 768px) {
            #dev-presence-ui {
                top: 80px;
                right: 20px;
                width: 260px;
                max-height: calc(100vh - 100px);
                border-radius: 12px;
                padding: 16px;
                overflow-y: auto;
            }
        }

        /* Mobile: Top Bar */
        @media (max-width: 767px) {
            #dev-presence-ui {
                top: 0;
                left: 0;
                right: 0;
                width: 100%;
                max-height: 120px;
                border-radius: 0 0 12px 12px;
                padding: 10px;
                display: flex;
                flex-direction: column;
            }
        }

        .presence-header {
            font-size: 0.85rem;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .presence-count {
            background: #3b82f6;
            color: white;
            padding: 2px 8px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        .presence-user {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 8px;
            padding: 8px;
            border-radius: 8px;
            transition: background 0.2s;
        }

        .presence-user:hover {
            background: rgba(255, 255, 255, 0.05);
        }

        .presence-avatar-wrap {
            position: relative;
            flex-shrink: 0;
        }

        .presence-avatar {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #334155;
            object-fit: cover;
            border: 2px solid #3b82f6;
        }

        .presence-info {
            display: flex;
            flex-direction: column;
            flex: 1;
            overflow: hidden;
        }

        .presence-name {
            font-size: 0.9rem;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .presence-level-badge {
            background: #f59e0b;
            color: white;
            font-size: 0.65rem;
            padding: 1px 4px;
            border-radius: 4px;
            font-weight: 800;
        }

        .presence-activity {
            font-size: 0.75rem;
            color: #cbd5e1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        
        .presence-section {
            font-size: 0.65rem;
            color: #64748b;
            margin-top: 2px;
        }

        .online-dot {
            position: absolute;
            bottom: -2px;
            right: -2px;
            width: 12px;
            height: 12px;
            background: #22c55e;
            border-radius: 50%;
            border: 2px solid #1e293b;
        }
        
        /* Custom Scrollbar for Desktop */
        @media (min-width: 768px) {
            #dev-presence-ui::-webkit-scrollbar { width: 6px; }
            #dev-presence-ui::-webkit-scrollbar-track { background: transparent; }
            #dev-presence-ui::-webkit-scrollbar-thumb { background: #475569; border-radius: 10px; }
        }

        /* Mobile Adjustments */
        @media (max-width: 767px) {
            .presence-list {
                display: flex;
                gap: 12px;
                overflow-x: auto;
                padding-bottom: 4px;
                scrollbar-width: none; /* Firefox */
            }
            .presence-list::-webkit-scrollbar { display: none; } /* Chrome */
            
            .presence-user {
                flex-direction: column;
                margin-bottom: 0;
                min-width: 60px;
                padding: 4px;
                text-align: center;
                gap: 4px;
            }
            .presence-info {
                align-items: center;
            }
            .presence-name {
                font-size: 0.75rem;
            }
            .presence-level-badge { display: none; }
            .presence-activity { display: none; }
            .presence-section { display: none; }
            .presence-header { margin-bottom: 8px; }
        }
    `;
    document.head.appendChild(style);

    // Crear Contenedor UI
    const uiContainer = document.createElement('div');
    uiContainer.id = 'dev-presence-ui';
    uiContainer.innerHTML = `
        <div class="presence-header">
            <span>🚀 Devs Online</span>
            <span class="presence-count" id="presence-count-badge">0</span>
        </div>
        <div class="presence-list" id="presence-list-container">
            <!-- Los usuarios se inyectan aquí -->
            <div style="font-size:0.8rem;color:#94a3b8;text-align:center;">Conectando...</div>
        </div>
    `;
    document.body.appendChild(uiContainer);

    // Función para renderizar usuarios
    const renderUsers = (users) => {
        const list = document.getElementById('presence-list-container');
        const badge = document.getElementById('presence-count-badge');
        if (!list || !badge) return;

        badge.textContent = users.length;
        
        if (users.length === 0) {
            list.innerHTML = '<div style="font-size:0.8rem;color:#94a3b8;text-align:center;">Nadie más en línea 🥺</div>';
            return;
        }

        // Obtener el catálogo de avatares para resolver las URLs
        const avatarCatalog = SupabaseManager.getAvatarCatalog();

        list.innerHTML = users.map(u => {
            const state = u.presenceData;
            
            let avatarSrc = '';
            if (state.avatar_source === 'custom' && state.avatar_custom_url) {
                avatarSrc = state.avatar_custom_url;
            } else {
                const avatarObj = avatarCatalog.find(a => a.id === state.avatar_id) || avatarCatalog[0];
                const isPagesDir = window.location.pathname.includes('/pages/');
                avatarSrc = isPagesDir ? avatarObj.src : avatarObj.src.replace('../', '');
            }

            // Nivel (si existe)
            const levelBadge = state.level ? \`<span class="presence-level-badge">Lvl \${state.level}</span>\` : '';

            return \`
            <div class="presence-user" title="\${state.activity}">
                <div class="presence-avatar-wrap">
                    <img src="\${avatarSrc}" class="presence-avatar" alt="\${state.nickname}">
                    <div class="online-dot"></div>
                </div>
                <div class="presence-info">
                    <span class="presence-name">\${state.nickname} \${levelBadge}</span>
                    <span class="presence-activity">\${state.activity}</span>
                    <span class="presence-section">Sección \${state.section || 'N/A'}</span>
                </div>
            </div>
            \`;
        }).join('');
    };

    // ── Supabase Realtime ──
    const client = SupabaseManager.getClient();
    // Usamos un canal global 'global-dev-lounge'
    const channel = client.channel('global-dev-lounge');

    channel
        .on('presence', { event: 'sync' }, () => {
            const newState = channel.presenceState();
            const uniqueUsers = [];
            
            for (const [userId, presences] of Object.entries(newState)) {
                if (presences.length > 0) {
                    uniqueUsers.push({
                        userId,
                        presenceData: presences[0] 
                    });
                }
            }
            renderUsers(uniqueUsers);
        })
        .subscribe(async (status) => {
            if (status === 'SUBSCRIBED') {
                await channel.track({
                    user_id: user.id,
                    nickname: profile.nickname || 'Anon Dev',
                    avatar_id: profile.avatar_id,
                    avatar_source: profile.avatar_source,
                    avatar_custom_url: profile.avatar_custom_url,
                    section: profile.section,
                    activity: activity,
                    level: profile.level || 1 // Agregaremos esto en la Fase 2
                });
            }
        });
});
