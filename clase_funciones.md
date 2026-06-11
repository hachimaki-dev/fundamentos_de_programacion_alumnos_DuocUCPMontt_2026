# Mini-taller: Funciones en Python — De cero a sistema completo

## Introducción: ¿qué es una función y por qué existe?

Imagina que cada vez que quieres lavarte los dientes tuvieras que explicarle a alguien, paso por paso, "agarra el cepillo, pon pasta, mueve la mano arriba y abajo durante 2 minutos, enjuaga". Sería agotador repetir esa explicación cada vez. En cambio, simplemente dices "lávate los dientes" y todos entienden el procedimiento completo.

Una **función** es exactamente eso: un bloque de código con un nombre, que encapsula un procedimiento. Una vez que lo defines, puedes "invocarlo" (llamarlo) las veces que quieras sin reescribir la lógica.

```python
def lavarse_dientes():
    print("Agarrar cepillo")
    print("Poner pasta")
    print("Cepillar 2 minutos")
    print("Enjuagar")

lavarse_dientes()  # "invocación" o "llamado" de la función
lavarse_dientes()  # se puede usar cuantas veces se quiera
```

**Vocabulario clave:**
- **Definir** una función = escribir su código con `def`.
- **Invocar/llamar** una función = ejecutarla escribiendo su nombre seguido de `()`.
- **Parámetro** = una variable que la función espera recibir (se define entre los paréntesis al crear la función).
- **Argumento** = el valor real que le pasas cuando la invocas.

```python
def lavarse_dientes(minutos):  # "minutos" es un PARÁMETRO
    print(f"Cepillando por {minutos} minutos")

lavarse_dientes(2)  # "2" es el ARGUMENTO
```

Por qué importa esto en tu examen: vas a tener que crear *muchas* funciones pequeñas, cada una con un trabajo específico. Entender bien esta diferencia entre parámetro/argumento te evitará el 50% de los errores típicos.

---

## Concepto 1: `return` vs `print` — la confusión más común

Esta es, sin exagerar, la fuente del 80% de los errores de quienes recién aprenden funciones.

`print()` **muestra algo en pantalla**. Es comunicación con el usuario humano. No le sirve de nada al programa.

`return` **entrega un valor de vuelta** a quien llamó la función. Es comunicación entre partes del programa. El programa SÍ puede usar ese valor después.

```python
def sumar_print(a, b):
    print(a + b)  # solo IMPRIME, no entrega nada

def sumar_return(a, b):
    return a + b  # ENTREGA el resultado

resultado1 = sumar_print(3, 4)   # en pantalla aparece "7"
print(resultado1)                # pero esto imprime "None" !!

resultado2 = sumar_return(3, 4)  # no aparece nada en pantalla
print(resultado2)                # esto imprime "7"
```

**¿Por qué pasa esto?** Cuando una función no tiene `return`, Python automáticamente le asigna el valor especial `None` (que significa "nada"/"vacío"). Por eso `resultado1` termina siendo `None`: la función `sumar_print` nunca dijo "devuelve esto", solo imprimió y terminó.

**Regla práctica para tu examen:** si una función necesita que el programa principal *use* el resultado después (para guardarlo, compararlo, decidir algo), necesita `return`. Si la función solo necesita *mostrar algo al usuario y listo*, usa `print`.

---

## Concepto 2: Parámetros con valores por defecto

A veces queremos que un parámetro tenga un valor "de respaldo" si no se especifica.

```python
def saludar(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")

saludar("Juan")              # usa "español" por defecto
saludar("John", "inglés")    # sobreescribe el valor por defecto
```

**Detalle importante:** los parámetros con valor por defecto deben ir *después* de los que no lo tienen. Esto daría error:

```python
def mal(a="x", b):  # ERROR: parámetro sin default después de uno con default
    pass
```

---

## Concepto 3: Funciones que reciben listas y diccionarios — mutabilidad

Este concepto es **crítico** para tu examen, porque vas a tener UNA lista que vive durante toda la ejecución y muchas funciones que la modifican.

En Python, las listas y diccionarios son **mutables**: cuando le pasas una lista a una función y la función la modifica (con `.append()`, `.pop()`, cambiando un valor, etc.), el cambio se mantiene afuera de la función, **aunque la función no haga `return`**.

```python
def agregar_fruta(lista_frutas):
    lista_frutas.append("manzana")
    # no hay return, y no hace falta

mis_frutas = ["pera", "uva"]
agregar_fruta(mis_frutas)
print(mis_frutas)  # ['pera', 'uva', 'manzana']  -> ¡se modificó!
```

Compara esto con un número (los números NO son mutables):

```python
def intentar_cambiar(numero):
    numero = numero + 100
    # esto NO afecta la variable original

x = 5
intentar_cambiar(x)
print(x)  # sigue siendo 5
```

**¿Por qué pasa esto?** Las listas y diccionarios se pasan "por referencia": la función recibe un "mapa" hacia el mismo objeto en memoria, no una copia. Los números, strings y booleanos se pasan "por valor": la función recibe una copia independiente.

