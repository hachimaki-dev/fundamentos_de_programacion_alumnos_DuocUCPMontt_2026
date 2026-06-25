Perfecto. Ya analicé los tres enunciados y tengo clarísimo el patrón: dos diccionarios relacionados, mismo código como clave, 6 opciones de menú (consulta por categoría, búsqueda por rango, actualizar, agregar con validaciones individuales, eliminar, salir).

Acá va el enunciado completo 👇

---

## Evaluación Práctica — FPY1101
**Fundamentos de Programación | Tiempo sugerido: 4 horas**

---

### Instrucciones

La plataforma de streaming **AniStream** requiere un programa en Python para administrar su catálogo de series de anime y la disponibilidad de episodios por serie. Todo el comportamiento del sistema debe organizarse en funciones bien definidas. El programa incluye un menú interactivo, validaciones de entrada y una separación clara entre la lógica de cada función y las decisiones del programa principal.

---

### 1. Datos que debe manejar el sistema

El sistema trabaja con **dos diccionarios relacionados**, ambos identificados por el mismo código de serie como clave. Estos diccionarios deben existir desde que el programa inicia y permanecer disponibles durante toda la ejecución.

---

**Diccionario `series`**

Contiene la información descriptiva de cada anime. La **clave** es el código de la serie y el **valor** es una lista con los siguientes campos, en este orden:

| **Campo** | **Qué representa** | **Restricciones de validación** |
|---|---|---|
| `"titulo"` | Nombre de la serie | No debe contener solo espacios en blanco ni estar vacío |
| `"genero"` | Género de la serie | No debe contener solo espacios en blanco ni estar vacío |
| `"estudio"` | Estudio de animación | No debe contener solo espacios en blanco ni estar vacío |
| `"clasificacion"` | Clasificación de audiencia | Debe ser exactamente `'G'`, `'PG'` o `'M'` |
| `"subtitulado"` | Indica si la serie está subtitulada al español | El usuario ingresa `'s'` o `'n'`. El sistema lo convierte a `True` o `False` |
| `"pais_origen"` | País de origen de la serie | No debe contener solo espacios en blanco ni estar vacío |

Los puntos suspensivos indican que pueden existir más registros:

```python
series = {
    'AN001': ['Attack on Titan',    'accion',  'MAPPA',      'M',  False, 'Japon'],
    'AN002': ['Your Name',          'romance', 'CoMix Wave', 'PG', True,  'Japon'],
    'AN003': ['One Punch Man',      'comedia', 'J.C.Staff',  'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yaiba',   'accion',  'ufotable',   'PG', True,  'Japon'],
    'AN005': ['No Game No Life',    'isekai',  'Madhouse',   'PG', True,  'Japon'],
    'AN006': ['Violet Evergarden',  'drama',   'KyoAni',     'G',  True,  'Japon'],
    ...
}
```

---

**Diccionario `catalogo`**

Contiene la información operativa de cada serie. La **clave** es el mismo código de serie y el **valor** es una lista con los siguientes dos campos:

| **Campo** | **Qué representa** | **Restricciones de validación** |
|---|---|---|
| `"precio"` | Precio mensual de acceso a la serie en pesos | Número entero mayor que cero |
| `"episodios"` | Cantidad de episodios disponibles para ver | Número entero mayor o igual a cero |

```python
catalogo = {
    'AN001': [9990,  75],
    'AN002': [4990,   0],
    'AN003': [7990,  12],
    'AN004': [8990,  26],
    'AN005': [5990,  13],
    'AN006': [6990,  13],
    ...
}
```

---

### 2. Lo que debe hacer el sistema

El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El usuario elige una opción numérica, el programa ejecuta la tarea y vuelve a mostrar el menú. Esto se repite hasta que el usuario elige salir. Si el usuario ingresa un valor que no corresponda a ninguna opción válida, el sistema muestra *"Debe seleccionar una opción válida"* y vuelve a mostrar el menú.

```
========== MENÚ PRINCIPAL ==========
1. Episodios por género
2. Búsqueda de series por rango de precio
3. Actualizar precio de serie
4. Agregar serie
5. Eliminar serie
6. Salir
=====================================
```

