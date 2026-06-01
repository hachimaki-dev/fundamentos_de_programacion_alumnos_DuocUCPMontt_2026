#DICCIONARIO:
# --- 1. clear() ---
# Descripción: Elimina todos los elementos del diccionario.
usuario = {"nombre": "Ana", "edad": 25}
usuario.clear()
print("Resultado clear():", usuario)  # Salida: {}

# --- 2. copy() ---
# Descripción: Devuelve una copia del diccionario.
original = {"a": 1, "b": 2}
copia = original.copy()
print("Resultado copy():", copia)  # Salida: {"a": 1, "b": 2}

# --- 3. fromkeys() ---
# Descripción: Devuelve un diccionario con las llaves y el valor especificados.
llaves = ["id", "rol", "estado"]
# Crea un diccionario nuevo asignando el valor "N/A" a todas las llaves
nuevo = dict.fromkeys(llaves, "N/A")
print("Resultado fromkeys():", nuevo)  # Salida: {"id": "N/A", "rol": "N/A", "estado": "N/A"}

# --- 4. get() ---
# Descripción: Devuelve el valor de la llave especificada.
precios = {"pan": 1.5, "leche": 2.0}
# Si la llave existe, devuelve su valor. Si no existe, devuelve None (evita errores)
print("Resultado get():", precios.get("pan"))  # Salida: 1.5

# --- 5. items() ---
# Descripción: Devuelve una lista que contiene una tupla por cada par de llave-valor.
auto = {"marca": "Ford", "año": 2020}
print("Resultado items():", list(auto.items()))  # Salida: [("marca", "Ford"), ("año", 2020)]

# --- 6. keys() ---
# Descripción: Devuelve una lista que contiene las llaves del diccionario.
frutas = {"manzana": 5, "pera": 3}
print("Resultado keys():", list(frutas.keys()))  # Salida: ["manzana", "pera"]

# --- 7. pop() ---
# Descripción: Elimina el elemento con la llave especificada (y te devuelve su valor).
productos = {"id": 101, "nombre": "Teclado"}
nombre_eliminado = productos.pop("nombre")
print("Resultado pop():", productos)  # Salida: {"id": 101}

# --- 8. popitem() ---
# Descripción: Elimina el último par de llave-valor que fue insertado.
config = {"tema": "oscuro", "fuente": "Arial", "zoom": 100}
config.popitem()
print("Resultado popitem():", config)  # Salida: {"tema": "oscuro", "fuente": "Arial"}

# --- 9. setdefault() ---
# Descripción: Devuelve el valor de la llave especificada. 
# Si la llave no existe: inserta la llave con el valor especificado.
datos = {"nombre": "Luis"}
# Como "pais" no existe en el diccionario, lo agrega automáticamente con el valor "Chile"
pais = datos.setdefault("pais", "Chile")
print("Resultado setdefault():", datos)  # Salida: {"nombre": "Luis", "pais": "Chile"}


# --- 10. update() ---
# Descripción: Actualiza el diccionario con los pares de llave-valor especificados.
empleado = {"nombre": "Carlos", "edad": 30}
# Modifica llaves existentes o agrega nuevas si no existen dentro del diccionario
empleado.update({"edad": 31, "ciudad": "Santiago"})
print("Resultado update():", empleado)  # Salida: {"nombre": "Carlos", "edad": 31, "ciudad": "Santiago"}


# --- 11. values() ---
# Descripción: Devuelve una lista de todos los valores en el diccionario.
notas = {"matematicas": 6.5, "historia": 5.8}
print("Resultado values():", list(notas.values()))  # Salida: [6.5, 5.8]