**Para tu examen:** cuando definas la función que agrega un estudiante, recibirás la lista como parámetro, le harás `.append()` al diccionario nuevo, y **no necesitas retornar la lista** — el cambio ya quedó hecho.

---

## Concepto 4: Funciones de validación — el patrón "pregunta de sí o no"

Una función de validación responde una pregunta booleana: ¿esto cumple la condición o no? Por convención, su nombre suele empezar con `es_`, `tiene_`, `valida_`, etc., y siempre retorna `True` o `False`.

```python
def es_mayor_de_edad(edad):
    return edad >= 18
```

**¿Por qué retornar la comparación directamente y no escribir un if/else?** Porque `edad >= 18` *ya es* un valor booleano (`True` o `False`). Escribir:

```python
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
```

hace exactamente lo mismo, pero con más líneas. Ambas formas son válidas — la primera es más "pythonica" (idiomática de Python), pero si recién estás aprendiendo y el `if/else` te ayuda a pensar, úsalo. **Lo importante es que entiendas que ambas producen lo mismo**, y puedas reconocer las dos formas cuando las veas en código de otra persona.

---

## Concepto 5: Funciones de búsqueda — el patrón "posición o -1"

Este es uno de los patrones más importantes del examen. La idea: recorres una lista buscando algo, y si lo encuentras retornas **en qué posición está** (un número, el índice). Si no lo encuentras, retornas `-1` (porque `-1` nunca es una posición válida en una lista, así que sirve como "señal" de "no encontrado").

```python
def buscar_posicion(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i  # encontramos! salimos inmediatamente con return
    return -1  # si el for terminó sin encontrar nada, llegamos aquí
```

**¿Por qué `return` corta el ciclo?** Porque `return` no solo entrega un valor, sino que **termina la ejecución de la función inmediatamente**, sin importar en qué parte del código esté. Por eso, si encontramos el valor en la posición 2, el `for` ni siquiera sigue revisando las posiciones 3, 4, 5...

**Forma alternativa con `enumerate()`:** `enumerate()` es una función de Python que, al recorrer una lista, te entrega *automáticamente* tanto el índice como el valor, en cada vuelta del ciclo:

```python
def buscar_posicion_v2(lista, valor_buscado):
    for indice, valor in enumerate(lista):
        if valor == valor_buscado:
            return indice
    return -1
```

Ambas versiones hacen lo mismo. `enumerate()` es más limpio cuando necesitas tanto el índice como el valor; `range(len(lista))` es más explícito y a veces más fácil de entender al principio. **Conocer ambas te prepara para leer código de otros y para examen, donde podrías necesitar cualquiera de las dos.**

---

## Concepto 6: ¿Por qué la búsqueda retorna la posición y no decide qué hacer?

Esto conecta con un principio de diseño llamado **separación de responsabilidades**: cada función debería hacer **una sola cosa** y hacerla bien.

La función de búsqueda tiene UNA responsabilidad: encontrar y reportar dónde está algo (o avisar que no está). NO es su responsabilidad decidir qué mensaje mostrar, ni qué hacer con esa información — eso depende de **quién la llama** y **para qué** la está usando.

¿Por qué importa esto? Porque la misma función de búsqueda la vas a **reutilizar** para cosas distintas:
- Para "Buscar estudiante" → si encuentra, muestra los datos.
- Para "Eliminar estudiante" → si encuentra, lo elimina.

Si la función de búsqueda ya tuviera "incrustada" la lógica de "mostrar datos", no podrías reutilizarla para eliminar. Al hacer que solo retorne la posición (o -1), el programa principal decide qué hacer con esa información según el contexto. Esto es lo que se llama una función **reutilizable**.

---

## Concepto 7: Reutilizar una función dentro de otra

Una función puede llamar a otra función. Esto es completamente normal y deseable — es la base de la organización modular.

```python
def buscar_posicion(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def eliminar(lista, valor):
    posicion = buscar_posicion(lista, valor)  # reutilizamos la función anterior
    if posicion != -1:
        lista.pop(posicion)
        print("Eliminado correctamente")
    else:
        print("No se encontró el elemento")
```

Esto evita escribir dos veces la misma lógica de búsqueda, y si en el futuro mejoras `buscar_posicion`, automáticamente `eliminar` también mejora.

---

## Concepto 8: Recorrer y modificar TODOS los elementos de una lista

A veces no buscas un elemento específico, sino que necesitas aplicar una regla a **cada** elemento de la lista, sin excepción.

```python
def aplicar_descuento(lista_precios):
    for i in range(len(lista_precios)):
        lista_precios[i] = lista_precios[i] * 0.9  # 10% de descuento a todos
```

Cuando la lista contiene diccionarios (como en tu examen), accedes y modificas un campo específico de cada uno:

```python
def marcar_todos_revisados(lista_productos):
    for producto in lista_productos:
        producto["revisado"] = True
```

