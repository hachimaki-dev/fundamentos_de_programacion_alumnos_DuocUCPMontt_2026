"""
### Ejercicio 1: Nivel fácil

Crea un diccionario llamado `libro` con estas claves: `titulo`, `autor` y `anio`.

Luego:

1. Muestra cada dato con `print()`.
2. Cambia el año por uno más reciente.
3. Agrega una nueva clave llamada `editorial`.
"""

Libro = {
    "Titulo": "Black clover",
    "Autor": "Yūki Tabata",
    "Año": 2015,
}

print("Titulo:", Libro["Titulo"], "\n", "Autor:", Libro["Autor"], "\n", "Año:", Libro["Año"])

Libro["Editorial"] = "Shūeisha"

print("Editorial:", Libro["Editorial"])