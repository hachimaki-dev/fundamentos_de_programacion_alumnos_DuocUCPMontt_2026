# 🏆 7 Desafíos Élite — Post-55

> Para quienes ya conquistaron los 55 ejercicios. Estos retos no tienen una sola respuesta obvia: requieren que conectes varios conceptos a la vez y pienses antes de escribir. Sin herramientas nuevas, solo lo que ya sabes.
>
> Los desafíos 6 y 7 son de otra categoría. No son imposibles, pero sí van a hacerte pensar de verdad.

---

## Desafío 1: El Clasificador de Torneos 🎮

Tienes una lista de jugadores que participaron en un torneo. Cada jugador es un diccionario con su nombre y su puntaje final.

```python
jugadores = [
    {'nombre': 'Nico',   'puntaje': 4200},
    {'nombre': 'Valeria','puntaje': 8750},
    {'nombre': 'Diego',  'puntaje': 3100},
    {'nombre': 'Camila', 'puntaje': 8750},
    {'nombre': 'Matías', 'puntaje': 6300},
]
```

**Lo que debes lograr:**

Recorre la lista y clasifica a cada jugador según su puntaje en una de tres categorías: `'Bronce'` (menos de 5000), `'Plata'` (entre 5000 y 7999), u `'Oro'` (8000 o más). Al final, imprime cuántos jugadores hay en cada categoría.

**Resultado esperado en consola:**
```
Bronce: 2
Plata: 1
Oro: 2
```

**Lo que lo hace difícil:** Necesitas un diccionario de contadores que empiece en cero, un `for` para recorrer jugadores, condicionales para clasificar, y actualizar el conteo en cada vuelta. Son cuatro piezas que deben funcionar juntas.

---

## Desafío 2: El Resumen de Ventas 🏪

Una tienda registró todas sus ventas del día. Cada venta tiene un vendedor y un monto.

```python
ventas = [
    {'vendedor': 'Ana',    'monto': 15000},
    {'vendedor': 'Pedro',  'monto': 32000},
    {'vendedor': 'Ana',    'monto': 21000},
    {'vendedor': 'Pedro',  'monto': 8000},
    {'vendedor': 'Carlos', 'monto': 45000},
]
```

**Lo que debes lograr:**

Genera un resumen donde cada vendedor aparezca una sola vez con el total de todo lo que vendió. Al terminar, imprime el nombre del vendedor que más vendió y cuánto fue su total.

**Resultado esperado en consola:**
```
Ana: 36000
Pedro: 40000
Carlos: 45000
Ganador: Carlos con 45000
```

**Lo que lo hace difícil:** Debes construir un diccionario de totales mientras recorres la lista. Para encontrar al ganador, necesitas recorrer ese diccionario con otro `for`, rastreando el máximo con variables auxiliares, igual que hiciste en el matchmaking de ELO, pero esta vez tú decides la estructura de datos.

---

## Desafío 3: El Simulador de Cola de Banco 🏦

Un banco tiene una fila de clientes esperando ser atendidos. Cada cliente tiene un tipo de trámite que toma un tiempo diferente en minutos.

```python
cola = [
    {'nombre': 'Laura',   'tramite': 'depósito',    'minutos': 5},
    {'nombre': 'Roberto', 'tramite': 'crédito',     'minutos': 20},
    {'nombre': 'Sofía',   'tramite': 'depósito',    'minutos': 5},
    {'nombre': 'Marcelo', 'tramite': 'hipoteca',    'minutos': 35},
    {'nombre': 'Ignacia', 'tramite': 'depósito',    'minutos': 5},
]
```

**Lo que debes lograr:**

Simula la atención uno a uno. El banco cierra cuando han pasado **45 minutos** desde que abrió. Si atender al siguiente cliente haría superar ese límite, ese cliente y todos los que siguen deben quedar en una lista llamada `sin_atender`. Al terminar, imprime a los clientes que **sí fueron atendidos** y a los que **quedaron fuera**.

**Resultado esperado en consola:**
```
Atendidos: ['Laura', 'Roberto', 'Sofía', 'Marcelo']
Sin atender: ['Ignacia']
```

