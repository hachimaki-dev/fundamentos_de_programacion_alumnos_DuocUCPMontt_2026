'''Crea un diccionario llamado libro con estas claves: titulo, autor y anio.

Luego:

    Muestra cada dato con print().
    Cambia el año por uno más reciente.
    Agrega una nueva clave llamada editorial.'''

libro = {
    "titulo": "The Call of Cthulhu",
    "autor": "H.P. Lovecraft",
    "anio": 1928
}

for clave, valor in libro.items():
    print(f"{clave}: {valor}")

libro["anio"] = 2017
libro["editorial"] = "Alma Editorial"
print("\nDatos recientes: ")
for clave, valor in libro.items():
    print(f"{clave}: {valor}")
