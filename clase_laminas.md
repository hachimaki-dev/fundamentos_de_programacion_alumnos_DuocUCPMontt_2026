# Material de práctica — Examen Final Transversal
## Sistema de Gestión de Colección de Láminas — Álbum del Mundial

*Listas, diccionarios anidados, funciones y manejo de errores*

| Sigla / Asignatura | Modalidad de trabajo | Duración sugerida |
|---|---|---|
| FPY1101 — Fundamentos de Programación | Individual | 200 a 220 minutos |

> **Cómo usar este material:** simula la dificultad y extensión esperada del examen final transversal. Incluye el enunciado, tabla de campos, reglas de negocio, tips de implementación, patrones de código parciales (no la solución armada) y una guía de autoevaluación. Inténtalo solo, sin mirar una solución completa.

---

## Enunciado

Desarrolla un programa en Python que implemente un sistema de gestión de colecciones de láminas del álbum del Mundial, donde todo el comportamiento se organice mediante funciones bien definidas. El programa debe incluir un menú interactivo, validaciones de entrada (incluyendo manejo de errores con try/except), operaciones lógicas (decisiones y comparaciones) y uso de funciones separadas.

### 1. Datos que debe manejar el sistema

El sistema trabaja con una colección de coleccionistas. Esta colección debe existir desde que el programa inicia y estar disponible durante toda la ejecución. Cada vez que se registra un coleccionista, se incorpora a esa colección como un nuevo elemento.

Cada coleccionista se representa como un diccionario con varios campos. Dos de esos campos —las láminas que pegó y las láminas repetidas que tiene para intercambiar— no son valores simples, sino listas. Esto agrega un nivel de profundidad respecto a lo trabajado anteriormente: una lista general (coleccionistas) que contiene diccionarios (cada coleccionista), donde cada uno de esos diccionarios contiene a su vez dos listas propias.

El álbum completo tiene un total fijo de **20 láminas por sección**, repartidas en **3 secciones**: `"Equipos"`, `"Estadios"` y `"Figuras"` (60 láminas en total). Cada lámina se identifica con un código único, por ejemplo `"EQ-01"`, `"ES-14"`, `"FI-07"`.

#### Estructura de un coleccionista

| Campo | Qué representa | Restricciones de validación |
|---|---|---|
| `"nombre"` | Nombre del coleccionista | No vacío ni solo espacios en blanco |
| `"laminas_pegadas"` | Lista de códigos de láminas que ya pegó en su álbum | Se crea como lista vacía al registrar. Cada código debe tener un formato válido (ver función de validación de código) y no puede repetirse dentro de la misma lista |
| `"laminas_repetidas"` | Lista de códigos de láminas que tiene de más, disponibles para intercambiar | Se crea como lista vacía al registrar. Un código no puede estar simultáneamente en pegadas y en repetidas para el mismo coleccionista |
| `"porcentaje_avance"` | Porcentaje del álbum completo que lleva pegado | **No se solicita al usuario.** El sistema lo calcula automáticamente cada vez que se actualiza el álbum, a partir de `laminas_pegadas` |

Cada diccionario de coleccionista se guarda dentro de una lista general llamada, por ejemplo, `coleccionistas`. El programa comienza con la lista vacía y la va llenando a medida que se registran coleccionistas.

### 2. Lo que debe hacer el sistema

El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú. Esto se repite hasta que el usuario elige salir.

El menú tiene siete opciones:

```
========== MENÚ ÁLBUM MUNDIAL ==========
1. Registrar coleccionista
2. Pegar lámina
3. Marcar lámina repetida
4. Buscar coleccionista
5. Ver láminas faltantes por sección
6. Buscar intercambio entre dos coleccionistas
7. Salir
==========================================
```

Debes definir dos funciones separadas para el menú: una que muestre las opciones en pantalla (sin recibir nada ni retornar nada) y otra que lea y retorne la opción elegida, validando con try/except que el usuario haya ingresado un número entero. Ambas funciones deben invocarse en cada vuelta del ciclo.

#### Opción 1 — Registrar coleccionista