**Nota sutil:** aquí `for producto in lista_productos` funciona para *modificar* porque `producto` es una referencia al diccionario real dentro de la lista (los diccionarios son mutables, como vimos en el Concepto 3). Si la lista contuviera números y quisieras modificarlos, necesitarías usar índices (`lista[i] = ...`), porque los números no son mutables y `for numero in lista` te daría solo una copia del valor.

---

## Concepto 9: ¿Qué es un "dispatcher" y por qué se llama así?

La palabra **dispatcher** viene del inglés *to dispatch*, que significa "despachar" o "enviar algo a su destino" — como un operador de central telefónica que recibe una llamada y la "despacha" (la dirige) hacia la persona correcta según lo que el usuario pida.

En programación, un **patrón dispatcher** es una estructura que:
1. Recibe una "señal" o "instrucción" (en tu caso, el número que el usuario elige en el menú).
2. Según esa señal, "despacha" la ejecución hacia la función o bloque de código correspondiente.

El ejemplo más común y simple de dispatcher es un `if/elif/else` que redirige según una opción:

```python
opcion = leer_opcion()

if opcion == 1:
    agregar_estudiante(lista)
elif opcion == 2:
    buscar_estudiante(lista)
elif opcion == 3:
    eliminar_estudiante(lista)
elif opcion == 6:
    print("Adiós")
    break
```

Aquí, `leer_opcion()` obtiene la "señal", y el bloque `if/elif` actúa como el dispatcher: dirige el flujo del programa hacia la función correcta.

**¿Existen otras formas de hacer un dispatcher?** Sí. Una alternativa más avanzada (no obligatoria para tu examen, pero bueno conocerla) es usar un **diccionario de funciones**, donde las claves son las opciones y los valores son las funciones mismas:

```python
def opcion_agregar():
    print("Agregando...")

def opcion_buscar():
    print("Buscando...")

# diccionario donde los VALORES son funciones (sin paréntesis, sin ejecutarlas)
acciones = {
    1: opcion_agregar,
    2: opcion_buscar,
}

opcion = 1
if opcion in acciones:
    acciones[opcion]()  # aquí SÍ se ejecuta, por eso los paréntesis
else:
    print("Opción inválida")
```

Esto se usa en sistemas más grandes (por ejemplo, frameworks web que "despachan" una URL hacia la función que debe responderla). **Para tu examen, el `if/elif/else` es perfectamente válido y suficiente** — pero ahora sabes de dónde viene el término y que existe una versión más "elegante" si quieres explorar.

---

## Concepto 10: El ciclo `while True` con `break` — la estructura de un menú

Un menú necesita repetirse indefinidamente *hasta que el usuario decide salir*. Como no sabemos de antemano cuántas veces se repetirá, usamos `while True` (un ciclo "infinito" a propósito) combinado con `break` (que rompe/termina el ciclo cuando se cumple cierta condición).

```python
while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 6:
        print("Adiós")
        break  # rompe el ciclo, el programa continúa después del while

    # ... resto de las opciones
```

**¿Por qué no usar un `while` con una condición normal, como `while opcion != 6`?** Técnicamente se puede, pero tendrías que inicializar `opcion` con algún valor *antes* del ciclo (para que la condición pueda evaluarse la primera vez), lo cual es un poco artificial. `while True` + `break` es el patrón estándar para "repetir hasta que pase algo que decido durante el ciclo", y es el que vas a usar en tu examen.

---

## Concepto 11: Validar entradas con bucles — "pedir hasta que sea válido"

Cuando pides un dato al usuario y necesitas que cumpla una condición, el patrón es: pedir, validar, y si no es válido, **volver a pedir**, repitiendo hasta obtener algo correcto.

```python
def pedir_edad_valida():
    while True:
        entrada = input("Ingrese edad: ")
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("Edad inválida, intente nuevamente")
```

`.isdigit()` es un método de los strings que retorna `True` si el texto está compuesto **solo** por dígitos (0-9), y `False` si contiene letras, espacios, puntos, signos negativos, etc. Es útil para verificar que algo "parece un número entero" *antes* de convertirlo con `int()`, evitando que el programa se caiga con un error si el usuario escribe "abc".

**Alternativa con `try/except`:** otra forma de manejar esto es "intentar" la conversión y "atrapar" el error si falla:

```python
def pedir_edad_valida_v2():
    while True:
        entrada = input("Ingrese edad: ")
        try:
            edad = int(entrada)
            if edad > 0:
                return edad
            else:
                print("La edad debe ser mayor que 0")
        except ValueError:
            print("Eso no es un número válido")
```

`try` significa "intenta ejecutar este código"; `except ValueError` significa "si ocurre un error de tipo ValueError (por ejemplo, al intentar convertir 'abc' a entero), no dejes que el programa se caiga, en su lugar haz esto otro". Esta forma es más robusta porque maneja casos como números negativos escritos con signo (`"-5"`, que `.isdigit()` consideraría inválido aunque sí se puede convertir a entero).

**Para tu examen:** cualquiera de las dos formas es válida. Te recomendamos elegir UNA estrategia y ser consistente con ella en todas tus validaciones.

