# Programa de cachipun contra un bot usando el módulo random.
# El programa comprueba si el usuario ingresa un número válido y no le permitirá continuar si su número es inválido.
# No hay comprobación de errores en caso de que el usuario ingrese algo que no es un número.

import random

bandera = True
victorias_jugador = 0
victorias_bot = 0

def numeroRandomBot():    # Función que crea un número al azar entre 1 y 3 (un número menos que el segundo argumento de random.randrange)
    return(random.randrange(1,4))

while bandera:    # Loop principal del juego
    eleccion_jugador = int(input("\nJugador elige:    1. Piedra    2. Papel    3. Tijeras        "))
    
    if eleccion_jugador < 1 or eleccion_jugador > 3:    # Comprobación de número válido
        print("Elección inválida!")
        continue
    else:
        pass

    eleccion_bot = numeroRandomBot()

    if eleccion_bot == 1:    # Se muestra al jugador la elección del bot
        print(f"El bot elige:    1. Piedra")
    elif eleccion_bot == 2:
        print(f"El bot elige:    2. Papel")
    else:
        print(f"El bot elige:    3. Tijeras")

    # Comprobación de quién gana

    if eleccion_jugador == eleccion_bot:    # Si el jugador y el bot eligen el mismo número (empate)
        print("\n¡Empate!")

    elif eleccion_jugador == 1:    # Si el jugador elige Piedra
        if eleccion_bot == 3:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el jugador!")
            victorias_jugador = victorias_jugador + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")
        else:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el bot!")
            victorias_bot = victorias_bot + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")
    
    elif eleccion_jugador == 2:    # Si el jugador elige Papel
        if eleccion_bot == 1:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el jugador!")
            victorias_jugador = victorias_jugador + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")
        else:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el bot!")
            victorias_bot = victorias_bot + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")

    elif eleccion_jugador == 3:    # Si el jugador elige Tijeras
        if eleccion_bot == 2:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el jugador!")
            victorias_jugador = victorias_jugador + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")
        else:
            print("\n/////////////////////////////////////////////////////////////////")
            print("¡Gana el bot!")
            victorias_bot = victorias_bot + 1
            print(f"Victorias jugador: {victorias_jugador}        Victorias bot: {victorias_bot}")
            print("/////////////////////////////////////////////////////////////////\n")

    # Comprobación de cantidad de victorias

    if victorias_jugador == 3:
        print("\n============================")
        print("¡Victoria para el jugador!")
        print("============================")
        bandera = False
    elif victorias_bot == 3:
        print("\n============================")
        print("¡Victoria para el bot!")
        print("============================")
        bandera = False
    else:
        print("¡Siguiente ronda!")
