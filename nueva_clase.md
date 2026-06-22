# Opción B — Sistema de gestión de personajes desbloqueables

## FICHA 4 — Versión Adaptada
**Enunciado prueba parcial 4 (Adaptación)**
*Listas, diccionarios, funciones*

| Sigla | Asignatura | Experiencia de Aprendizaje |
|---|---|---|
| FPY1101 | Fundamentos de Programación | EA3: Colecciones y funciones en Python |

| Tiempo | Modalidad de Trabajo | Indicadores de logro |
|---|---|---|
| 1 h | Individual | IL 3.1 al IL 4.2 |

### Resolver

Desarrolla un programa en Python que implemente un sistema de gestión de personajes desbloqueables de un videojuego, donde todo el comportamiento se organice mediante funciones bien definidas. El programa debe incluir un menú interactivo, validaciones de entrada, una operación de decisión simple y uso de funciones separadas.

### 1. Datos que debe manejar el sistema

El sistema trabaja con una colección de personajes. Esta colección debe existir desde que el programa inicia y estar disponible durante toda la ejecución. Cada vez que se agrega un personaje, se incorpora a esa colección como un nuevo elemento.

Cada personaje se representa como un conjunto de campos asociados: nombre, nivel y un indicador de si está desbloqueado o no.

| Campo | Qué representa | Restricciones de validación |
|---|---|---|
| `"nombre"` | Nombre del personaje | No vacío ni solo espacios en blanco |
| `"nivel"` | Nivel del personaje | Número entero mayor que 0 |
| `"desbloqueado"` | ¿El personaje está desbloqueado? | **False al registrar.** No se valida ni se solicita al usuario: el sistema lo asigna automáticamente. Su valor puede cambiar a True cuando se ejecute la opción 4 (Actualizar desbloqueo), según el nivel del personaje. |

Cada diccionario se guarda dentro de una lista. La lista es la colección general; los diccionarios son los personajes individuales dentro de ella. El programa comienza con la lista vacía y la va llenando a medida que se agregan registros.

### 2. Lo que debe hacer el sistema

El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú. Esto se repite hasta que el usuario elige salir.

El menú tiene seis opciones:

```
========== MENÚ PRINCIPAL ==========
1. Agregar personaje
2. Buscar personaje
3. Eliminar personaje
4. Actualizar desbloqueo
5. Mostrar personajes
6. Salir
=====================================
```

Para implementar este comportamiento debes definir dos funciones separadas: una que muestre las opciones en pantalla (sin recibir nada ni retornar nada) y otra que lea y retorne la opción elegida por el usuario (sin recibir nada, retornando el número validado). Ambas funciones deben invocarse en cada vuelta del ciclo.

A continuación, se describe qué debe ocurrir al elegir cada opción:

**Opción 1 — Agregar personaje**

El sistema solicita al usuario el nombre y el nivel del personaje. Antes de guardar el registro, verifica que cada dato cumpla su condición:
- El nombre no puede estar vacío ni ser solo espacios en blanco.
- El nivel debe ser un número entero mayor que 0.

Si algún dato no cumple la condición, el sistema informa al usuario y no registra el personaje. Solo cuando todos los datos son válidos se crea el diccionario y se agrega a la lista.

Para implementar esta opción debes definir una función que reciba la lista como parámetro. Dentro de ella se solicitan los datos al usuario y se llama a una función de validación distinta para cada campo. Los mensajes de error se muestran en esta función, no dentro de las validaciones.

**Opción 2 — Buscar personaje**

El sistema solicita un nombre de personaje al usuario y recorre la lista buscando un registro cuyo campo nombre coincida exactamente con el ingresado. Si lo encuentra, muestra la posición en la que está y sus datos. Si no existe ningún registro con ese nombre, informa al usuario.

Para implementar esta opción debes definir una función que reciba la lista y el nombre a buscar como parámetros. La función recorre la lista y retorna la posición del registro encontrado, o -1 si no existe. Es el programa principal quien recibe ese valor y decide qué hacer con él: si la posición es válida, muestra los datos del personaje en esa posición; si es -1, muestra el mensaje de no encontrado.

**Opción 3 — Eliminar personaje**

El sistema solicita el nombre del personaje que se desea eliminar. Para localizarlo, llama a la función de búsqueda definida en la opción anterior, pasándole la lista y el nombre ingresado. Si la función retorna una posición válida, el sistema elimina el registro en esa posición. Si retorna -1, informa al usuario con el siguiente mensaje:

*El personaje 'nombre' no se encuentra registrado.*

**Opción 4 — Actualizar desbloqueo**

El sistema recorre la lista completa de personajes y actualiza el campo `"desbloqueado"` de cada registro según su nivel: si el nivel es mayor o igual a 5, el campo pasa a True; si es menor, queda en False. Esta operación afecta a todos los registros de la lista sin excepción.

Para implementar esta opción debes definir una función que reciba la lista como parámetro y aplique esa regla a cada elemento.

**Opción 5 — Mostrar personajes**

El sistema primero actualiza el desbloqueo de todos los personajes haciendo el llamado a la función anterior, luego recorre la lista mostrando los datos de cada personaje. El formato de salida es el siguiente:

```
=== LISTA DE PERSONAJES ===
Nombre: Ragnar
Nivel: 7
Estado: DESBLOQUEADO
********************************************
Nombre: Lyra
Nivel: 3
Estado: BLOQUEADO
*********************************************
```

**Opción 6 — Salir**

El sistema termina la ejecución de forma limpia, sin errores. El ciclo del menú se detiene y el programa finaliza con un mensaje de despedida:

*"Gracias por usar el sistema. Vuelva pronto"*

---

# Ejercicio alternativo propuesto — Catálogo de mascotas de granja

*Mismo nivel de dificultad y mismo menú de 6 opciones, pensado como versión de respaldo, segunda fecha, o recuperación.*

### Datos que debe manejar el sistema

El sistema trabaja con una colección de mascotas de una granja virtual. Cada mascota se representa como un conjunto de campos asociados: nombre, edad y un indicador de si está adulta o no.

| Campo | Qué representa | Restricciones de validación |
|---|---|---|
| `"nombre"` | Nombre de la mascota | No vacío ni solo espacios en blanco |
| `"edad"` | Edad de la mascota (en años) | Número entero mayor que 0 |
| `"adulta"` | ¿La mascota es adulta? | **False al registrar.** No se valida ni se solicita al usuario: el sistema lo asigna automáticamente. Su valor puede cambiar a True cuando se ejecute la opción 4 (Actualizar madurez), según la edad de la mascota. |

### Menú principal (igual estructura)

```
========== MENÚ PRINCIPAL ==========
1. Agregar mascota
2. Buscar mascota
3. Eliminar mascota
4. Actualizar madurez
5. Mostrar mascotas
6. Salir
=====================================
```

### Reglas equivalentes a la opción A

- **Opción 1:** valida nombre (no vacío) y edad (entero mayor que 0); si todo es válido, agrega el diccionario a la lista.
- **Opción 2:** función que recibe lista y nombre, retorna posición o -1; el programa principal decide el mensaje.
- **Opción 3:** reusa la función de búsqueda de la opción 2; si retorna -1, muestra: *"La mascota 'nombre' no se encuentra registrada."*
- **Opción 4:** recorre toda la lista; si edad ≥ 3, `"adulta"` pasa a True; si no, queda en False.
- **Opción 5:** llama primero a la función de la opción 4, luego muestra todos los registros con el mismo formato de asteriscos usado en el ejercicio principal.
- **Opción 6:** mensaje de despedida y cierre limpio del ciclo.