---

## Concepto 12: Validar contra texto vacío o solo espacios

```python
# Versión manual: recorrer carácter por carácter
def tiene_contenido_v1(texto):
    for caracter in texto:
        if caracter != " ":
            return True  # encontramos un carácter que NO es espacio
    return False  # recorrimos todo y todos eran espacios (o estaba vacío)

# Versión con método de strings
def tiene_contenido_v2(texto):
    return texto.strip() != ""
```

`.strip()` es un método de los strings que retorna una copia del string **sin espacios en blanco al principio ni al final**. Por ejemplo, `"   hola  ".strip()` retorna `"hola"`. Si el string original era solo espacios (`"   "`), `.strip()` lo deja como `""` (string vacío), y comparar `"" != ""` da `False` — correctamente detectando que no había contenido real.

**¿Por qué existen ambas formas?** La versión manual (v1) te obliga a pensar en la lógica carácter por carácter — esto desarrolla tu capacidad de "pensar como el computador" y es útil cuando *no existe* una función built-in para lo que necesitas. La versión con `.strip()` (v2) es más corta y es lo que usarías en código real, porque Python ya resolvió ese problema por ti. **Saber ambas te permite reconocer cuándo "reinventar la rueda" y cuándo usar lo que el lenguaje ya ofrece.**

---

## Concepto 13: Validar números decimales en un rango

```python
def es_nota_valida(nota):
    return isinstance(nota, (int, float)) and 1.0 <= nota <= 7.0
```

`isinstance(valor, tipo)` retorna `True` si `valor` es del `tipo` indicado. `isinstance(nota, (int, float))` verifica si `nota` es un entero **o** un decimal (le pasamos una tupla de tipos posibles). Esto importa porque si pides la nota con `input()`, recibes un string, y necesitas convertirlo con `float()` antes de poder compararlo numéricamente — y esa conversión puede fallar si el usuario escribe texto.

`1.0 <= nota <= 7.0` es una "comparación encadenada" propia de Python: equivale a escribir `nota >= 1.0 and nota <= 7.0`, pero más legible.

---

## Concepto 14: Contar elementos que cumplen una condición

```python
# Versión con contador y for
def contar_aprobados_v1(lista_estudiantes):
    contador = 0
    for estudiante in lista_estudiantes:
        if estudiante["aprobado"] == True:
            contador = contador + 1
    return contador

# Versión con sum() y expresión generadora
def contar_aprobados_v2(lista_estudiantes):
    return sum(1 for estudiante in lista_estudiantes if estudiante["aprobado"])
```

La versión 2 usa una **expresión generadora**: `(1 for estudiante in lista_estudiantes if estudiante["aprobado"])` produce un "1" por cada estudiante aprobado (y nada por los que no lo están), y `sum()` suma todos esos 1, dando el total de aprobados. Es una forma compacta de "contar con condición" muy común en Python, pero si te resulta confusa, la versión con contador (v1) es perfectamente válida y quizás más fácil de explicar si te preguntan en el examen "¿qué hace esta línea?".

---

## Concepto 15: Crear un diccionario "registro" con valores iniciales fijos

```python
def crear_estudiante(nombre, edad, nota):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False  # siempre inicia en False, no se pide al usuario
    }
    return estudiante
```

Este patrón aparece cuando un campo del registro **no depende de lo que el usuario ingresa**, sino que el sistema lo asigna por defecto, para actualizarlo después con otra función (Concepto 8).

---

# Serie de ejercicios progresivos

**Contexto:** sistema de gestión de una **biblioteca**, distinto al de tu examen (estudiantes), para que practiques los mismos *patrones* sin resolver directamente el examen.

Cada ejercicio indica qué concepto(s) del taller pone en práctica, para que puedas volver atrás si te trabas.

---

## Bloque A: Fundamentos de funciones (Ejercicios 1-6)

**Ejercicio 1** — *Concepto: definir/invocar, sin parámetros, sin return*
Crea una función `mostrar_bienvenida()` que no reciba nada y no retorne nada, solo imprima un mensaje de bienvenida a la biblioteca. Llámala 3 veces seguidas.
*Pregúntate:* ¿qué pasaría si guardas `x = mostrar_bienvenida()` y luego imprimes `x`? Pruébalo y reflexiona por qué da ese resultado.

**Ejercicio 2** — *Concepto: return vs print*
Crea dos funciones: `duplicar_print(numero)` que imprima el doble del número, y `duplicar_return(numero)` que lo retorne. Luego:
```python
a = duplicar_print(5)
b = duplicar_return(5)
print(a)
print(b)
```
*Pregúntate:* ¿por qué `a` y `b` son distintos aunque ambas funciones "hacen lo mismo" a primera vista?

**Ejercicio 3** — *Concepto: parámetros con valor por defecto*
Crea una función `calcular_multa(dias_atraso, valor_por_dia=100)` que retorne el total de la multa (`dias_atraso * valor_por_dia`). Pruébala llamándola con un solo argumento y luego con dos.
*Pregúntate:* ¿qué pasa si intentas escribir `def calcular_multa(valor_por_dia=100, dias_atraso)`? ¿Por qué da error?

