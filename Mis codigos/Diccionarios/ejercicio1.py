# Ejercicio 1: Nivel fácil
# Crea un diccionario llamado libro con estas claves: titulo, autor y anio.

# Luego:

# Muestra cada dato con print().
# Cambia el año por uno más reciente.
# Agrega una nueva clave llamada editorial.

libro = {
    "titulo" : "Harry Potter", 
    "autor" : "JKR",
    "anio" : 1990
}

print(libro["titulo"])
print(libro["autor"])
print(libro["anio"])

print("\nCon For")
for clave, valor in libro.items():
    print(clave, valor)

libro["anio"] = 2000
libro["editorial"] = "Zig-Zag"

print("\nDatos actualizados:")
for clave, valor in libro.items():
    print(f"Clave: {clave} | Valor: {valor}")