bandera = True
vida_boss = 100
nombre_jugador = ""
import sys

print("Bienvenido al juego de python")
nombre_jugador = input("¿Comó te llamas?")
print(f"Vale {nombre_jugador}. Es un gusto conocerte, pero para tu desgracia, en este preciso momento que tiene 100 puntos de vida")

while bandera:
    ataque = int(input("¿Cuanto daño le haz provocado a este Gran Boss?"))
    if ataque == 100:
        print(f"Wow {nombre_jugador}, eres demasiado fuerte, LO HAZ VENCIDO DE UN GOLPE")
        bandera = False
        sys.exit ()
    if ataque < 0:
        print(f"Una lastima, no le has lastimads, el Gran Boss tiene {vida_boss} puntos de vida")
    if ataque >= 0:
        vida_boss = vida_boss - ataque
        print(f"Felicidad {nombre_jugador}, le haz quitado {ataque} puntos de vida")
        print(f"Para tu infortunio, todavia le queda {vida_boss} puntos de vida")
    if vida_boss == 0:
        print(f"Felicidades {nombre_jugador}, haz derrotado al Gran Boss")
        print("En hora buena")
        bandera = False
        sys.exit ()