**Lo que lo hace difícil:** Necesitas un acumulador de tiempo, dos listas que se van llenando según una condición, y entender que no es un filtro simple: una vez que el tiempo se agota, todos los siguientes van automáticamente a `sin_atender` sin ni siquiera revisar su tiempo.

---

## Desafío 4: El Motor de Descuentos por Categoría 🛒

Una tienda online aplica descuentos distintos según la categoría del producto. Las reglas son:

- `'tecnología'` → 15% de descuento
- `'ropa'` → 25% de descuento
- `'alimentos'` → sin descuento

```python
carrito = [
    {'producto': 'Notebook',  'categoria': 'tecnología', 'precio': 600000},
    {'producto': 'Polera',    'categoria': 'ropa',       'precio': 18000},
    {'producto': 'Pan',       'categoria': 'alimentos',  'precio': 2500},
    {'producto': 'Audífonos', 'categoria': 'tecnología', 'precio': 45000},
    {'producto': 'Jeans',     'categoria': 'ropa',       'precio': 35000},
]
```

**Lo que debes lograr:**

Calcula el precio final de cada producto después de su descuento. Imprime cada producto con su precio original y su precio final. Al terminar, imprime el **total a pagar** por todo el carrito.

**Resultado esperado en consola:**
```
Notebook: 600000 → 510000.0
Polera: 18000 → 13500.0
Pan: 2500 → 2500
Audífonos: 45000 → 38250.0
Jeans: 35000 → 26250.0
Total: 590500.0
```

**Lo que lo hace difícil:** El truco no está en los números: está en que las reglas de descuento están en un diccionario separado que tú debes crear, y dentro del `for` debes consultarlo dinámicamente usando la categoría del producto como llave. Es la primera vez que usas un diccionario como tabla de configuración.

---

## Desafío 5: El Analizador de Partidas 🕹️

Al terminar una sesión de juego, el sistema registra si cada partida fue ganada o perdida, y el tiempo que duró en minutos.

```python
partidas = [
    {'resultado': 'victoria', 'minutos': 32},
    {'resultado': 'derrota',  'minutos': 18},
    {'resultado': 'victoria', 'minutos': 45},
    {'resultado': 'derrota',  'minutos': 22},
    {'resultado': 'victoria', 'minutos': 38},
    {'resultado': 'derrota',  'minutos': 11},
]
```

**Lo que debes lograr:**

Con un solo `for` que recorra la lista una única vez, calcula todo lo siguiente:

1. Total de victorias y total de derrotas.
2. Tiempo total jugado (todas las partidas sumadas).
3. Duración promedio **solo de las victorias** (suma de minutos de victorias ÷ número de victorias).

Imprime los cuatro valores al final.

**Resultado esperado en consola:**
```
Victorias: 3
Derrotas: 3
Tiempo total: 166 minutos
Promedio victorias: 38.33 minutos
```

**Lo que lo hace difícil:** Todo debe salir de un único recorrido. Necesitas mantener al menos cinco variables acumuladoras en paralelo, actualizar las correctas en cada iteración según la condición, y calcular el promedio recién al final, fuera del ciclo. Si lo haces con varios `for`, estás repitiendo trabajo: el desafío es resolverlo todo de una pasada.

---

---

## Desafío 6: El Sistema de Reputación ⭐

Una plataforma de servicios como Airbnb guarda las reseñas que los usuarios le dejan a cada anfitrión. Cada reseña tiene el nombre del anfitrión y una nota del 1 al 5.

```python
resenas = [
    {'anfitrion': 'Mario',   'nota': 5},
    {'anfitrion': 'Claudia', 'nota': 3},
    {'anfitrion': 'Mario',   'nota': 4},
    {'anfitrion': 'Claudia', 'nota': 5},
    {'anfitrion': 'Mario',   'nota': 2},
    {'anfitrion': 'Claudia', 'nota': 4},
    {'anfitrion': 'Mario',   'nota': 5},
]
```

**Lo que debes lograr:**