---

**Opción 1 — Episodios por género**

El sistema solicita al usuario el nombre de un género (por ejemplo: `accion`, `romance`, `isekai`). La búsqueda **no distingue entre mayúsculas y minúsculas**, por lo que `"accion"` y `"ACCION"` deben producir el mismo resultado. El sistema recorre el diccionario **`series`** identificando todas las series que pertenezcan a ese género. Por cada serie encontrada, debe buscar su código en el diccionario **`catalogo`**, extraer la cantidad de episodios disponibles (el segundo elemento de la lista) y acumularla en un total. Una vez procesadas todas las series encontradas, se debe mostrar dicho total acumulado en pantalla.

**Para implementar esta opción:**
Define una función llamada **`episodios_genero(genero)`**. Recibe el género como parámetro, **no retorna ningún valor** y muestra el resultado directamente por pantalla.

---

**Opción 2 — Búsqueda de series por rango de precio**

El sistema solicita al usuario un precio mínimo y un precio máximo. Luego recorre el diccionario **`catalogo`** y construye una lista con todas las series que: **(a)** tengan un precio dentro del rango ingresado, y **(b)** tengan episodios disponibles (episodios distintos de cero). Cada elemento de la lista tiene el formato `"Titulo--Codigo"`. Los resultados se muestran ordenados **alfabéticamente por título**. Si no hay series que cumplan las condiciones, el sistema muestra: *"No hay series en ese rango de precios."*

**Restricciones de entrada:**
El precio mínimo y máximo deben ingresarse como valores enteros. Esta validación ocurre en el **programa principal**, antes de llamar a la función. Como el usuario puede ingresar cualquier tipo de dato, debe utilizarse manejo de excepciones. Si el dato ingresado no es un entero válido, el sistema muestra *"Debe ingresar valores enteros"* y vuelve a solicitar ambos valores.

**Para implementar esta opción:**
Define una función llamada **`busqueda_precio(p_min, p_max)`**. Recibe el precio mínimo y máximo como parámetros *(estos valores deben ser mayores o iguales a cero y el `p_min` debe ser menor o igual al `p_max`)*, **no retorna ningún valor** y muestra los resultados directamente por pantalla.

---

**Opción 3 — Actualizar precio de serie**

El sistema solicita al usuario el código de la serie y el nuevo precio que se desea asignar. Si el código existe en el diccionario **`catalogo`**, el sistema actualiza su precio. Si el código no existe, informa al usuario. Al terminar, pregunta: *"¿Desea actualizar otro precio (s/n)?"*: si la respuesta es `"s"`, el proceso se repite; si es `"n"`, el programa vuelve al menú principal.

**Para implementar esta opción:**
Define una función llamada **`actualizar_precio(codigo, nuevo_precio)`**. Si el código **no existe**, retorna **`False`**. Si el código **existe**, actualiza el precio y retorna **`True`**. El **programa principal** recibe ese valor y decide qué mostrar: *"Precio actualizado"* si fue exitoso, o *"El código no existe"* si no lo fue.

Recordar que `nuevo_precio` debe ser un valor entero positivo y la validación del código **no debe distinguir mayúsculas y minúsculas**.

---

**Opción 4 — Agregar serie**

El sistema solicita al usuario todos los datos de la nueva serie: código, título, género, estudio, clasificación, si está subtitulada, país de origen, precio y episodios. Antes de crear el registro, **cada dato es validado de forma independiente**. Si algún dato no cumple su condición, el sistema informa al usuario y **no registra la serie**. Solo cuando todos los datos son válidos y el código no existe previamente, el sistema agrega el registro en ambos diccionarios.

La siguiente tabla resume las condiciones que debe cumplir cada campo:

| **Campo solicitado** | **Condición de validación** |
|---|---|
| código | No vacío ni solo espacios en blanco, y que no exista ya en los diccionarios |
| título | No vacío ni solo espacios en blanco |
| género | No vacío ni solo espacios en blanco |
| estudio | No vacío ni solo espacios en blanco |
| clasificación | Debe ser exactamente `'G'`, `'PG'` o `'M'` |
| subtitulado | El usuario ingresa `'s'` o `'n'`. El sistema almacena `True` si es `'s'`, `False` si es `'n'` |
| país de origen | No vacío ni solo espacios en blanco |
| precio | Número entero mayor que cero |
| episodios | Número entero mayor o igual a cero |

