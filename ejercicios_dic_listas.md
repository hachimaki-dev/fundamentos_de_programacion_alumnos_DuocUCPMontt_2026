¡Hola! Como asistente de inteligencia artificial, me parece una excelente iniciativa preparar este material para tus estudiantes. Organizar los ejercicios progresivamente y proveerles un "acordeón" o guía de patrones al final de cada uno es una de las mejores formas de consolidar el aprendizaje en programación.

He unificado y ordenado los 12 ejercicios de menor a mayor complejidad, agrupándolos por los conceptos clave que deben dominar (Validación, Menús interactivos, Estructuras de datos básicas, y Operaciones avanzadas).

Aquí tienes el documento completo en formato Markdown, listo para que lo compartas con ellos.

---

# Guía Práctica de Programación: Patrones y Estructuras de Datos

Esta guía está diseñada para que practiques patrones de código paso a paso. Los ejercicios aumentan de dificultad progresivamente. Al final de cada ejercicio encontrarás una **Tabla de Referencia** con trucos, funciones y explicaciones para ayudarte a resolverlo.

---

## FASE 1: Fundamentos de Control de Flujo y Validación

### Ejercicio 1 — Formulario básico de validación

**Contexto:** Estás construyendo un formulario de registro básico.

**Lo que debe hacer el programa:**
Pide al usuario que ingrese su edad. La edad debe ser un número entero positivo (mayor a 0). Si el usuario ingresa algo inválido (letras, cero, número negativo), el programa debe mostrar: `"Entrada inválida. Ingresa un número entero positivo."` y volver a preguntar. Cuando el valor sea válido, muestra: `"Edad registrada: X años."`

**Ejemplos:**

```text
Ingresa tu edad: hola
Entrada inválida. Ingresa un número entero positivo.
Ingresa tu edad: -5
Entrada inválida. Ingresa un número entero positivo.
Ingresa tu edad: 0
Entrada inválida. Ingresa un número entero positivo.
Ingresa tu edad: 22
Edad registrada: 22 años.

```

**💡 Pistas:**

* Usa un bucle `while True` que solo se rompa (`break`) cuando el valor sea válido.
* Para detectar si algo no es número, investiga el uso de `try / except ValueError`.
* La condición de número positivo va **dentro** del `try`, después de convertir el valor.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Bucle Infinito** | `while True:`<br>

<br> `...código...` | Útil para forzar al usuario a responder bien. Se detiene solo cuando encuentra un `break`. |
| **Validar números (`try / except`)** | `try:`<br>

<br> `  num = int(input())`<br>

<br>`except ValueError:`<br>

<br> `  print("Error")` | Previene que el programa se caiga (crash) si el usuario escribe letras en lugar de números. |
| **Interrumpir bucle** | `break` | Debe ir justo después de comprobar que el dato es válido (ej. `if num > 0: break`). |

---

### Ejercicio 2 — Clasificación y contadores

**Contexto:** Un sistema escolar necesita clasificar notas de alumnos.

**Lo que debe hacer el programa:**
Pide al usuario cuántos alumnos desea registrar (entero positivo). Por cada alumno, solicita su nota (número entero entre 1 y 100). Clasifica automáticamente:

* Nota **mayor a 59** → `"Aprobado"`
* Nota **59 o menor** → `"Reprobado"`

Lleva la cuenta de cuántos aprobaron y cuántos reprobaron. Al final muestra: `"Resultado: X aprobados y Y reprobados."`

**Ejemplo:**

```text
¿Cuántos alumnos? 3
Nota alumno 1: 75  → Aprobado
Nota alumno 2: 45  → Reprobado
Nota alumno 3: 60  → Aprobado
Resultado: 2 aprobados y 1 reprobados.

```

**💡 Pistas:**

* Necesitas **dos contadores** que empiecen en `0` antes del bucle.
* Usa un bucle `for` si ya sabes cuántos alumnos son.
* La clasificación es un simple `if / else` sobre la nota.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Contadores** | `aprobados = 0`<br>

<br>`aprobados += 1` | Siempre inicializa los contadores **antes** del bucle. Súmales 1 dentro del bloque `if/else` correspondiente. |
| **Bucle For con Rango** | `for i in range(cantidad):` | `range(n)` ejecuta el bucle exactamente `n` veces. `i` tomará valores de `0` a `n-1`. |
| **Interpolación de strings** | `f"Nota alumno {i+1}:"` | Al usar `f""`, las variables entre llaves se reemplazan por su valor. `i+1` sirve para que empiece a contar desde 1 visualmente. |