Recorre la lista una sola vez y construye, al mismo tiempo, dos diccionarios: uno llamado `totales` que acumule la suma de notas por anfitrión, y otro llamado `conteos` que lleve la cuenta de cuántas reseñas tiene cada uno. Ambos deben empezar vacíos y llenarse dinámicamente dentro del `for`.

Una vez terminado el recorrido, calcula el promedio de cada anfitrión dividiendo su total entre su conteo. Imprime el promedio de cada uno redondeado a 2 decimales y, al final, imprime quién tiene la mejor reputación.

**Resultado esperado en consola:**
```
Mario: 4.0
Claudia: 4.0
Empate en reputación
```

> **Nota:** Sí, en este caso específico hay empate. Tu código debe detectarlo y manejarlo. Si no hubiera empate, debería imprimir al ganador con su promedio.

**Lo que lo hace difícil:** Aquí no te damos la estructura de los diccionarios lista. Tú debes inicializar las llaves dinámicamente: antes de sumar, tienes que revisar si el anfitrión ya existe en el diccionario; si no existe, crearlo con valor inicial. Es el patrón más importante en el manejo de datos agrupados, y para resolverlo necesitas coordinar dos diccionarios en paralelo dentro del mismo ciclo, más un segundo recorrido para calcular promedios y detectar empates. Son más de seis decisiones de lógica en cadena.

---

## Desafío 7: El Simulador de Ligas 🏟️

Este es el más complejo del set. Tienes los resultados de todos los partidos de una liga de fútbol. Cada partido registra al equipo local, al equipo visita y los goles de cada uno.

```python
partidos = [
    {'local': 'Colo-Colo', 'visita': 'La U',      'goles_local': 3, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Audax',      'goles_local': 0, 'goles_visita': 0},
    {'local': 'Audax',     'visita': 'Colo-Colo',  'goles_local': 1, 'goles_visita': 2},
    {'local': 'Colo-Colo', 'visita': 'Audax',      'goles_local': 1, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Colo-Colo',  'goles_local': 2, 'goles_visita': 2},
    {'local': 'Audax',     'visita': 'La U',        'goles_local': 0, 'goles_visita': 3},
]
```

**Las reglas de puntuación son las del fútbol real:**
- Victoria → 3 puntos para el ganador, 0 para el perdedor.
- Empate → 1 punto para cada equipo.

**Lo que debes lograr:**

Construye la tabla de posiciones de la liga desde cero. Al final, imprime los equipos ordenados de mayor a menor puntaje con sus puntos, y declara al campeón.

**Resultado esperado en consola:**
```
1. Colo-Colo — 7 pts
2. La U — 5 pts
3. Audax — 1 pts
Campeón: Colo-Colo
```

**Lo que lo hace difícil:** Este desafío tiene cuatro fases y ninguna es trivial.

**Fase 1 — Registro dinámico:** Al igual que en el desafío anterior, debes construir el diccionario de puntos en blanco y agregar equipos dinámicamente. Pero aquí hay dos equipos por partido, así que tienes que hacer ese chequeo dos veces por vuelta de ciclo.

**Fase 2 — Lógica de partido:** Dentro del `for`, debes determinar el resultado del partido comparando `goles_local` con `goles_visita` y repartir los puntos correctamente a cada equipo usando los corchetes del diccionario.

**Fase 3 — Ordenamiento manual:** Python tiene `.sort()`, pero aquí no lo has visto. Tendrás que ordenar la tabla tú mismo: usando el patrón de búsqueda de máximo que ya conoces, pero repetido para construir una nueva lista ordenada. Esta es la parte que más va a hacer pensar.

**Fase 4 — Impresión con posición:** Al imprimir, necesitas un contador de posición (1°, 2°, 3°...) que avance junto con el recorrido de la lista ordenada.

Cuatro fases encadenadas, ninguna ayuda en el código, solo los datos. Si llegas al resultado correcto, realmente ya no eres principiante.

---

*Hecho con 🔥 para Fundamentos de Programación 2026 — Nivel Post-55*