**Ejercicio 4** — *Concepto: funciones de validación, dos caminos*
Crea una función `es_libro_antiguo(anio)` que retorne `True` si el año es menor a 1990.
- Escríbela primero con `if/else` explícito.
- Luego reescríbela en una sola línea con `return`.
*Pregúntate:* ¿en qué casos preferirías la versión larga aunque sea más código?

**Ejercicio 5** — *Concepto: mutabilidad de listas*
Crea una función `agregar_a_lista(lista, elemento)` que use `.append()` para agregar `elemento` a `lista`, sin retornar nada. Luego:
```python
mi_lista = ["a", "b"]
agregar_a_lista(mi_lista, "c")
print(mi_lista)
```
*Pregúntate:* la función no tiene `return`, pero `mi_lista` cambió. Investiga: ¿qué pasaría si en lugar de `.append()` la función hiciera `lista = lista + [elemento]`? (Pista: esto crea una lista *nueva*, no modifica la original — investiga la diferencia entre "modificar en el lugar" y "reasignar").

**Ejercicio 6** — *Concepto: mutabilidad de números (contraste)*
Crea una función `intentar_aumentar(numero)` que haga `numero = numero + 10` (sin retornar). Luego:
```python
x = 5
intentar_aumentar(x)
print(x)
```
*Pregúntate:* ¿por qué el resultado es distinto al ejercicio 5? Escribe con tus propias palabras la diferencia entre tipos mutables (listas, diccionarios) e inmutables (números, strings, booleanos).

---

## Bloque B: Validaciones (Ejercicios 7-13)

**Ejercicio 7** — *Concepto 12: texto vacío/espacios, dos caminos*
Crea `tiene_contenido_v1(texto)` (recorriendo carácter por carácter con `for`) y `tiene_contenido_v2(texto)` (usando `.strip()`). Pruébalas con `"   "`, `""`, `"  Don Quijote  "`.
*Investiga:* busca en la documentación de Python qué otros métodos de strings existen para espacios, como `.lstrip()` y `.rstrip()`. ¿En qué se diferencian de `.strip()`?

**Ejercicio 8** — *Concepto 11 + 13: validar año, dos estrategias*
Crea `validar_anio(anio)` que retorne `True` si `anio` es un entero mayor que 0 y menor o igual a 2026.
- Versión con `isinstance()`.
- Versión con `try/except` que intente convertir a `int` y luego valide el rango.
*Investiga:* ¿qué retorna `isinstance(5.0, int)`? ¿Y `isinstance(5.0, (int, float))`? Pruébalo y anota el resultado — te ayudará a entender por qué a veces se usan tuplas de tipos.

**Ejercicio 9** — *Concepto 13: rango decimal*
Crea `validar_precio(precio)` que retorne `True` si es un número (entero o decimal) entre 1000 y 50000 inclusive.
*Pregúntate:* si el usuario ingresa exactamente `1000`, ¿debería ser válido? ¿Y `50000.01`? Decide tú el criterio y documéntalo con un comentario en tu código — en tu examen vas a tener que tomar decisiones similares con la nota (1.0 a 7.0).

**Ejercicio 10** — *Concepto 11: validar enteros no negativos*
Crea `validar_stock(cantidad)` que retorne `True` solo si es un entero mayor o igual a 0.
*Investiga:* ¿qué hace el método `.isdigit()` si lo aplicas a un string vacío `""`? ¿Y a `"-5"`? Prueba ambos casos y explica por qué `.isdigit()` por sí solo no es suficiente para validar números negativos.

**Ejercicio 11** — *Concepto 12 (ambos caminos) + texto*
Crea `validar_isbn(isbn)` que retorne `True` si `isbn` tiene exactamente 13 caracteres y todos son dígitos.
- Versión con `for` recorriendo carácter por carácter.
- Versión combinando `len()` e `.isdigit()`.
*Investiga:* ¿qué retorna `"123".isdigit()`? ¿Y `"12 3".isdigit()` (con un espacio en medio)? Esto te ayuda a entender por qué `.isdigit()` valida *cada carácter*, no el string como número completo.

**Ejercicio 12** — *Concepto 11: pedir hasta validar (while)*
Crea `solicitar_titulo_valido()`: usa un `while True` que pida un título por `input()`, lo valide con tu función del ejercicio 7, y solo retorne el título cuando sea válido. Si no es válido, imprime un mensaje de error *dentro de esta función* (no dentro de la validación).
*Pregúntate:* ¿por qué el mensaje de error va en `solicitar_titulo_valido()` y no en `tiene_contenido_v1()`? Relaciona esto con el Concepto 6 (separación de responsabilidades) — ¿qué pasaría si quisieras reutilizar `tiene_contenido_v1()` en otro contexto donde el mensaje de error debería ser distinto?

