# Diccionarios en Python

## Lectura guiada

Hasta ahora ya has trabajado con listas, que son colecciones ordenadas de elementos. Los diccionarios, en cambio, nos permiten guardar información en pares de **clave : valor**. Esta diferencia es fundamental, porque en vez de pensar en la posición de un dato, pensamos en su significado.

Por ejemplo, en una lista puedes guardar nombres:

```python
nombres = ["Ana", "Luis", "Marta"]
```

Pero si quieres guardar información más completa sobre una persona, una lista ya no es la mejor opción. Ahí aparece el diccionario:

```python
persona = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería"
}
```

En este caso, cada clave representa un concepto claro. La clave `"nombre"` está asociada al valor `"Ana"`; la clave `"edad"` está asociada al valor `20`.

Eso hace que los diccionarios sean muy útiles cuando queremos modelar información real: estudiantes, productos, cuentas bancarias, pedidos, videojuegos, usuarios de una aplicación, etc.

### 1. ¿Qué es un diccionario?

Un diccionario es una estructura de datos que almacena información en formato **clave : valor**. Las claves deben ser únicas dentro del diccionario. Los valores sí pueden repetirse.

```python
producto = {
    "nombre": "Notebook",
    "precio": 599990,
    "stock": 10
}
```

Aquí:

* `"nombre"` es una clave
* `"Notebook"` es su valor
* `"precio"` es otra clave
* `599990` es su valor

### 2. ¿Cómo se accede a los datos?

En una lista usamos índices:

```python
colores = ["rojo", "verde", "azul"]
print(colores[0])
```

En un diccionario usamos claves:

```python
print(producto["nombre"])
```

Esto imprime:

```python
Notebook
```

Si intentas acceder a una clave que no existe, Python genera error. Por eso conviene usar `get()` cuando no estamos completamente seguros de que la clave esté presente.

```python
print(producto.get("marca"))
```

Esto devuelve `None` si la clave no existe, en lugar de romper el programa.

### 3. Agregar y modificar datos

Los diccionarios son mutables, es decir, se pueden cambiar.

```python
persona = {
    "nombre": "Ana",
    "edad": 20
}

persona["edad"] = 21
persona["carrera"] = "Programación"
```

Después de esto, el diccionario tendrá tres claves. Si la clave ya existía, se actualiza. Si no existía, se agrega.

### 4. Eliminar datos

También podemos eliminar elementos.

```python
persona = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Programación"
}

del persona["edad"]
```

Otra forma segura es usar `pop()`:

```python
carrera = persona.pop("carrera")
```

`pop()` elimina la clave y además devuelve su valor.

### 5. Recorrer un diccionario

Una de las cosas más importantes en programación es recorrer estructuras de datos. En los diccionarios esto puede hacerse de varias maneras.

#### Recorrer solo las claves

```python
persona = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Programación"
}

for clave in persona:
    print(clave)
```

#### Recorrer las claves y los valores

```python
for clave, valor in persona.items():
    print(clave, valor)
```

Esto es muy útil porque te permite mostrar información de forma ordenada.

#### Recorrer solo los valores

```python
for valor in persona.values():
    print(valor)
```

### 6. Diccionarios dentro de listas

En la práctica, muchas veces los diccionarios no trabajan solos. Es muy común ver listas que contienen diccionarios.

```python
estudiantes = [
    {"nombre": "Ana", "nota": 6.0},
    {"nombre": "Luis", "nota": 5.5},
    {"nombre": "Marta", "nota": 7.0}
]
```

Esta estructura sirve para representar grupos de elementos con características parecidas.

Por ejemplo, si quieres mostrar los nombres de todos los estudiantes:

```python
for estudiante in estudiantes:
    print(estudiante["nombre"])
```

### 7. ¿Por qué los diccionarios son tan importantes?

Porque permiten representar información de manera más natural. Cuando un dato tiene nombre propio, sentido y relación con otros datos, un diccionario suele ser la mejor elección.

Además, aparecen en muchos contextos reales:

* formularios
* JSON
* APIs
* configuración de programas
* inventarios
* registros de usuarios

### 8. Idea clave para recordar

Una lista responde muy bien a la pregunta: **¿qué elemento está en esta posición?**

Un diccionario responde muy bien a la pregunta: **¿qué valor corresponde a esta clave?**

Esa diferencia cambia por completo la forma de pensar los programas.

## Ejemplo integrador

```python
persona = {
    "nombre": "Carla",
    "edad": 22,
    "notas": [6.0, 5.8, 7.0]
}

print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Notas:", persona["notas"])

suma = 0
for nota in persona["notas"]:
    suma += nota

promedio = suma / len(persona["notas"])
print("Promedio:", promedio)
```

En este ejemplo ya aparecen varias ideas juntas: diccionarios, listas, `for`, operaciones matemáticas y salida por pantalla.

## Ejercicios

### Ejercicio 1: Nivel fácil

Crea un diccionario llamado `libro` con estas claves: `titulo`, `autor` y `anio`.

Luego:

1. Muestra cada dato con `print()`.
2. Cambia el año por uno más reciente.
3. Agrega una nueva clave llamada `editorial`.

### Ejercicio 2: Nivel medio

Crea una lista llamada `productos` que contenga al menos 3 diccionarios. Cada diccionario debe tener:

* `nombre`
* `precio`
* `stock`

Luego:

1. Recorre la lista con `for`.
2. Muestra el nombre y precio de cada producto.
3. Usa `if` para indicar cuáles productos tienen stock mayor que 0.
4. Al final, imprime cuántos productos están disponibles.

### Ejercicio 3: Nivel difícil

Crea un programa que simule un pequeño registro de estudiantes.

Debes usar:

* `while`
* `for`
* `if`
* listas
* diccionarios
* `print()`

El programa debe hacer lo siguiente:

1. Tener una lista de estudiantes, donde cada estudiante sea un diccionario con `nombre`, `edad` y `notas`.
2. Recorrer la lista y mostrar el nombre de cada estudiante.
3. Calcular el promedio de notas de cada estudiante usando un `for`.
4. Si el promedio es mayor o igual a 4.0, mostrar que está aprobado; si no, mostrar que está reprobado.
5. Usar un `while` para repetir una consulta: el usuario escribe el nombre de un estudiante y el programa busca si existe.
6. Si lo encuentra, mostrar todos sus datos; si no, indicar que no está registrado.
7. El ciclo debe terminar cuando el usuario escriba `salir`.

### Preguntas de validación

Responde por escrito:

1. ¿Cuál es la diferencia entre una lista y un diccionario?
2. ¿Qué es una clave?
3. ¿Qué ocurre si intentas acceder a una clave que no existe?
4. ¿Cuándo conviene usar un diccionario en vez de una lista?
5. ¿Por qué `items()` es útil cuando recorres diccionarios?

## Cierre

Los diccionarios son una de las estructuras más importantes de Python porque permiten modelar información real de forma clara, flexible y ordenada. Si dominas bien listas, condicionales y ciclos, los diccionarios se vuelven una herramienta muy poderosa para construir programas más útiles y más cercanos a problemas reales.