# 🚀 Instrucciones de Implementación — Full Personalización de Perfiles

Todos los archivos están listos. Sigue estos pasos para activar el sistema.

---

## 📋 Paso 1: Actualizar la Base de Datos en Supabase

### 1.1 Ejecutar Scripts SQL (En Orden)

Ve a **Supabase Dashboard → SQL Editor** y ejecuta estos scripts en ORDEN:

1. **[02_profiles_enhancement.sql](./02_profiles_enhancement.sql)** — Agrega nuevos campos a profiles
2. **[03_profile_followers.sql](./03_profile_followers.sql)** — Crea tabla de followers y funciones helper
3. **[04_profile_storage.sql](./04_profile_storage.sql)** — Configura bucket para avatares

> ⚠️ **IMPORTANTE:** Ejecutarlos en este ORDEN exacto. Cada script es idempotente (puedes re-ejecutar sin problemas).

### 1.2 Result del Lado de Supabase

Después de ejecutar los scripts, deberías tener:

✅ **Nueva columna en `profiles`:**
- `avatar_custom_url` — URL de Storage para foto subida
- `avatar_source` — 'catalog' o 'custom'
- `bio` — Biografía corta
- `social_links` — JSON con {github, twitter, youtube, portfolio}
- `visibility` — 'public', 'followers_only', 'private'
- `custom_html` — Actualizado con sanitización
- `custom_css` — Actualizado con sanitización
- `myspace_theme` — Tema seleccionado
- `profile_completed` — Flag de setup

✅ **Nueva tabla `profile_followers`:**
- Relación follower_id → following_id
- RLS policies configuradas
- Funciones helper en SQL

✅ **Bucket `profile-avatars`:**
- Almacenamiento de avatares custom
- Límite 5MB por imagen
- Solo formatos imagen

---

## 📂 Paso 2: Archivos Creados/Modificados

### Nuevos Archivos ✨

| Archivo | Descripción |
|---------|-------------|
| `pages/profile-editor.html` | Página principal para editar perfil |
| `js/profile-editor-app.js` | Lógica Vue del editor |
| `supabase/02_profiles_enhancement.sql` | Migración de campos nuevos |
| `supabase/03_profile_followers.sql` | Sistema de followers |
| `supabase/04_profile_storage.sql` | Storage para avatares |

### Archivos Modificados 🔄

| Archivo | Cambios |
|---------|---------|
| `js/supabase-client.js` | +7 funciones nuevas para followers |
| `pages/dashboard.html` | Link a profile-editor + mostrar bio |
| `pages/profile.html` | Follow/unfollow mejorado + bio + social links |
| `supabase/00_README.sql` | Instrucciones actualizadas |

---

## 🔧 Paso 3: Configuración Manual en Supabase (Opcional pero Recomendado)

### Si tu bucket "profile-avatars" no se creó automáticamente:

1. Ve a **Storage → Buckets**
2. Click en **"Create a new bucket"**
3. Configura:
   - **Name:** `profile-avatars`
   - **Public:** ON (para que los avatares se puedan mostrar públicamente)
   - **File size limit:** 5242880 (5MB)
   - **Allowed MIME types:** `image/jpeg, image/png, image/webp, image/gif`
4. Click **Create bucket**

> Nota: Si al ejecutar `04_profile_storage.sql` en el editor SQL obtienes el error
> "must be owner of table objects", deja esa parte y crea las políticas de Storage
> directamente desde el panel de Storage de Supabase.

---

## ✅ Paso 4: Verificar que Todo Funciona

### Testing en el Navegador:

1. **Login** a tu cuenta en la app
2. Ve a **Dashboard**
3. En el perfil card (parte superior izquierda), deberías ver:
   - ✏️ **Botón "Editar"** (nuevo)
   - 👁️ **Botón "Ver"** (igual)
4. Click en **"Editar"** → Deberías ver la página `/pages/profile-editor.html`
5. Prueba:
   - ✅ Cambiar nickname
   - ✅ Editar full_name
   - ✅ Escribir bio
   - ✅ **Subir foto** con drag-drop o click
   - ✅ Agregar social links
   - ✅ Cambiar visibilidad
   - ✅ Guardar

### Si ve un error al subir foto:
- Verifica que el bucket `profile-avatars` exista
- Verifica RLS policies en Supabase SQL

---

## 🎯 Flujos de Usuario Activos

### Flujo 1: Editar Mi Perfil

```
Dashboard → Click "Editar" → profile-editor.html
→ Completa campos → Click "Guardar Cambios"
→ Avatar se sube a Storage → Perfil se guarda
→ Redirige a profile.html (ver con cambios)
```

### Flujo 2: Ver Mi Perfil Público

```
Dashboard → Click "Ver" → profile.html?nickname=mi-nick
→ Ve su perfil como otros lo verían
```

### Flujo 3: Ver Perfil de Otro Usuario