**Para implementar esta opción:**
Define una función de validación independiente para cada campo de la tabla anterior. Cada función recibe únicamente el dato a validar, aplica su condición y retorna **`True`** si es válido o **`False`** si no lo es. Los mensajes de error **no** se muestran dentro de las funciones de validación.

En el **programa principal**, al elegir esta opción, se solicitan los datos al usuario y se llama a cada función de validación. Si alguna retorna **`False`**, el programa muestra el mensaje de error correspondiente y no registra la serie.

Solo si todas las validaciones retornan **`True`**, el programa llama a la función **`agregar_serie(codigo, titulo, genero, estudio, clasificacion, subtitulado, pais_origen, precio, episodios)`**, que agrega el registro en ambos diccionarios y retorna **`True`**. Si el código ya existía, retorna **`False`**. El programa principal muestra: *"Serie agregada"* o *"El código ya existe"* según corresponda.

---

**Opción 5 — Eliminar serie**

El sistema solicita el código de la serie que se desea eliminar. Si el código existe, elimina el registro en **ambos diccionarios** (`series` y `catalogo`) e informa que la operación fue exitosa. Si el código no existe, informa al usuario.

**Para implementar esta opción:**
Define una función llamada **`eliminar_serie(codigo)`**. Si el código **no existe**, retorna **`False`**. Si el código **existe**, elimina el registro de ambos diccionarios y retorna **`True`**. El **programa principal** recibe ese valor y muestra: *"Serie eliminada"* si fue exitoso, o *"El código no existe"* si no lo fue.

Recordar que la validación del código **no debe distinguir mayúsculas y minúsculas**.

---

**Opción 6 — Salir**

El sistema termina la ejecución de forma limpia. El ciclo del menú se detiene y el programa finaliza mostrando el mensaje: *"Programa finalizado."*

Esta opción no requiere función adicional. El programa principal es responsable de detener el ciclo y mostrar el mensaje de cierre.

---

### 3. Ejemplo de ejecución

Los datos en **negrita** son valores ingresados por el usuario:

```
========== MENÚ PRINCIPAL ==========
1. Episodios por género
2. Búsqueda de series por rango de precio
3. Actualizar precio de serie
4. Agregar serie
5. Eliminar serie
6. Salir
=====================================
Ingrese opción: 1
Ingrese género a consultar: ACCION
El total de episodios disponibles es: 101

Ingrese opción: 2
Ingrese precio mínimo: hola
Debe ingresar valores enteros
Ingrese precio mínimo: 5000
Ingrese precio máximo: 9000
Las series encontradas son: ['Kimetsu no Yaiba--AN004', 'No Game No Life--AN005', 'One Punch Man--AN003', 'Violet Evergarden--AN006']

Ingrese opción: 3
Ingrese código de la serie: S999
Ingrese nuevo precio: 8990
El código no existe
¿Desea actualizar otro precio (s/n)?: n

Ingrese opción: 4
Ingrese código de la serie: AN010
Ingrese título: Fullmetal Alchemist
Ingrese género: accion
Ingrese estudio: Bones
Ingrese clasificación (G/PG/M): PG
¿Está subtitulada al español? (s/n): s
Ingrese país de origen: Japon
Ingrese precio: 8490
Ingrese episodios disponibles: 64
Serie agregada

Ingrese opción: 6
Programa finalizado.
```

---

Algunas notas sobre el ejemplo para que puedas verificar tu solución:

- **Opción 1** con `"ACCION"`: Attack on Titan (75 ep) + Kimetsu no Yaiba (26 ep) = **101** ✓
- **Opción 2** con rango 5000–9000: quedan fuera AN001 (precio 9990) y AN002 (precio 4990 y además 0 episodios). Las 4 series restantes aparecen **ordenadas alfabéticamente** ✓
- **Opción 3** con código `S999`: no existe en el catálogo ✓