El sistema solicita el nombre del coleccionista. Verifica que no esté vacío ni sea solo espacios en blanco. Si el dato no cumple la condición, informa al usuario y no registra. Solo cuando el dato es válido se crea el diccionario —con ambas listas de láminas vacías y porcentaje_avance en 0— y se agrega a la lista general.

Para implementar esta opción debes definir una función que reciba la lista de coleccionistas como parámetro y llame a una función de validación distinta para el nombre. Los mensajes de error se muestran en esta función, no dentro de la validación.

#### Opción 2 — Pegar lámina

El sistema solicita el nombre del coleccionista, lo busca, y si existe solicita el código de la lámina a pegar (por ejemplo `"EQ-05"`). Antes de agregarla verifica:

- El código tiene un formato válido: dos letras, un guion, dos números (`EQ-05`, `ES-14`, `FI-20`), y la sección (las dos letras) corresponde a una de las tres válidas (`EQ`, `ES`, `FI`).
- La lámina no está ya en `laminas_pegadas` de ese coleccionista (no se puede pegar dos veces la misma).

Si el código no es válido, o ya estaba pegado, el sistema informa al usuario y no realiza el cambio. Si todo es correcto, agrega el código a `laminas_pegadas` y **recalcula automáticamente** el `porcentaje_avance` del coleccionista.

Para implementar esta opción debes definir una función que reciba el diccionario del coleccionista y el código de la lámina, valide el formato con una función aparte, y —si corresponde— actualice la lista y vuelva a calcular el porcentaje llamando a la función de la opción 5 (o a una función de cálculo que ambas reutilicen).

#### Opción 3 — Marcar lámina repetida

El sistema solicita el nombre del coleccionista y el código de una lámina que tiene repetida (de más, no pegada en su álbum). Valida el mismo formato de código que en la opción anterior. Una regla de negocio nueva: **una lámina no puede estar simultáneamente en `laminas_pegadas` y en `laminas_repetidas`** del mismo coleccionista — si el código ya está pegado, el sistema rechaza la operación e informa al usuario, porque no tiene sentido tener de más algo que aún no completó.

#### Opción 4 — Buscar coleccionista

El sistema solicita un nombre y recorre la lista de coleccionistas buscando una coincidencia exacta. Para implementar esta opción debes definir una función que reciba la lista y el nombre como parámetros. La función recorre la lista y retorna la posición del registro encontrado, o -1 si no existe.

Es el programa principal quien recibe ese valor y decide qué hacer con él: si la posición es válida, muestra los datos completos del coleccionista (nombre, cantidad de láminas pegadas, cantidad de repetidas, porcentaje de avance); si es -1, muestra un mensaje de no encontrado.

#### Opción 5 — Ver láminas faltantes por sección

El sistema solicita el nombre de un coleccionista y, si existe, recorre **las 20 láminas posibles de cada una de las 3 secciones** comparando contra `laminas_pegadas`, para determinar cuáles le faltan. Muestra el resultado agrupado por sección, junto con el porcentaje de avance total. El formato de salida es el siguiente:

```
=== AVANCE DE Camila Rojas ===
Avance total: 35.0%

Sección Equipos — faltan 13 de 20:
  EQ-01, EQ-03, EQ-04, EQ-06, EQ-07, EQ-09, EQ-10, EQ-12, EQ-15, EQ-16, EQ-17, EQ-19, EQ-20

Sección Estadios — faltan 18 de 20:
  ES-01, ES-02, ES-03, ES-04, ES-05, ES-06, ES-07, ES-08, ES-09, ES-10, ES-11, ES-12, ES-13, ES-15, ES-16, ES-17, ES-18, ES-19

Sección Figuras — completa
*********************************************
```

Si una sección está completa (no falta ninguna), se muestra el texto `Sección Figuras — completa` en vez de intentar imprimir una lista vacía como si tuviera elementos.

Para implementar esta opción debes definir una función que reciba el diccionario del coleccionista y retorne, por ejemplo, un diccionario con las láminas faltantes agrupadas por sección, además de actualizar el porcentaje de avance. El programa principal se encarga de mostrar el resultado con el formato pedido.

