import random

vic_user = 0
vic_maquina = 0

eleccion_maquina = ""

opciones = ["piedra", "papel", "tijera"]

print("Vamos a jugar al cachipun al primero con 3 victorias\n")

while (vic_user < 3 and vic_maquina < 3):
    eleccion_user = ""
    while eleccion_user.lower() not in opciones:
        eleccion_user = input("Ingrese su opcion: ")

    eleccion_maquina = random.choice(opciones)
    print(f"Opción de la máquina: {eleccion_maquina.capitalize()}\n")

    print(f"----- {eleccion_user.capitalize()} vs {eleccion_maquina.capitalize()} -----")

    match(eleccion_user.lower()):
        case "piedra":
            if eleccion_maquina == "piedra":
                print("¡Empate!, No hay puntos para ninguno")
            elif eleccion_maquina == "papel":
                print("¡Perdiste humano!, Punto para la máquina")
                vic_maquina += 1
            else:
                print("¡Ganaste humano!, Punto para ti")
                vic_user += 1
        case "papel":
            if eleccion_maquina == "papel":
                print("¡Empate!, No hay puntos para ninguno")
            elif eleccion_maquina == "tijera":
                print("¡Perdiste humano!, Punto para la máquina")
                vic_maquina += 1
            else:
                print("¡Ganaste humano!, Punto para ti")
                vic_user += 1
        case "tijera":
            if eleccion_maquina == "tijera":
                print("¡Empate!, No hay puntos para ninguno")
            elif eleccion_maquina == "piedra":
                print("¡Perdiste humano!, Punto para la máquina")
                vic_maquina += 1
            else:
                print("¡Ganaste humano!, Punto para ti")
                vic_user += 1
        case _:
            print("Algo pasó, ni idea")
    
    print(f"Puntos humano: {vic_user}\nPuntos máquina: {vic_maquina}\n")

if vic_user > vic_maquina:
    print("Felicidades humano, ¡Ganaste!")
else:
    print("Ganó la máquina, buuu")