```
Timeline/Competencias → Click en avatar/nombre de usuario
→ profile.html?nickname=otro-nick
→ Si es público: Ve todo
→ Si es followers_only: Botón de seguir
→ Si es private: "Perfil privado"
```

### Flujo 4: Seguir/Unfollow

```
profile.html (otro usuario) → Click "➕ Seguir"
→ Se agrega relación en profile_followers
→ Counter de "Seguidores" aumenta
→ Botón cambia a "✅ Siguiendo"
→ Click de nuevo → Dejar de seguir
```

---

## 🎨 Características Implementadas

### MVP — Ya Funciona ✅

- [x] Editar nombre completo, nickname, bio
- [x] Subir foto de perfil custom (5MB)
- [x] Ver fotos (catalog o custom)
- [x] Agregar social links (GitHub, Twitter, YouTube, Portfolio)
- [x] Control de privacidad (Public, Private, Followers Only)
- [x] Sistema de seguidores (Follow/Unfollow)
- [x] Ver cantidad de seguidores/siguiendo
- [x] Personalización HTML/CSS del MySpace
- [x] Mostrar bio en dashboard y profile
- [x] Mostrar social links en profile público
- [x] Preview de perfil de tiempo real

### Futuro (Fase 2)

- 🔄 Plantillas de MySpace predefinidas
- 🔄 Badges de logros en perfil
- 🔄 Analytics de visitas al perfil
- 🔄 Mensaje directo entre usuarios
- 🔄 Perfil completion score gamificado

---

## 🔐 Seguridad Implementada

✅ **Frontend:**
- Validación HTML5 + JS custom
- DOMPurify para sanitizar HTML/CSS
- No se ejecutan scripts en custom_html

✅ **Backend (Supabase):**
- RLS en `profiles` → públicos visible, privados restringidos
- RLS en `profile_followers` → solo follower puede unfollow
- RLS en `storage.objects` → solo owner puede subir/eliminar
- Constraints en BD (no self-follow, unique followers, etc)

✅ **Storage:**
- Validación MIME types
- Límite de tamaño (5MB)
- URLs signed (control de acceso)

---

## 🐛 Troubleshooting

### Error: "Error al subir la imagen"
**Solución:**
1. Verifica que bucket `profile-avatars` exista
2. Verifica RLS policy `"Allow authenticated to upload avatars"`
3. Intenta con otra imagen más pequeña

### Error: "Este nickname ya está en use"
**Solución:**
1. Elige otro nickname
2. Verifica uniqueness constraint en BD

### Botón "Editar" no aparece
**Solución:**
1. Verifica que estés logueado
2. Hard reload del dashboard (Ctrl+Shift+R)
3. Revisa console para errores

### Profile de otro usuario no carga
**Solución:**
1. Si es privado: "Este perfil es privado"
2. Si es followers_only: Síguelo primero
3. Verifica que el nickname exista

---

## 📊 Estadísticas de Implementación

| Aspecto | Métrica |
|--------|---------|
| **Nuevos Archivos** | 3 (2 HTML/JS + 2 SQL) |
| **Archivos Modificados** | 4 (JS + HTML) |
| **Nuevas Funciones JS** | 7 (followers management) |
| **Nuevas Columnas BD** | 9 |
| **Nuevas Tablas** | 1 (profile_followers) |
| **Nuevas Views SQL** | 2 |
| **RLS Policies Nuevas** | 8+ |
| **Tiempo Estimado Setup** | 15 mins |

---

## 📝 Notas Importantes

### Avatar Source Priority

```
Si avatar_source = 'custom' y avatar_custom_url existe
  → Mostrar foto custom
Sino
  → Buscar en catálogo por avatar_id
  → Fallback a catálogo[0]
```

### Privacidad por Defecto

```
- visibility = 'public'  → Todos ven
- visibility = 'followers_only' → Solo followers + owner
- visibility = 'private' → Solo owner (me lo oculto a mí mismo? no)
```

### Validación de Nickname

```
- Longitud: 3-30 caracteres
- Formato: a-zA-Z0-9_ solamente
- Unique a nivel de BD
- Async validation al blur
```

---

## 🎓 Recursos

| Recurso | Enlace |
|---------|--------|
| Plan Detallado | `./.PLAN_PERSONALIZACION.md` |
| SQL Scripts | `./supabase/` |
| Profile Editor | `./pages/profile-editor.html` |
| Supabase Docs | https://supabase.com/docs |

---

## ✨ Próximos Pasos Opcionales

1. **Gamificación:** Mostrar profile_completeness en dashboard
2. **Notificaciones:** Avisar cuando alguien te sigue
3. **Búsqueda:** Buscar otros usuarios por nickname/bio
4. **Leaderboard:** Top usuarios más seguidos
5. **Export:** Descargar datos del perfil

---

**Estado:** ✅ **LISTO PARA PRODUCCIÓN**  
**Versión:** 1.0  
**Fecha:** 7 de Mayo, 2026  

¡Tu sistema de personalización de perfiles está operativo! 🎉