#### Opción 6 — Buscar intercambio entre dos coleccionistas

El sistema solicita los nombres de dos coleccionistas distintos, los busca (reutilizando la función de búsqueda de la opción 4), y si ambos existen, determina si pueden intercambiar láminas entre sí. Dos coleccionistas pueden intercambiar si existe al menos una lámina que el primero tiene repetida y al segundo le falta (no está en su `laminas_pegadas`), **o viceversa**.

El sistema muestra qué láminas podría darle cada uno al otro. Si no existe ningún intercambio posible en ningún sentido, informa al usuario con el siguiente mensaje:

```
No hay intercambios posibles entre 'nombre1' y 'nombre2'.
```

Esta es la regla de negocio más exigente del ejercicio: requiere comparar la lista de repetidas de uno contra la lista de pegadas del otro, en ambos sentidos, sin asumir que el intercambio es simétrico.

#### Opción 7 — Salir

El sistema termina la ejecución de forma limpia, sin errores. El ciclo del menú se detiene y el programa finaliza con un mensaje de despedida:

```
"¡Gracias por coleccionar con nosotros! Hasta la próxima."
```

---

## Tips de implementación

### Sobre la estructura de datos anidada

- Esta vez el anidamiento no es "lista dentro de diccionario dentro de lista" como en el ejemplo del restaurante, sino **dos listas independientes dentro de un mismo diccionario**: `laminas_pegadas` y `laminas_repetidas`. Acostúmbrate a leer cuál de las dos corresponde según el contexto antes de operar sobre ella.
- El "álbum completo" (las 60 láminas posibles) no necesita guardarse como una lista gigante escrita a mano. Puedes generarlo con código, por ejemplo recorriendo las secciones y números del 1 al 20, y construyendo el código con f-strings (`f"{seccion}-{numero:02d}"`).
- Para calcular qué falta, no recorras buscando con `for` anidados si no es necesario: la comparación entre dos listas se puede hacer con operadores de pertenencia (`in`) o con conjuntos (`set`), que en este nivel también es válido si ya los conoces.

### Sobre el manejo de errores con try/except

Aquí el error de conversión más típico no es numérico sino de **formato de texto**: el código de lámina puede venir mal escrito (`"eq5"`, `"EQ_05"`, `"XX-05"`). Para esto no necesitas try/except —no hay conversión de tipo que falle—, necesitas validación con condicionales y manipulación de strings. Reserva el try/except para los lugares donde sí se convierte texto a número, como la lectura de la opción del menú.

> **Diferencia clave:** try/except protege contra errores de *conversión* (cuando el dato ni siquiera se puede transformar al tipo esperado). La validación con `if` protege contra datos que sí tienen el tipo correcto pero no cumplen el formato o la regla de negocio (un código con la sección equivocada, una lámina duplicada, etc.). Para el código de lámina vas a necesitar sobre todo la segunda.

### Sobre la reutilización de funciones

- La función de búsqueda por nombre (opción 4) se reutiliza en las opciones 2, 3, 5 y 6. Escribe una sola función `buscar_coleccionista(lista, nombre)` y llámala desde todas partes.
- La función que calcula el porcentaje de avance debería ser la misma que usa la opción 2 (después de pegar una lámina) y la opción 5 (al mostrar el detalle). No dupliques la fórmula en dos lugares distintos del código.
- La validación de formato de código de lámina (sección + número) se usa igual en la opción 2 y en la opción 3. Es una sola función de validación, llamada desde ambas.

### Sobre el cálculo del porcentaje de avance

```
porcentaje = (cantidad de láminas pegadas / 60) * 100
```

- El total de láminas del álbum (60) es un valor fijo que no depende de ningún coleccionista en particular: considera definirlo como una constante al principio del programa, no repetir el número `60` escrito a mano en varias funciones.
- Recuerda redondear o formatear el porcentaje para que se vea razonable al imprimirlo (por ejemplo, con `round(valor, 1)`).