---

### Ejercicio 3 — Sistema de registro de atletas

**Contexto:** El Centro Deportivo Nacional necesita registrar a sus atletas de nueva incorporación.

**Lo que debe hacer el programa:**

1. **Cantidad:** Pregunta cuántos atletas se registrarán. Debe ser entero positivo. Si no lo es, muestra `"¡Dato inválido! Ingresa un entero positivo para continuar."` y repregunta.
2. **Por cada atleta solicita:**
* **Código de atleta:** mínimo 5 caracteres, sin espacios, solo letras y números. Si es inválido: `"Código inválido. Debe tener al menos 5 caracteres, sin espacios y solo letras o números."`
* **Puntaje de rendimiento:** entero positivo. Si es inválido: `"¡Error! Ingresa un número entero positivo para el puntaje."`


3. **Clasificación automática:**
* Mayor a 70 → Atleta Élite
* 70 o menor → Atleta Regular


4. **Resumen final:** `"¡El centro cuenta con X Atletas Élite y Y Atletas Regulares! ¡Registro completado!"`

**💡 Pistas:**

* Es el mismo flujo que el ejercicio anterior, pero agregando las validaciones del Ejercicio 1.
* Valida el código con `len()`, `.isalnum()` y `" " not in codigo`.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Validar longitud** | `if len(codigo) >= 5:` | `len()` devuelve la cantidad de caracteres de un string. |
| **Validar Alfanumérico** | `codigo.isalnum()` | Devuelve `True` si el texto SOLO contiene letras y números (sin guiones, puntos, etc.). |
| **Buscar caracteres (espacios)** | `" " not in codigo` | Es una forma rápida de verificar que el usuario no escribió espacios en blanco dentro de la palabra. |

---

## FASE 2: Menús Interactivos y Estado del Programa

### Ejercicio 4 — Menú interactivo (Calculadora)

**Contexto:** Una calculadora de sesión simple.

**Lo que debe hacer el programa:**
Muestra un menú que se repite hasta que el usuario elija salir:

```text
=== CALCULADORA ===
1. Sumar número al total
2. Ver total acumulado
3. Reiniciar total
4. Salir

```

* Opción 1: pide un número entero y lo suma al total acumulado (empieza en 0).
* Opción 2: muestra el total actual.
* Opción 3: reinicia el total a 0.
* Opción 4: imprime `"Hasta luego."` y termina.
* Opción inválida: `"Opción no reconocida. Intenta de nuevo."`

**💡 Pistas:**

* Usa `while True` para el menú; la única salida es `break` en la opción 4.
* El total acumulado es una variable que se define **antes** del bucle.
* Lee la opción como `input()` y compárala con strings `"1"`, `"2"`, etc., o conviértela a entero con `int()` dentro de un `try/except`.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Estructura de Menú** | `if op == "1":`<br>

<br> `elif op == "2":`<br>

<br> `else:` | Tratar la opción como *string* (`"1"`) evita usar `try/except` si el usuario ingresa letras accidentalmente en el menú. |
| **Acumuladores** | `total = 0`<br>

<br>`total += numero` | Diferente a un contador (que suma de 1 en 1). El acumulador suma valores variables a lo largo del tiempo. |
| **Reiniciar Estado** | `total = 0` | Si el usuario elige reiniciar, simplemente sobreescribes la variable a su valor inicial. |

---

### Ejercicio 5 — Sistema de gestión de biblioteca

**Contexto:** La Biblioteca Central necesita un sistema para gestionar su stock de libros disponibles para préstamo. Inicia con **30 libros disponibles**.

**Lo que debe hacer el programa:**
Muestra un `"¡Bienvenido al sistema de préstamos de la Biblioteca Central!"` y un menú que se repite:

```text
=== MENÚ PRINCIPAL ===
1. Libros disponibles
2. Registrar préstamo
3. Registrar devolución
4. Movimientos de la sesión
5. Salir

```

