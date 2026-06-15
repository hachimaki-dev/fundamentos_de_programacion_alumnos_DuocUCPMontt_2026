# Guía de Diseño – Pensando antes de Programar
## Acompaña a: FICHA 4 (Versión B) – Cazabichos

Este documento **no es el código de la solución**. Es la etapa anterior: el momento en que se piensa *qué piezas necesita el programa, qué hace cada pieza, qué recibe, qué entrega y cómo se conectan entre sí*, antes de escribir la primera línea de Python.

La idea es recorrer este documento en orden. Cada paso depende del anterior.

---

## Paso 1: ¿Dónde "vive" la información?

Antes de pensar en funciones, hay que identificar el **estado** del programa: los datos que deben mantenerse durante toda la ejecución.

- En este programa, el estado es **una sola cosa**: la lista de bichos.
- Esa lista se crea **una sola vez**, antes de entrar al ciclo del menú (`lista_bichos = []`).
- Como las listas en Python son **mutables**, si una función recibe la lista como parámetro y le hace `append()`, `pop()` o modifica un diccionario adentro, el cambio queda hecho "afuera" también. **No es necesario retornar la lista** para que los cambios se vean en el programa principal.

> Pregunta guía: cada vez que una función necesite leer o modificar la lista de bichos, ¿cómo se la voy a entregar? → Como **parámetro**.

---

## Paso 2: Diseñar la "ficha" de un bicho

Cada bicho es un diccionario con 4 llaves. Antes de programar, conviene tener esto clarísimo:

| Campo | Tipo de dato en Python | Ejemplo | Validación que necesita |
|---|---|---|---|
| `"especie"` | `str` | `"Escarabajo Rinoceronte"` | No vacío ni solo espacios |
| `"tamaño"` | `int` | `15` | Entero mayor que 0 |
| `"peligrosidad"` | `float` | `8.5` | Decimal entre 1.0 y 10.0 |
| `"peligroso"` | `bool` | `False` | No se pide al usuario, el sistema lo calcula |

Un bicho recién agregado siempre se ve así:

```python
{"especie": "Mariquita", "tamaño": 1, "peligrosidad": 2.0, "peligroso": False}
```

---

## Paso 3: Traducir cada opción del menú en "trabajo a hacer"

Antes de nombrar funciones, conviene preguntarse para cada opción del menú: **¿qué pasos hay que dar?** y **¿alguno de esos pasos se repite en otra opción?** (si se repite, es candidato a ser su propia función).

| Opción del menú | ¿Qué hay que hacer? | ¿Se reutiliza en otra opción? |
|---|---|---|
| 1. Agregar bicho | Pedir datos, validar cada uno, crear diccionario, agregarlo a la lista | No |
| 2. Buscar bicho | Pedir especie, recorrer la lista, devolver posición o -1 | **Sí** → la usa también la opción 3 |
| 3. Eliminar bicho | Pedir especie, **reutilizar la búsqueda**, eliminar si existe | Reutiliza la función de la opción 2 |
| 4. Actualizar estados | Recorrer toda la lista y fijar `"peligroso"` según `"peligrosidad"` | **Sí** → la usa también la opción 5 |
| 5. Mostrar bichos | Actualizar estados (reutiliza opción 4) y luego imprimir todo | Reutiliza la función de la opción 4 |
| 6. Salir | Mostrar mensaje y terminar el ciclo | No |

Esta tabla es la clave de todo el ejercicio: **dos funciones se construyen para ser reutilizadas por otras opciones del menú**. Si al programar te encuentras copiando y pegando el mismo bloque de código en dos opciones distintas, probablemente debería ser una función.

---

## Paso 4: Tipos de funciones que vas a necesitar

No todas las funciones "hacen lo mismo". Pensarlas por categoría ayuda a decidir si deben **retornar algo**, **modificar la lista**, o **solo mostrar texto**.

| Tipo de función | ¿Qué la caracteriza? | ¿Imprime mensajes de error? | ¿Retorna algo? | Ejemplos en este programa |
|---|---|---|---|---|
| **Validación** | Recibe un dato suelto, decide si es válido | **No** (eso lo hace quien la llama) | Sí, un `bool` | `validar_especie`, `validar_tamano`, `validar_peligrosidad` |
| **Consulta / búsqueda** | Recibe la lista y un criterio, no la modifica | No | Sí, una posición (`int`) | `buscar_bicho` |
| **Acción sobre la lista** | Recibe la lista y la modifica "por dentro" | Puede que sí (mensajes de éxito/error) | Generalmente **no** | `agregar_bicho`, `actualizar_estados` |
| **Interfaz / E-S** | Habla con el usuario (input/print) | — | Depende | `mostrar_menu`, `leer_opcion`, `mostrar_bichos` |