**Ejercicio 13** — *Concepto 11 (try/except) + conversión*
Crea `solicitar_precio_valido()` similar al anterior, pero usando `try/except` para manejar el caso en que el usuario ingresa texto no numérico.
*Investiga:* ¿qué tipo de excepción (`Exception`) lanza Python si haces `float("abc")`? Ejecuta ese código fuera de un `try/except` para ver el error completo, y luego identifica el nombre exacto de la excepción para usarlo en tu `except`.

---

## Bloque C: Listas de diccionarios (Ejercicios 14-22)

**Ejercicio 14** — *Concepto 15: crear un registro*
Crea `crear_libro(titulo, autor, anio, precio)` que retorne un diccionario con esos 4 campos más `"disponible": True`.
*Pregúntate:* ¿por qué `"disponible"` no es un parámetro de la función si su valor inicial siempre es el mismo? ¿En qué se parece esto al campo `"aprobado"` de tu examen?

**Ejercicio 15** — *Concepto 5 (mutabilidad aplicada a .append)*
Crea `agregar_libro(lista_libros, libro)` que haga `.append()` del diccionario a la lista, sin retornar nada.
*Investiga:* ¿qué pasa si en lugar de `.append(libro)` escribes `.append(libro.copy())`? Investiga qué hace `.copy()` en un diccionario y por qué podría importar si luego modificas la variable `libro` original.

**Ejercicio 16** — *Recorrer y mostrar*
Crea `mostrar_libros(lista_libros)` que recorra la lista e imprima cada libro (todos sus campos) con el formato que tú definas. Si la lista está vacía, debe mostrar un mensaje específico para ese caso.
*Pregúntate:* ¿cómo verificas en código si una lista está vacía? Hay al menos dos formas: `len(lista) == 0` y simplemente `if not lista:`. Investiga por qué la segunda funciona (pista: en Python, las listas vacías son "falsy").

**Ejercicio 17** — *Concepto 5: búsqueda, dos caminos*
Crea `buscar_por_titulo(lista_libros, titulo)` que retorne la posición del libro con ese título exacto, o `-1`.
- Versión con `range(len(...))`.
- Versión con `enumerate()`.
*Investiga:* ¿qué pasa si hay dos libros con el mismo título en la lista? ¿Cuál posición retorna tu función? ¿Es esto un problema, o es el comportamiento esperado para tu examen (donde se asume nombres únicos)?

**Ejercicio 18** — *Concepto 6: la búsqueda solo informa, no decide*
En tu programa principal (fuera de cualquier función), pide un título, llama a `buscar_por_titulo`, y según el resultado (-1 o posición válida) muestra el libro o un mensaje de "no encontrado".
*Pregúntate:* si quisieras que el mensaje de "no encontrado" fuera distinto en dos partes diferentes del programa (por ejemplo, al buscar dice "no existe" y al eliminar dice "no se puede eliminar porque no existe"), ¿podrías lograrlo si la función de búsqueda imprimiera el mensaje ella misma? ¿Por qué la solución actual sí lo permite?

**Ejercicio 19** — *Concepto 7: reutilizar función dentro de otra*
Crea `eliminar_libro(lista_libros, titulo)` que use `buscar_por_titulo` internamente: si la posición es válida, elimina con `.pop()`; si es -1, imprime un mensaje de "no encontrado".
*Investiga:* ¿cuál es la diferencia entre `lista.pop(posicion)` y `del lista[posicion]`? ¿Ambos sirven para este caso? Investiga si `.pop()` retorna algo y si eso te podría ser útil (por ejemplo, para mostrar qué se eliminó).

**Ejercicio 20** — *Concepto 8: recorrer y modificar todos*
Agrega un campo `"stock"` a tus libros. Crea `actualizar_disponibilidad(lista_libros)` que recorra **toda** la lista y ponga `"disponible": False` si `"stock" == 0`, y `True` en caso contrario.
*Pregúntate:* en este ejercicio usas `for libro in lista_libros:` (sin índices) y modificas `libro["disponible"]` directamente. En el ejercicio 5 (Bloque A) viste que reasignar una variable dentro de una función no afecta el original. ¿Por qué aquí SÍ funciona modificar `libro["disponible"]`? (Pista: no estás reasignando la variable `libro`, estás modificando el contenido del diccionario al que `libro` apunta).

**Ejercicio 21** — *Combinar funciones (como Concepto 8 + mostrar)*
Crea `mostrar_reporte(lista_libros)` que primero llame a `actualizar_disponibilidad` y luego muestre cada libro con un formato visual (usa separadores como `***` entre cada uno).
*Pregúntate:* ¿por qué tiene sentido que "mostrar" llame primero a "actualizar"? Piensa en un escenario donde el usuario cambió el stock de un libro justo antes de pedir el reporte — ¿qué pasaría si "mostrar" no actualizara primero?