* **Opción 1:** Muestra cuántos libros hay disponibles actualmente.
* **Opción 2 (préstamo):** Pide cuántos libros se prestan. Valida que sea > 0 y no supere los disponibles. Actualiza el stock.
* **Opción 3 (devolución):** Pide cuántos libros se devuelven. Valida que sea > 0 y que no supere la capacidad máxima (30). Actualiza el stock.
* **Opción 4:** Muestra el historial neto (préstamos − devoluciones) de la sesión.
* **Opción 5:** `"Gracias por usar el sistema de la biblioteca. ¡Hasta pronto!"` y cierra.
* **Opción inválida:** `"Opción no válida. Elige entre 1 y 5."`

**💡 Pistas:**

* Necesitas tres variables antes del bucle: `disponibles`, `capacidad_maxima` e `historial_neto`.
* El historial neto **suma** con cada préstamo y **resta** con cada devolución.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Validar Límites (Inferior)** | `if prestamo <= disponibles:` | Evita que el inventario quede en números negativos (no puedes prestar lo que no tienes). |
| **Validar Límites (Superior)** | `if devueltos + disp <= max:` | Evita superar la capacidad máxima de tu programa. |
| **Variable Historial (Neto)** | `historial += prestamo`<br>

<br> `historial -= devueltos` | Un solo acumulador puede sumar y restar para llevar un balance neto general. |

---

### Ejercicio 6 — Sistema de gestión de estacionamiento

**Contexto:** Un estacionamiento público tiene capacidad para **20 vehículos**. Necesita un sistema para controlar entradas y salidas. Inicia con **20 espacios disponibles**.

**Lo que debe hacer el programa:**
Muestra un `"¡Bienvenido al sistema de control del Estacionamiento Central!"` y el menú:

```text
=== PANEL DE CONTROL ===
1. Espacios disponibles
2. Registrar entrada de vehículo
3. Registrar salida de vehículo
4. Resumen de la jornada
5. Salir

```

* **Opción 1:** Muestra los espacios libres actuales.
* **Opción 2 (entrada):** Pide cuántos vehículos ingresan. Valida que sea > 0 y no supere los espacios disponibles. Si no hay espacio: `"No hay suficientes espacios. Solo quedan X lugares."`.
* **Opción 3 (salida):** Pide cuántos vehículos salen. Valida que sea > 0 y que al liberar espacios no se supere la capacidad máxima (20). Si se superaría: `"Operación inválida. Se superaría la capacidad máxima del estacionamiento."`.
* **Opción 4:** Muestra el total neto de vehículos ingresados durante la jornada (entradas − salidas).
* **Opción 5:** `"Cerrando sistema. ¡Hasta mañana!"` y termina.
* **Opción inválida:** `"Opción no reconocida. Selecciona del 1 al 5."`.

**💡 Pistas:**

* La lógica de entrada/salida es idéntica al check-in/check-out de la biblioteca.
* Declara `espacios_disponibles = 20`, `capacidad_maxima = 20` y `jornada_neta = 0` antes del bucle principal.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Replicar Patrones** | *Mismos conceptos que Ejercicio 5* | **FAQ:** *¿Por qué un ejercicio igual?* Para que notes que el **dominio** cambia (libros vs autos), pero la **lógica** es la misma. |
| **Gestión de Stock Inverso** | `disponibles -= entradas`<br>

<br> `disponibles += salidas` | Al igual que con los libros (prestar resta, devolver suma), aquí un auto entrando **resta** un espacio disponible, y uno saliendo lo **suma**. |

---

## FASE 3: Estructuras de Datos (Listas y Diccionarios)

### Ejercicio 7 — Crear y recorrer una lista de diccionarios (Fijo)

**Contexto:** Una clínica quiere guardar el registro básico de sus pacientes.

**Lo que debe hacer el programa:**
Pide al usuario que ingrese exactamente **3 pacientes**. Por cada uno solicita:

* **Nombre** (solo texto, no vacío)
* **Edad** (entero positivo)

Guarda cada paciente como diccionario en una lista. Al finalizar, muestra todos así:

```text
--- Lista de Pacientes ---
Nombre: Ana | Edad: 34
Nombre: Luis | Edad: 28
Nombre: María | Edad: 45

```

**💡 Pistas:**

* Lista vacía antes del bucle: `pacientes = []`.
* Cada diccionario tiene dos claves: `"nombre"` y `"edad"`.
* Para mostrar, recorre la lista con `for p in pacientes:` y accede con `p["nombre"]`, `p["edad"]`.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Crear Lista Vacía** | `mi_lista = []` | Se declara fuera y antes del bucle para que los datos no se borren en cada vuelta. |
| **Crear e Insertar Diccionario** | `paciente = {"nombre": nom, "edad": ed}`<br>

