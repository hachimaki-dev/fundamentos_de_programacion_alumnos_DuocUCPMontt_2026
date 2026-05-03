# Tienes una lista llamada jugadores.

# Cada elemento es un diccionario con:

#    'nombre'
#    'pts'

# Debes encontrar al jugador con más puntos y guardar su nombre en la variable mejor_jugador.

jugadores = [
    {
        "nombre": "Matias",
        "pts": 5
    },
    {
        "nombre": "Marianny",
        "pts": 15
    },
    {
        "nombre": "Claudio",
        "pts": 7
    },
    {
        "nombre": "Sofia",
        "pts": 2
    },
    {
        "nombre": "Pablo",
        "pts": 12
    }
]

mejor_jugador = jugadores[0]

for i in range(len(jugadores)):
    if jugadores[i].get("pts") > mejor_jugador.get("pts"):
        mejor_jugador = jugadores[i]

print(f"El mejor jugador es: {mejor_jugador.get("nombre")}")