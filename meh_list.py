# MÉTODOS DE LISTAS EN PYTHON
# --- 1. append() ---
# Descripción: Añade un elemento al final de la lista.
frutas = ["manzana", "banana"]
frutas.append("cereza")
print("Resultado append():", frutas)  # Salida: ["manzana", "banana", "cereza"]

# --- 2. clear() ---
# Descripción: Elimina todos los elementos de la lista.
numeros = [1, 2, 3, 4]
numeros.clear()
print("Resultado clear():", numeros)  # Salida: []

# --- 3. copy() ---
# Descripción: Devuelve una copia de la lista.
original = ["a", "b", "c"]
copia = original.copy()
print("Resultado copy():", copia)  # Salida: ["a", "b", "c"]

# --- 4. count() ---
# Descripción: Devuelve el número de elementos que tienen el valor especificado.
letras = ["a", "b", "a", "c", "a"]
cantidad = letras.count("a")
print("Resultado count():", cantidad)  # Salida: 3

# --- 5. extend() ---
# Descripción: Añade los elementos de una lista (o cualquier iterable) al final de la lista actual.
lista1 = [1, 2, 3]
lista2 = [4, 5]
lista1.extend(lista2)
print("Resultado extend():", lista1)  # Salida: [1, 2, 3, 4, 5]

# --- 6. index() ---
# Descripción: Devuelve el índice (posición) del primer elemento con el valor especificado.
colores = ["rojo", "azul", "verde", "azul"]
posicion = colores.index("azul")
print("Resultado index():", posicion)  # Salida: 1 (encuentra la primera coincidencia)

# --- 7. insert() ---
# Descripción: Añade un elemento en la posición especificada.
tareas = ["estudiar", "cocinar"]
# Inserta "ejercicio" en la posición 1, desplazando los demás elementos
tareas.insert(1, "ejercicio")
print("Resultado insert():", tareas)  # Salida: ["estudiar", "ejercicio", "cocinar"]

# --- 8. pop() ---
# Descripción: Elimina el elemento en la posición especificada (si no pones posición, elimina el último).
paises = ["Chile", "Argentina", "Perú"]
pais_eliminado = paises.pop(1)  # Elimina el elemento en el índice 1
print("Resultado pop():", paises)  # Salida: ["Chile", "Perú"]

# --- 9. remove() ---
# Descripción: Elimina el primer elemento que tenga el valor especificado.
mascotas = ["perro", "gato", "loro", "gato"]
mascotas.remove("gato")  # Elimina solo el primer "gato" que encuentra
print("Resultado remove():", mascotas)  # Salida: ["perro", "loro", "gato"]

# --- 10. reverse() ---
# Descripción: Invierte el orden actual de la lista.
orden = [10, 20, 30]
orden.reverse()
print("Resultado reverse():", orden)  # Salida: [30, 20, 10]

# --- 11. sort() ---
# Descripción: Ordena la lista (por defecto de forma ascendente o alfabética).
desordenados = [5, 2, 9, 1]
desordenados.sort()
print("Resultado sort():", desordenados)  # Salida: [1, 2, 5, 9]"""