<br> `mi_lista.append(paciente)` | Agrupa múltiples datos de una misma entidad. `.append()` lo agrega al final de la lista. |
| **Recorrer Lista de Diccionarios** | `for p in mi_lista:`<br>

<br> `  print(p["nombre"])` | En el bucle `for`, `p` representa el diccionario completo de esa vuelta. Accedes a los datos mediante sus claves en corchetes. |

---

### Ejercicio 8 — Inventario dinámico de productos

**Contexto:** Una tienda quiere guardar su inventario de productos.

**Lo que debe hacer el programa:**
Pide al usuario cuántos productos desea registrar. Por cada producto solicita:

* **Nombre** del producto (mínimo 3 caracteres, sin espacios)
* **Precio** (número entero positivo)

Guarda cada producto como un diccionario dentro de una lista. Al finalizar, muestra todos los productos registrados en este formato:

```text
--- Inventario ---
Producto: Manzana | Precio: $200
Producto: Pan | Precio: $150

```

**💡 Pistas:**

* Cada producto es un diccionario: `{"nombre": "Manzana", "precio": 200}`.
* Mezcla el patrón de validación (Fase 1) con el patrón de lista de diccionarios (Fase 3).

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Bucle Anidado (Concepto)** | `for i in range(cant):`<br>

<br> `  while True:` | Usas el `for` para iterar sobre la cantidad de productos, y dentro de él, un `while True` para validar el nombre o precio de ese producto específico. |
| **Formateo de Moneda** | `print(f"Precio: ${p['precio']}")` | Presta atención al uso de comillas. Si tu f-string usa comillas dobles `" "`, la clave del diccionario adentro debe usar simples `' '`. |

---

### Ejercicio 9 — Registro y clasificación de voluntarios

**Contexto:** Una ONG necesita registrar a sus nuevos voluntarios y clasificarlos por disponibilidad.

**Lo que debe hacer el programa:**

1. **Cantidad:** Pregunta cuántos voluntarios se registrarán (entero positivo con validación).
2. **Por cada voluntario solicita:**
* **Nombre clave:** mínimo 4 caracteres, sin espacios, solo letras y números.
* **Horas disponibles por semana:** entero positivo.


3. **Clasificación:**
* Mayor a 20 → Voluntario Dedicado
* 20 o menos → Voluntario Casual


4. Guarda cada voluntario como **diccionario** en una lista (con nombre, horas y categoría).
5. **Resumen final:** `"La ONG tiene X Voluntarios Dedicados y Y Voluntarios Casuales. ¡Gracias por su apoyo!"`

**💡 Pistas:**

* La clasificación y los contadores van **dentro del mismo bucle** donde registras cada voluntario.
* Agrega la categoría directamente al diccionario: `{"nombre": n, "horas": h, "categoria": cat}`.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Diccionarios más complejos** | `vol = {"nom": n, "cat": c}`<br>

<br>`lista.append(vol)` | No hay límite práctico para cuántas claves puedes poner en un diccionario. |
| **Uniendo Patrones** | *Validación + Estructuras + Contadores* | Este ejercicio simula una aplicación real básica donde recolectas datos, los limpias (validas), los clasificas, los guardas y muestras un reporte. |

---

## FASE 4: Operaciones Avanzadas (Búsqueda, Filtros y CRUD)

### Ejercicio 10 — Búsqueda en una lista de diccionarios

**Contexto:** El sistema de pacientes de la clínica (Ejercicio 7), ahora con búsqueda.

**Lo que debe hacer el programa:**
Repite el registro de 3 pacientes con nombre y edad, pero al finalizar, el programa pregunta: `"¿Qué nombre deseas buscar?"`. Busca ese nombre en la lista (sin distinguir mayúsculas de minúsculas). Si lo encuentra, muestra sus datos. Si no, muestra `"Paciente no encontrado."`.

**Ejemplo:**

```text
¿Qué nombre deseas buscar? ana
Paciente encontrado → Nombre: Ana | Edad: 34

```

**💡 Pistas:**

* Usa `.lower()` tanto en el nombre guardado como en el nombre buscado para comparar sin importar mayúsculas.
* Usa una variable bandera (`encontrado = False`) que cambia a `True` si lo encuentras.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Banderas (Flags) Booleanas** | `encontrado = False`<br>

<br>`if coincidencia:`<br>

