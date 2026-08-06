""" Ejercicio 1: Calentamiento

Crea una variable llamada saludo y asígnale exactamente el texto 'Hola Mundo'.

Ejemplo esperado:

saludo = 'Hola Mundo'

Ejercicio 2: Matemáticas Rápidas

Crea una variable llamada total que guarde el resultado de la operación: primero suma 15 + 25 y luego multiplica ese resultado por 2.

Ejemplo esperado:

total = (15 + 25) * 2

Ejercicio 3: El Guardián (If/Else)

Tienes una variable llamada nota.

Debes crear una nueva variable llamada estado que guarde:

'Aprobado' si nota es mayor o igual a 4.0
'Reprobado' si nota es menor que 4.0
Pista: usa un if con else.



Ejercicio 4: Ciclo While Básico

Usa un ciclo while para sumar los números del 1 al 5.

Debes guardar el resultado final en la variable suma.

Pista: puedes usar una variable contador que comience en 1 y vaya aumentando.



Ejercicio 5: Ciclo For y Rango

Usa un ciclo for con range() para sumar todos los números del 0 al 10, incluyendo el 10.

Guarda el resultado en la variable resultado.

Pista: recuerda que range(11) llega hasta 10.



Ejercicio 6: Extracción de Vocales

Tienes una cadena llamada palabra.

Debes recorrerla con un ciclo for y contar cuántas veces aparece la letra 'a' minúscula.

El resultado debe guardarse en la variable contador_a.

Ejemplo:

Si palabra = 'manzana', entonces contador_a debe ser 3.

Ejercicio 7: Mi Primera Lista

Crea una lista llamada inventario que contenga estos tres elementos, en este orden:

'Espada'
'Escudo'
'Poción'
Ejercicio 8: Agregando Elementos

Tienes una lista llamada mochila.

Debes agregar al final el texto 'Mapa' usando el método correcto de listas.

Pista: el método que necesitas es append().



Ejercicio 9: Sumando una Lista

Tienes una lista llamada precios con varios números.

Debes recorrerla con un ciclo for y sumar todos sus valores.

El resultado debe guardarse en la variable total_pagar.

Ejemplo:

Si precios = [1000, 2500, 500], entonces total_pagar = 4000.

Ejercicio 10: Creando un Diccionario

Crea un diccionario llamado perfil con estas claves y valores:

'nombre': 'Ash'
'edad': 10
Ejercicio 11: Acceso a Diccionarios

Tienes un diccionario llamado enemigo.

Debes extraer el valor de la clave 'hp' y guardarlo en una variable llamada salud_actual.

Ejemplo:

Si enemigo = {'nombre': 'Slime', 'hp': 45}, entonces salud_actual = 45.

Ejercicio 12: Recorriendo un Diccionario

Tienes un diccionario llamado ventas, donde:

la clave es el nombre del producto
el valor es el monto vendido
Debes recorrer el diccionario y sumar todos los valores.

El resultado debe guardarse en total_ventas.

Pista: puedes usar .values() o .items().



Ejercicio 13: La Búsqueda (Lista + Condicional)

Tienes una lista llamada edades.

Debes contar cuántos valores son mayores o iguales a 18.

Guarda el resultado en la variable mayores_edad.

Ejemplo:

Si edades = [15, 18, 22, 12, 40], entonces mayores_edad = 3.

Ejercicio 14: Lista de Diccionarios

Tienes una lista llamada alumnos.

Cada elemento de esa lista es un diccionario con estas claves:

'nombre'
'nota'
Debes contar cuántos alumnos tienen una nota mayor o igual a 4.0.

Guarda el resultado en la variable aprobados.

Ejercicio 15: Boss Final 🐉

Tienes un diccionario llamado tienda.

Cada clave representa un producto, y su valor es otro diccionario con:

'precio'
'stock'
Tu tarea es calcular el valor total de todo el inventario.

Eso significa multiplicar precio * stock de cada producto y sumar todos esos resultados.

Guarda el total en la variable capital_total.

Ejemplo:

Si

tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}

entonces

capital_total = 350

Ejercicio 16: Frecuencias Clásicas

Tienes una lista llamada votos.

Debes crear un diccionario llamado resultados que cuente cuántas veces aparece cada opción.

Ejemplo:

Si votos = ['A', 'A', 'B'], entonces resultados = {'A': 2, 'B': 1}.

Pista: recorre la lista y verifica si cada elemento ya existe en el diccionario.



Ejercicio 17: El Campeón (Búsqueda de Máximo)

Tienes una lista llamada jugadores.

Cada elemento es un diccionario con:

'nombre'
'pts'
Debes encontrar al jugador con más puntos y guardar su nombre en la variable mejor_jugador.

Ejemplo:

Si jugadores = [{'nombre': 'Ash', 'pts': 150}, {'nombre': 'Gary', 'pts': 200}], entonces mejor_jugador = 'Gary'.

Ejercicio 18: Agrupación Clasificatoria

Tienes una lista llamada numeros.

Debes clasificar sus valores en un diccionario llamado clasificacion:

en la lista clasificacion['pares'] debes guardar los números pares
en la lista clasificacion['impares'] debes guardar los números impares
Pista: usa el operador % para verificar si un número es par o impar.



Ejercicio 19: Inventario Cruzado

Tienes:

una lista llamada compras, con nombres de productos comprados
un diccionario llamado precios, donde cada producto tiene su costo
Debes calcular el total sumando el precio de cada producto comprado.

Si el subtotal es mayor a 200, aplica un descuento del 10%.

Guarda el resultado final en total_final.

Ejemplo:

Si compras = ['espada', 'pocion', 'espada'] y precios = {'espada': 100, 'pocion': 50}, entonces el subtotal es 250 y el total final es 225.0.

Ejercicio 20: Jefe Supremo ☠️

Tienes un diccionario llamado catalogo.

Cada clave es una categoría y su valor es una lista de productos.

Debes recorrer todas las categorías y guardar en la lista todo_stock únicamente los productos que tengan más de 4 letras.

Ejemplo:

Si

catalogo = {'armas': ['espada', 'arco', 'hacha'], 'pociones': ['luz', 'mana', 'vida']}

entonces todo_stock debe contener solo ['espada', 'hacha']"""