### Sobre la comparación para intercambios

Piensa la opción 6 en dos pasos separados, no en uno solo:

1. ¿Qué de las repetidas del coleccionista A le falta al coleccionista B? (recorrer `repetidas_A` y comprobar cuáles **no** están en `pegadas_B`)
2. ¿Qué de las repetidas del coleccionista B le falta al coleccionista A? (lo mismo, al revés)

Un error común es calcular solo un sentido y asumir que el otro es igual — no lo es, salvo coincidencia.

### Errores frecuentes a evitar

- **No generar el álbum completo de forma dinámica**, y en su lugar escribir 60 códigos a mano, lo que vuelve el código rígido y propenso a errores de tipeo.
- **Permitir códigos con sección inventada** (por ejemplo `"XX-05"`) porque solo se validó el formato (letras-guion-números) y no que la sección sea una de las tres válidas.
- **Olvidar la regla de exclusión mutua** entre pegadas y repetidas, dejando que una misma lámina aparezca en ambas listas del mismo coleccionista.
- **Calcular el intercambio en un solo sentido**, mostrando solo lo que A le puede dar a B y omitiendo lo que B le puede dar a A.
- **No actualizar el porcentaje de avance** justo después de pegar una lámina, dejándolo desincronizado hasta la próxima vez que se ejecute la opción 5.

---

## Patrones de código de referencia

*Estos fragmentos muestran el patrón general, pero están incompletos a propósito (marcados con `# COMPLETAR`). El objetivo es que practiques resolviendo la lógica faltante.*

### Constantes y generación del álbum completo

```python
SECCIONES = ["EQ", "ES", "FI"]
LAMINAS_POR_SECCION = 20
TOTAL_LAMINAS = len(SECCIONES) * LAMINAS_POR_SECCION  # 60

def generar_album_completo():
    album = {}
    for seccion in SECCIONES:
        codigos = []
        for numero in range(1, LAMINAS_POR_SECCION + 1):
            codigo = f"{seccion}-{numero:02d}"
            codigos.append(codigo)
        album[seccion] = codigos
    return album
    # album queda algo así:
    # {"EQ": ["EQ-01", "EQ-02", ..., "EQ-20"], "ES": [...], "FI": [...]}
```

### Validación de formato de código de lámina

```python
def es_codigo_valido(codigo):
    if len(codigo) != 5:
        return False
    seccion = codigo[0:2]
    guion = codigo[2]
    numero = codigo[3:5]
    if seccion not in SECCIONES:
        return False
    if guion != "-":
        return False
    # COMPLETAR: validar que 'numero' sean dos dígitos numéricos
    #            entre "01" y "20" (pista: numero.isdigit() y luego
    #            convertir a entero y comprobar el rango)
    return True
```

### Función de búsqueda reutilizable

```python
def buscar_coleccionista(coleccionistas, nombre):
    for i in range(len(coleccionistas)):
        if coleccionistas[i]["nombre"] == nombre:
            return i
    return -1
```

### Pegar lámina (con recálculo automático)

```python
def calcular_porcentaje(coleccionista):
    cantidad = len(coleccionista["laminas_pegadas"])
    return round((cantidad / TOTAL_LAMINAS) * 100, 1)

def pegar_lamina(coleccionista, codigo):
    if not es_codigo_valido(codigo):
        print("Código de lámina inválido.")
        return

    if codigo in coleccionista["laminas_pegadas"]:
        print("Esta lámina ya estaba pegada.")
        return

    # COMPLETAR: si el código está en laminas_repetidas, ¿qué debería
    #            pasar? (pista: pensar si tiene sentido pegar algo
    #            que también está marcado como repetido)

    coleccionista["laminas_pegadas"].append(codigo)
    coleccionista["porcentaje_avance"] = calcular_porcentaje(coleccionista)
    print(f"Lámina {codigo} pegada. Avance: {coleccionista['porcentaje_avance']}%")
```

### Láminas faltantes por sección