<br> `  encontrado = True` | Sirve para "recordar" si un evento sucedió dentro de un bucle. Fuera del bucle usas `if not encontrado: print("No existe")`. |
| **Normalización de Texto** | `if p["nombre"].lower() == busq.lower():` | Estandariza los strings antes de compararlos. "AnA".lower() y "ana".lower() ambos resultan en "ana", permitiendo la coincidencia. |

---

### Ejercicio 11 — Filtrar y promediar desde una lista

**Contexto:** Un gimnasio quiere analizar su lista de miembros.

**Lo que debe hacer el programa:**
Pide cuántos miembros registrar (entero positivo). Por cada miembro solicita nombre clave y meses de membresía. Guarda todo en una lista de diccionarios. Al finalizar:

1. Muestra **todos** los miembros registrados.
2. Muestra **solo los miembros con más de 6 meses** (miembros frecuentes).
3. Muestra el **promedio de meses** de todos los miembros.

**Ejemplo de salida:**

```text
--- Todos los Miembros ---
Nombre: AlphaRun | Membresía: 12 meses
Nombre: BetaJog | Membresía: 4 meses
Nombre: GammaSprint | Membresía: 6 meses

--- Miembros frecuentes (más de 6 meses) ---
Nombre: AlphaRun | Membresía: 12 meses

Promedio de membresía: 7.33 meses
```

**💡 Pistas:**

* Para el promedio: suma todos los meses y divide por el total de miembros.
* Formatea el promedio con dos decimales usando `f"{promedio:.2f}"`.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Filtrado Visual** | `if m["meses"] > 6:`<br>

<br> `  print(m["nombre"])` | Puedes recorrer toda la lista y usar un `if` para imprimir o procesar *solo* aquellos elementos que cumplan una condición. |
| **Cálculo de Promedio** | `prom = suma_total / len(lista)` | Asegúrate de que la lista no esté vacía antes de dividir, ¡o te dará un error de división por cero (`ZeroDivisionError`)! |
| **Formateo de Decimales** | `f"Promedio: {prom:.2f}"` | El `:.2f` dentro de la llave le dice a Python que redondee a 2 decimales fijos. |

---

### Ejercicio 12 — Modificar y eliminar (CRUD) en listas

**Contexto:** Un pequeño almacén necesita gestionar su lista de productos con opciones de edición.

**Lo que debe hacer el programa:**
Inicia con esta lista ya cargada (no hace falta pedirla al usuario):

```python
productos = [
    {"nombre": "Arroz", "stock": 50},
    {"nombre": "Aceite", "stock": 20},
    {"nombre": "Harina", "stock": 35}
]

```

Muestra un menú que se repite hasta que el usuario salga:

```text
=== GESTIÓN DE PRODUCTOS ===
1. Ver todos los productos
2. Actualizar stock de un producto
3. Eliminar un producto
4. Salir

```

* **Opción 1:** Muestra nombre y stock.
* **Opción 2:** Pide el nombre del producto y nuevo stock. Si no existe: `"Producto no encontrado."`. Si existe, lo actualiza.
* **Opción 3:** Pide el nombre del producto. Si existe, lo elimina de la lista. Si no: `"Producto no encontrado."`.

**💡 Pistas:**

* Para buscar, recorre la lista con `for i, p in enumerate(productos):` — el `i` te da la posición numérica.
* Para **actualizar**: `productos[i]["stock"] = nuevo_stock`.
* Para **eliminar**: `productos.pop(i)` elimina el elemento en esa posición. Usa un `break` en el bucle después de eliminar para evitar errores de índice.

**Tabla de Referencia y Patrones**

| Concepto / Herramienta | Código de Ejemplo / Explicación | Tips / FAQ |
| --- | --- | --- |
| **Indexación en Bucle (`enumerate`)** | `for i, p in enumerate(lista):` | `enumerate()` te entrega tanto el índice (`0`, `1`, `2`...) como el elemento (el diccionario) en cada vuelta. |
| **Actualizar Diccionario** | `lista[i]["clave"] = valor` | Navegas a la lista en la posición `[i]`, entras a la clave del diccionario, y le asignas un nuevo valor con `=`. |
| **Eliminar por Índice** | `lista.pop(i)` | Remueve el elemento en la posición `i`. **Regla de oro:** Tras hacer `.pop()` mientras iteras sobre una lista, debes usar `break`, o alterarás la iteración y causará un error. |