**Ejercicio 22** — *Concepto 14: contar con condición*
Crea `contar_disponibles(lista_libros)` con dos versiones: una con contador y `for`, otra con `sum()` y expresión generadora.
*Investiga:* prueba ejecutar solo la parte `(1 for libro in lista_libros if libro["disponible"])` sin el `sum()` alrededor, e imprímela directamente. ¿Qué tipo de objeto es? Investiga qué es un "generador" en Python (no necesitas dominarlo, solo tener una idea de qué es).

---

## Bloque D: Menús y estructura del programa (Ejercicios 23-27)

**Ejercicio 23** — *Concepto 9: dispatcher simple*
Crea `mostrar_menu()` (imprime 4 opciones: Agregar, Buscar, Eliminar, Salir) y `leer_opcion()` (pide y retorna un número, validando con `.isdigit()` o `try/except` que sea un entero válido).
*Investiga:* busca qué significa el término "dispatcher" en otros contextos de programación (por ejemplo, "event dispatcher" en interfaces gráficas, o "dispatcher" en sistemas de emergencia/911). ¿Ves la analogía con "alguien que recibe una solicitud y la dirige al lugar correcto"?

**Ejercicio 24** — *Concepto 10: while True + break*
Crea el esqueleto: un `while True` que llame a `mostrar_menu()` y `leer_opcion()`, use `if/elif` para cada opción (de momento solo `print("Ejecutando opción X")`), y `break` en la opción de salir.
*Pregúntate:* ¿qué pasaría si olvidas el `break` en la opción de salir? Pruébalo deliberadamente (¡y prepárate para detener la ejecución con Ctrl+C si entra en loop infinito!). Esto te ayudará a recordar por qué es crítico.

**Ejercicio 25** — *Integración*
Conecta las funciones de los ejercicios 12-22 dentro del esqueleto del ejercicio 24.
*Pregúntate:* ¿en qué orden llamas las funciones dentro de cada opción del menú? Por ejemplo, para "agregar", ¿primero pides los datos o primero creas el diccionario vacío? Escribe en un comentario el orden de pasos *antes* de programarlo — esto se llama "pseudocódigo" y te ahorra errores.

**Ejercicio 26** — *Concepto 9 (dispatcher con diccionario) — opcional/avanzado*
Reescribe el dispatcher del ejercicio 24 usando un diccionario de funciones (como se mostró en el Concepto 9), en lugar de `if/elif`.
*Investiga:* ¿qué pasa si el usuario ingresa una opción que no está en el diccionario (por ejemplo, el número 99)? Investiga el método `.get()` de los diccionarios, que permite dar un valor por defecto si la clave no existe — ¿cómo lo usarías aquí para manejar una opción inválida sin que el programa falle?

**Ejercicio 27** — *Concepto 14 + integración*
Agrega al menú una opción "Estadísticas" que muestre: cuántos libros hay en total (`len()`), cuántos están disponibles (ejercicio 22), y cuántos no.
*Pregúntate:* si ya tienes el total y los disponibles, ¿necesitas otra función para calcular los no disponibles, o puedes obtenerlo con una simple resta? Reflexiona sobre cuándo vale la pena crear una función nueva vs. usar un cálculo directo.

---

## Bloque E: Estructuras anidadas — preparación para nivel avanzado (Ejercicio 28)

**Ejercicio 28** — *Listas dentro de diccionarios, validación contra conjunto de valores*
Agrega un campo `"categoria"` a tus libros (valores posibles: `"Novela"`, `"Ciencia"`, `"Historia"`).
- Crea `validar_categoria(categoria, categorias_validas)` que retorne `True` si `categoria` está en la lista `categorias_validas`.
  - Versión con `for` y comparación manual.
  - Versión con el operador `in`.
- Crea `buscar_por_categoria(lista_libros, categoria)` que retorne una **lista nueva** con todos los libros de esa categoría (no una posición — puede haber varios resultados).
*Investiga:* ¿cuál es la diferencia conceptual entre una función que retorna una *posición* (un número) y una que retorna una *lista nueva* (una colección)? ¿En qué casos necesitas cada una? Esto te prepara para situaciones donde "puede haber más de un resultado válido".

---

## Bloque F: Ejercicios "espejo" del examen (Ejercicios 29-30)

Estos dos ejercicios replican **la estructura completa** de tu examen, con datos distintos (no estudiantes), para que practiques el flujo de principio a fin sin memorizar respuestas.

**Ejercicio 29 — Sistema de gestión de vehículos en un taller mecánico**

Cada vehículo es un diccionario con:
- `"patente"`: no vacía ni solo espacios.
- `"kilometraje"`: entero mayor que 0.
- `"costo_reparacion"`: decimal entre 10000.0 y 500000.0.
- `"reparado"`: booleano, inicia en `False`. Se actualiza a `True` cuando se ejecuta "Actualizar estados", según una regla que tú definas (por ejemplo: si `costo_reparacion <= 100000.0`, se considera reparación simple y se marca como reparado).

Menú de 6 opciones (igual estructura que tu examen): Agregar, Buscar (por patente), Eliminar, Actualizar estados, Mostrar, Salir.