> Regla de oro: **separar "decidir" de "avisar"**. Una función de validación dice *True/False*; la función que la llama decide *qué mostrar en pantalla* si el resultado fue `False`.

---

## Paso 5: Tabla maestra de funciones

Esta es la "ficha técnica" de cada función que el programa necesita. Antes de programar, llena (o revisa) esta tabla: si puedes responder las 4 columnas para una función, ya sabes exactamente qué escribir.

| Función | Recibe (parámetros) | Retorna | Modifica la lista | Qué hace |
|---|---|---|---|---|
| `mostrar_menu()` | nada | nada | no | Imprime las 6 opciones del menú |
| `leer_opcion()` | nada | `int` (1–6, ya validado) | no | Pide un número al usuario y se asegura de que sea válido |
| `validar_especie(especie)` | un `str` | `bool` | no | Indica si la especie no está vacía ni es solo espacios |
| `validar_tamano(tamano)` | un valor numérico | `bool` | no | Indica si el tamaño es un entero mayor que 0 |
| `validar_peligrosidad(valor)` | un valor numérico | `bool` | no | Indica si el valor está entre 1.0 y 10.0 |
| `agregar_bicho(lista)` | la lista | nada | **sí** (`append`) | Pide datos, valida cada uno, y si todo es válido agrega el diccionario |
| `buscar_bicho(lista, especie)` | la lista y un `str` | `int` (posición o `-1`) | no | Recorre la lista buscando coincidencia exacta de especie |
| `actualizar_estados(lista)` | la lista | nada | **sí** (cambia `"peligroso"`) | Recorre la lista y fija `True`/`False` según la peligrosidad |
| `mostrar_bichos(lista)` | la lista | nada | indirectamente (llama a `actualizar_estados`) | Actualiza estados y luego imprime cada bicho con el formato pedido |

> Punto de decisión: la opción **3 (Eliminar)** no exige explícitamente una función propia — el enunciado dice que el *programa principal* llama a `buscar_bicho` y luego elimina. Puedes:
> - **(a)** hacerlo directo en el bloque de la opción 3 del menú, o
> - **(b)** crear `eliminar_bicho(lista)` que internamente llame a `buscar_bicho`.
>
> Ambas son válidas; (b) mantiene el bloque del menú más limpio.

---

## Paso 6: Mapa de funciones — ¿quién llama a quién?

```
main()  (el ciclo del menú)
 │
 ├─ mostrar_menu()                 → solo imprime
 ├─ leer_opcion()                  → retorna la opción elegida
 │
 ├─ [Opción 1] agregar_bicho(lista)
 │      ├─ validar_especie(especie)
 │      ├─ validar_tamano(tamaño)
 │      └─ validar_peligrosidad(peligrosidad)
 │
 ├─ [Opción 2] pos = buscar_bicho(lista, especie)
 │      └─ main decide: si pos == -1 → "no encontrado"
 │                       si pos >= 0 → mostrar ese bicho
 │
 ├─ [Opción 3] pos = buscar_bicho(lista, especie)   (¡la misma función de arriba!)
 │      └─ main decide: si pos == -1 → mensaje de error
 │                       si pos >= 0 → lista.pop(pos)
 │
 ├─ [Opción 4] actualizar_estados(lista)
 │
 ├─ [Opción 5] mostrar_bichos(lista)
 │      └─ actualizar_estados(lista)   (se llama desde adentro)
 │
 └─ [Opción 6] imprime despedida y corta el ciclo (break)
```

Fíjate que **`buscar_bicho` aparece dos veces** y **`actualizar_estados` aparece dos veces**: esa es la reutilización que se mencionó en el Paso 3.

---

## Paso 7: Pseudocódigo del ciclo principal

```
crear lista_bichos = []

mientras True:
    mostrar_menu()
    opcion = leer_opcion()

    si opcion == 1:
        agregar_bicho(lista_bichos)

    si no si opcion == 2:
        especie = pedir nombre de especie
        pos = buscar_bicho(lista_bichos, especie)
        si pos == -1:
            mostrar "no encontrado"
        si no:
            mostrar lista_bichos[pos]

    si no si opcion == 3:
        especie = pedir nombre de especie
        pos = buscar_bicho(lista_bichos, especie)
        si pos == -1:
            mostrar "El bicho 'especie' no se encuentra registrado."
        si no:
            lista_bichos.pop(pos)

    si no si opcion == 4:
        actualizar_estados(lista_bichos)

    si no si opcion == 5:
        mostrar_bichos(lista_bichos)

    si no si opcion == 6:
        mostrar "Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!"
        romper el ciclo
```

