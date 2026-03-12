# 🚀 Guía Rápida de Git y GitHub

### Fundamentos de Programación - Duoc UC Puerto Montt


## 🛠️ 1. Preparación Inicial

Antes de empezar, asegúrate de estar dentro de la carpeta de tu proyecto en la terminal.

**Clonar el repositorio (solo la primera vez):**

```bash
git clone https://github.com/hachimaki-dev/fundamentos_de_programacion_alumnos_DuocUCPMontt_2026.git
cd fundamentos_de_programacion_alumnos_DuocUCPMontt_2026

```

---

## 📝 2. El Ciclo de Trabajo (Guardar Cambios)

Hacer un "commit" es como sacar una foto a tu código en un momento específico para poder volver a ella si algo sale mal.

1. **Verificar qué cambió:**
Mira qué archivos has modificado.
```bash
git status

```


2. **Preparar los archivos:**
Añade los cambios al "escenario" (staging area).
```bash
git add .

```


*(El punto indica que quieres agregar todos los archivos modificados).*
3. **Crear la foto (Commit):**
Ponle un nombre descriptivo a tu cambio.
```bash
git commit -m "Explica aquí qué hiciste (ej: Agregado ejercicio de bucles)"

```



---

## ☁️ 3. Subir el código a GitHub

Una vez que el commit está hecho en tu computadora, debes "empujarlo" al servidor de GitHub para que el profesor pueda verlo.

```bash
git push origin nombre-de-tu-rama

```

*(Si estás trabajando en la rama principal, suele ser `git push origin main`).*

---

## 🌿 4. Trabajando con Ramas (Branches)

Las ramas sirven para experimentar sin romper el código que ya funciona. Imaginalas como líneas de tiempo paralelas.

* **Crear una nueva rama y saltar a ella:**
```bash
git checkout -b nombre-de-la-rama

```


* **Ver en qué rama estás:**
```bash
git branch

```


* **Cambiar a una rama que ya existe:**
```bash
git checkout nombre-de-la-rama

```



---

## 💡 Consejos de Supervivencia

> [!TIP]
> **¿No sabes qué pasó?** Usa siempre `git status`. Es tu mejor amigo para saber en qué rama estás y si tienes archivos sin guardar.
> **¿Mensaje de error?** Lee las últimas líneas. Git suele decirte exactamente qué comando te falta ejecutar.
