# Bloque 1: Variables y aritmética

### Ejercicio 1: Hola mundo

Crea una variable llamada `saludo` y asígnale el texto `'Hola Mundo'`. Luego, muestra su contenido en pantalla.

**Resultado esperado en consola:**

```text
Hola Mundo
```

### Ejercicio 2: Matemática rápida

Crea una variable llamada `total` y asígnale el resultado de sumar `15 + 25` y luego multiplicar ese resultado por `2`. Imprime el valor de `total`.

**Pista:** Usa paréntesis para que primero se realice la suma.

**Resultado esperado en consola:**

```text
80
```

### Ejercicio 3: Estado de aprobación

Define una variable `nota` con el valor `3.5`. Luego, crea una variable `estado` que almacene lo siguiente:

* `'Aprobado'` si `nota` es mayor o igual a `4.0`
* `'Reprobado'` en caso contrario

Finalmente, imprime `estado`.

**Resultado esperado en consola:**

```text
Reprobado
```

---

# Bloque 2: Ciclos e iteraciones

### Ejercicio 4: Suma con `while`

Crea una variable `suma` con valor `0` y una variable `contador` con valor `1`. Usa un ciclo `while` para que, mientras `contador` sea menor o igual a `5`, se agregue `contador` a `suma` y luego `contador` aumente en `1`. Al final, imprime `suma`.

**Resultado esperado en consola:**

```text
15
```

### Ejercicio 5: Suma con `for`

Crea una variable `resultado` con valor `0`. Usa un ciclo `for` y `range()` para sumar todos los números desde `0` hasta `10`, incluyendo el `10`. Al final, imprime `resultado`.

**Pista:** `range(11)`

**Resultado esperado en consola:**

```text
55
```

### Ejercicio 6: Contador de letras

Define la variable `palabra` con el valor `'manzana'`. Crea una variable `contador_a` con valor `0`. Recorre la palabra con un ciclo `for` y, cada vez que encuentres la letra `'a'`, suma `1` al contador. Al final, imprime `contador_a`.

**Resultado esperado en consola:**

```text
3
```

---

# Bloque 3: Listas y colecciones

### Ejercicio 7: Mi primera lista

Crea una lista llamada `inventario` con los elementos `'Espada'`, `'Escudo'` y `'Poción'`. Imprime la lista completa.

**Resultado esperado en consola:**

```text
['Espada', 'Escudo', 'Poción']
```

### Ejercicio 8: Agregar elementos a una lista

Crea una lista llamada `mochila` con los elementos `'Pan'` y `'Cuerda'`. Luego, usa `.append()` para agregar `'Mapa'`. Imprime la lista final.

**Resultado esperado en consola:**

```text
['Pan', 'Cuerda', 'Mapa']
```

### Ejercicio 9: Sumar valores de una lista

Define la lista `precios = [1000, 2500, 500]`. Crea una variable `total_pagar` con valor `0`. Recorre la lista con un ciclo `for`, suma cada precio a `total_pagar` e imprime el resultado final.

**Resultado esperado en consola:**

```text
4000
```

---

# Bloque 4: Diccionarios

### Ejercicio 10: Crear un diccionario

Crea un diccionario llamado `perfil` con las claves y valores siguientes:

* `'nombre'`: `'Ash'`
* `'edad'`: `10`

Imprime el diccionario completo.

**Resultado esperado en consola:**

```text
{'nombre': 'Ash', 'edad': 10}
```

### Ejercicio 11: Acceder a un dato del diccionario

Define el diccionario `enemigo = {'nombre': 'Slime', 'hp': 45}`. Extrae el valor de la clave `'hp'`, guárdalo en una variable llamada `salud_actual` e imprime esa variable.

**Resultado esperado en consola:**

```text
45
```

### Ejercicio 12: Sumar los valores de un diccionario

Define el diccionario `ventas = {'taza': 500, 'plato': 1200, 'vaso': 300}`. Crea una variable `total_ventas` con valor `0`. Recorre los valores del diccionario, súmalos y luego imprime el total.

**Resultado esperado en consola:**

```text
2000
```

---

# Bloque 5: Lógica intermedia

### Ejercicio 13: Contar mayores de edad

Define la lista `edades = [15, 18, 22, 12, 40]`. Crea una variable `mayores_edad` con valor `0`. Recorre la lista y suma `1` cada vez que encuentres un número mayor o igual a `18`. Imprime el contador.

**Resultado esperado en consola:**

```text
3
```

### Ejercicio 14: Lista de diccionarios

Crea una lista llamada `alumnos` que contenga estos dos diccionarios:

```python
{'nombre': 'Ana', 'nota': 5.0}
{'nombre': 'Luis', 'nota': 3.0}
```

Luego, cuenta cuántos alumnos tienen una nota mayor o igual a `4.0` y guarda ese valor en una variable llamada `aprobados`. Imprime `aprobados`.

**Resultado esperado en consola:**

```text
1
```

### Ejercicio 15: Valor total del inventario

Define el diccionario:

```python
tienda = {
    'pocion': {'precio': 50, 'stock': 3},
    'espada': {'precio': 200, 'stock': 1}
}
```

Crea una variable `capital_total` con valor `0`. Recorre los productos, multiplica `precio × stock` para cada uno y suma ese valor al total. Luego, imprime `capital_total`.

**Resultado esperado en consola:**

```text
350
```

---

# Bloque 6: Algoritmos avanzados

### Ejercicio 16: Contador de votos

Define la lista `votos = ['A', 'A', 'B', 'C', 'A', 'B']`. Crea un diccionario vacío llamado `resultados`. Recorre la lista y cuenta cuántas veces aparece cada letra. Guarda ese conteo en el diccionario e imprime el resultado final.

**Resultado esperado en consola:**

```text
{'A': 3, 'B': 2, 'C': 1}
```

### Ejercicio 17: El jugador con más puntos

Define la lista:

```python
jugadores = [
    {'nombre': 'Ash', 'pts': 150},
    {'nombre': 'Gary', 'pts': 200}
]
```

Encuentra el nombre del jugador con más puntos y guárdalo en una variable llamada `mejor_jugador`. Imprime esa variable.

**Resultado esperado en consola:**

```text
Gary
```

### Ejercicio 18: Clasificar pares e impares

Define la lista `numeros = [1, 2, 3, 4]`. Crea un diccionario llamado `clasificacion` con esta estructura:

```python
{'pares': [], 'impares': []}
```

Recorre la lista y guarda cada número en la lista correspondiente según si es par o impar. Imprime el diccionario final.

**Resultado esperado en consola:**

```text
{'pares': [2, 4], 'impares': [1, 3]}
```

### Ejercicio 19: Carrito con descuento

Define `compras = ['espada', 'pocion', 'espada']` y `precios = {'espada': 100, 'pocion': 50}`. Calcula el subtotal de la compra. Si el subtotal es mayor que `200`, aplica un descuento del `10%` y guarda el valor final en una variable llamada `total_final`. Imprime el resultado.

**Resultado esperado en consola:**

```text
225.0
```

### Ejercicio 20: Filtrar productos por longitud

Define el diccionario `catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}`. Crea una lista vacía llamada `todo_stock`. Recorre todas las categorías y agrega a esa lista solo los productos que tengan más de `5` letras. Luego, imprime `todo_stock`.

**Resultado esperado en consola:**

```text
['espada', 'pocion']
```