```python
def laminas_faltantes(coleccionista):
    album = generar_album_completo()
    faltantes = {}
    for seccion in SECCIONES:
        faltantes_seccion = []
        for codigo in album[seccion]:
            # COMPLETAR: si 'codigo' no está en
            #            coleccionista["laminas_pegadas"], agregarlo
            #            a faltantes_seccion
            pass
        faltantes[seccion] = faltantes_seccion
    return faltantes

# Desde el programa principal:
# faltantes = laminas_faltantes(coleccionistas[posicion])
# for seccion in SECCIONES:
#     cantidad_faltante = len(faltantes[seccion])
#     if cantidad_faltante == 0:
#         print(f"Sección {seccion} — completa")
#     else:
#         print(f"Sección {seccion} — faltan {cantidad_faltante} de {LAMINAS_POR_SECCION}:")
#         print(", ".join(faltantes[seccion]))
```

### Buscar intercambio entre dos coleccionistas

```python
def que_le_falta_a(receptor, ofertante):
    """Retorna qué láminas repetidas de 'ofertante' le sirven a 'receptor'."""
    posibles = []
    for codigo in ofertante["laminas_repetidas"]:
        if codigo not in receptor["laminas_pegadas"]:
            posibles.append(codigo)
    return posibles

# Desde el programa principal, dentro de la opción 6:
# de_a_a_b = que_le_falta_a(coleccionista_b, coleccionista_a)
# de_b_a_a = que_le_falta_a(coleccionista_a, coleccionista_b)
#
# COMPLETAR: si de_a_a_b y de_b_a_a están ambas vacías, mostrar el
#            mensaje de "no hay intercambios posibles"; si no,
#            mostrar lo que cada uno le puede ofrecer al otro
```

---

## Guía de autoevaluación

Antes de considerar tu ejercicio terminado, revisa cada punto. Si respondes "no" a alguno, vuelve atrás y corrígelo.

**Estructura de datos**
- [ ] ¿La lista de coleccionistas existe antes del ciclo del menú y no se reinicia en cada vuelta?
- [ ] ¿Cada coleccionista nuevo se crea con ambas listas vacías y porcentaje_avance en 0, sin pedirle ese último dato al usuario?
- [ ] ¿Generas el álbum completo (60 códigos) de forma dinámica, sin escribirlo a mano?

**Funciones**
- [ ] ¿Tienes una función separada para mostrar el menú y otra para leer la opción?
- [ ] ¿Tu función de búsqueda por nombre es una sola, y la reutilizas en al menos tres opciones distintas?
- [ ] ¿La función que calcula el porcentaje de avance es una sola, reutilizada donde corresponde?
- [ ] ¿Los mensajes de error se muestran en la función que pide el dato, no dentro de las validaciones?

**Manejo de errores**
- [ ] ¿Usas try/except en la lectura de la opción del menú?
- [ ] ¿Tu programa no se cae si el usuario escribe letras donde se esperaba un número?
- [ ] ¿Distingues entre validar formato de código (con `if`) y convertir tipos (con `try/except`)?

**Reglas de negocio**
- [ ] ¿Tu sistema rechaza un código de lámina con sección inválida (por ejemplo `"XX-05"`)?
- [ ] ¿Tu sistema impide que una misma lámina esté pegada y repetida a la vez para el mismo coleccionista?
- [ ] ¿La búsqueda de intercambio revisa ambos sentidos (A hacia B y B hacia A), no solo uno?
- [ ] ¿El porcentaje de avance se recalcula automáticamente después de pegar una lámina?

**Formato de salida**
- [ ] ¿La opción 5 muestra correctamente una sección completa, sin imprimir una lista vacía como si tuviera elementos?
- [ ] ¿El mensaje de despedida aparece exactamente al elegir la opción 7, y el ciclo termina ahí?

> **Antes de entregar:** prueba al menos estos tres casos: (1) un coleccionista que completa una sección entera, (2) un intento de pegar un código con sección inválida o ya pegado, y (3) dos coleccionistas donde el intercambio solo funciona en un sentido (uno puede ayudar al otro, pero no al revés). Si los tres se comportan como esperas, vas bien encaminado.