Debes implementar, como funciones separadas:
- `mostrar_menu()` y `leer_opcion()`.
- Función de agregar que reciba la lista, pida los datos, y llame a una función de validación distinta para cada campo (mensajes de error en la función de agregar, no en las validaciones — Concepto 12 aplicado).
- Función de búsqueda que retorne posición o `-1` (Concepto 5).
- Eliminar reutilizando la búsqueda (Concepto 7).
- Actualizar estados recorriendo toda la lista sin excepción (Concepto 8).
- Mostrar con formato específico, definido por ti, con separadores.

*Antes de programar:* dibuja en papel (o en un comentario) el diagrama de qué función llama a cuál. Por ejemplo: "Mostrar → llama a → Actualizar estados → recorre lista". Esto se llama un "diagrama de flujo de control" y te ayuda a no perderte cuando el programa crece.

**Ejercicio 30 — Sistema de gestión de empleados**

Mismo formato que el ejercicio 29, pero con empleados:
- `"nombre"`: no vacío ni solo espacios.
- `"horas_trabajadas"`: entero mayor que 0.
- `"sueldo_base"`: decimal entre 300000.0 y 3000000.0.
- `"bono"`: booleano, inicia en `False`, se actualiza a `True` si `horas_trabajadas >= 180`.

Mismo menú de 6 opciones, mismas funciones separadas.

*Esta vez, hazlo sin mirar el ejercicio 29.* Si te trabas en algo específico (por ejemplo, "¿cómo era la función de búsqueda?"), vuelve a los ejercicios del Bloque C en lugar de copiar directamente del 29 — el objetivo es que la lógica quede en tu cabeza, no en tu copy-paste.

---

## Ejercicio 31 — Desafío final (opcional, mayor dificultad)

**Sistema de gestión de pedidos de un restaurante**

Este ejercicio introduce conceptos *nuevos* que no se cubrieron en el taller, para quienes quieran ir más allá:

- Cada pedido es un diccionario con: `"cliente"`, `"items"` (una **lista** de diccionarios, cada uno con `"nombre_plato"` y `"precio"`), `"propina_porcentaje"` (decimal entre 0 y 30) y `"estado"` (string: `"pendiente"`, `"en preparación"`, `"entregado"`).

**Nuevos retos:**

1. **Listas dentro de diccionarios dentro de listas** ("estructuras anidadas"). Para mostrar un pedido, necesitas un `for` que recorra los pedidos, y *dentro* de ese `for`, otro `for` que recorra los items de cada pedido. Esto se llama **anidamiento de ciclos**.

2. **Sub-ciclo de captura de datos**: al agregar un pedido, no sabes de antemano cuántos platos pedirá el cliente. Necesitas un ciclo que pregunte "¿desea agregar otro plato? (s/n)" repetidamente, agregando cada plato a la lista `"items"` del pedido.

3. **Búsqueda con múltiples resultados**: a diferencia de `buscar_por_titulo` (que asumía nombres únicos), aquí un cliente puede tener varios pedidos. Tu función `buscar_por_cliente(lista_pedidos, cliente)` debe retornar una **lista de posiciones** (no una sola), que podría estar vacía si no hay coincidencias.

4. **Cálculo compuesto**: `calcular_total_pedido(pedido)` debe sumar los precios de todos los items (otro `for` anidado) y luego aplicar el porcentaje de propina sobre ese subtotal.

5. **Actualización condicional más compleja**: en "Actualizar estados", los pedidos `"pendiente"` con más de 3 items pasan a `"en preparación"` automáticamente; define tú las demás reglas de transición.

*Investiga antes de empezar:* busca el término "nested loops" (ciclos anidados) y mira al menos un ejemplo donde se recorra una lista de listas o una lista de diccionarios que contienen listas. Dibuja en papel la estructura de datos completa de un pedido de ejemplo con 2-3 items, para visualizar cómo se accede a cada nivel (`pedido["items"][0]["nombre_plato"]`, por ejemplo).

---

## Cómo usar este material si "casi no entiendes nada"

1. No saltes el Mini-taller. Cada concepto tiene un número — si en un ejercicio te trabas, vuelve al concepto referenciado.
2. Ejecuta TODO. No leas el código y asumas que entiendes — escríbelo, córrelo, cambia valores y observa qué pasa.
3. Las preguntas "¿Pregúntate?" e "¿Investiga?" no son opcionales para este perfil — son las que construyen la comprensión real, no solo la memorización del patrón.

## Cómo usar este material si "te resulta fácil"

1. No te saltes las preguntas de "Investiga" — son las que te llevan a conceptos que probablemente no conoces aún (generadores, `.get()` en diccionarios, excepciones específicas, mutabilidad profunda).
2. En los ejercicios con "dos versiones", no te quedes solo con la que te resulte más cómoda — domina ambas, porque en el examen o en una entrevista te pueden pedir explicar la alternativa.
3. El Ejercicio 31 es tu verdadero desafío — intenta resolverlo sin pistas adicionales antes de buscar ayuda.