---

## Paso 8: Pseudocódigo guía, función por función

### `mostrar_menu()`
1. Imprimir el encabezado y las 6 líneas de opciones (formato literal del enunciado).
2. No recibe nada, no retorna nada.

### `leer_opcion()`
1. Pedir un número con `input()`.
2. Verificar que sea un número entero entre 1 y 6.
3. Si no es válido, avisar y volver a pedirlo (ciclo interno).
4. Retornar el número ya validado.

### `validar_especie(especie)`
1. Quitar espacios al inicio/fin (`.strip()`).
2. Si el resultado es una cadena vacía → retornar `False`.
3. En cualquier otro caso → retornar `True`.

### `validar_tamano(tamano)`
1. Verificar que el dato se pueda interpretar como entero.
2. Si es entero y es mayor que 0 → retornar `True`.
3. En cualquier otro caso → retornar `False`.

### `validar_peligrosidad(valor)`
1. Verificar que el dato se pueda interpretar como número decimal.
2. Si está entre 1.0 y 10.0 (ambos incluidos) → retornar `True`.
3. En cualquier otro caso → retornar `False`.

### `agregar_bicho(lista)`
1. Pedir la especie. Llamar a `validar_especie`. Si es `False`, mostrar mensaje de error y **terminar la función sin agregar nada**.
2. Pedir el tamaño. Llamar a `validar_tamano`. Si es `False`, mostrar mensaje de error y terminar.
3. Pedir la peligrosidad. Llamar a `validar_peligrosidad`. Si es `False`, mostrar mensaje de error y terminar.
4. Si los tres pasos anteriores fueron válidos, crear el diccionario con `"peligroso": False`.
5. Agregarlo a `lista` con `append()`.
6. Mostrar mensaje de confirmación.

> Nota: como cada validación corta la función con un `return` apenas falla un dato, **nunca se piden los tres datos si el primero ya falló** — conviene pensar el orden de los pasos así desde el principio.

### `buscar_bicho(lista, especie)`
1. Recorrer la lista con índice: `for i in range(len(lista))`.
2. Si `lista[i]["especie"] == especie` → retornar `i` inmediatamente.
3. Si el ciclo termina sin encontrar nada → retornar `-1`.

### `actualizar_estados(lista)`
1. Recorrer cada diccionario `bicho` de la lista.
2. Si `bicho["peligrosidad"] >= 7.0` → `bicho["peligroso"] = True`.
3. En caso contrario → `bicho["peligroso"] = False`.
4. No retorna nada: el cambio queda directamente en los diccionarios de la lista.

### `mostrar_bichos(lista)`
1. Llamar a `actualizar_estados(lista)` primero.
2. Imprimir el encabezado `=== LISTA DE BICHOS ===`.
3. Recorrer la lista y, para cada bicho, imprimir especie, tamaño, peligrosidad y el estado (`"PELIGROSO"` o `"NO PELIGROSO"` según `bicho["peligroso"]`).
4. Imprimir la línea de asteriscos después de cada bicho.

---

## Paso 9: Checklist antes de empezar a escribir código

Antes de programar cada función, responde estas preguntas:

- ¿Esta función necesita la lista de bichos? → entonces va como **parámetro**.
- ¿Esta función debe **decidir algo** (validar, buscar) o **hacer algo** (agregar, actualizar, mostrar)? → eso define si retorna un valor o no.
- Si es una validación: ¿estoy retornando `True`/`False` **sin imprimir nada adentro**?
- Si es una búsqueda: ¿retorno la **posición** (no el diccionario completo), tal como exige el enunciado?
- ¿Estoy reutilizando `buscar_bicho` en las opciones 2 y 3, en lugar de escribir el recorrido dos veces?
- ¿Estoy reutilizando `actualizar_estados` en las opciones 4 y 5?
- En la opción 1, ¿pido el siguiente dato solo si el anterior fue válido?

---

## Resumen visual rápido — "¿retorna o no retorna?"

| Función | ¿Retorna algo? |
|---|---|
| `mostrar_menu()` | No |
| `leer_opcion()` | **Sí** → `int` |
| `validar_especie()` | **Sí** → `bool` |
| `validar_tamano()` | **Sí** → `bool` |
| `validar_peligrosidad()` | **Sí** → `bool` |
| `agregar_bicho()` | No |
| `buscar_bicho()` | **Sí** → `int` (posición o `-1`) |
| `actualizar_estados()` | No |
| `mostrar_bichos()` | No |

Si una función de la lista de arriba **no retorna nada**, es porque su trabajo es "hacer algo" (modificar la lista o imprimir en pantalla), no "calcular y devolver un dato".