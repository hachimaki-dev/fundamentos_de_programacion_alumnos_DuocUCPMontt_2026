# Programa de cachipun simple en Python
# El programa asume que el usuario elige un número válido, no hay comprobación de errores

bandera = True
victorias_usuario1 = 0
victorias_usuario2 = 0

while bandera:    # Loop principal del juego
    eleccion_usuario1 = int(input("\nJugador 1 elige:    1. Piedra    2. Papel    3. Tijeras        "))
    eleccion_usuario2 = int(input("Jugador 2 elige:    1. Piedra    2. Papel    3. Tijeras        "))

    if eleccion_usuario1 == eleccion_usuario2:    # Si ambos jugadores escogen el mismo número (empate)
        print("¡Empate!")

    # Comprobación de quién gana

    elif eleccion_usuario1 == 1:    # Si el jugador 1 elige Piedra
        if eleccion_usuario2 == 3:
            print("\n¡Gana jugador 1!")
            victorias_usuario1 = victorias_usuario1 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")
        else:
            print("\n¡Gana jugador 2!")
            victorias_usuario2 = victorias_usuario2 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")
    
    elif eleccion_usuario1 == 2:    # Si el jugador 1 elige Papel
        if eleccion_usuario2 == 1:
            print("\n¡Gana jugador 1!")
            victorias_usuario1 = victorias_usuario1 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")
        else:
            print("\n¡Gana jugador 2!")
            victorias_usuario2 = victorias_usuario2 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")

    elif eleccion_usuario1 == 3:    # Si el jugador 1 elige Tijeras
        if eleccion_usuario2 == 2:
            print("\n¡Gana jugador 1!")
            victorias_usuario1 = victorias_usuario1 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")
        else:
            print("\n¡Gana jugador 2!")
            victorias_usuario2 = victorias_usuario2 + 1
            print(f"Victorias jugador 1: {victorias_usuario1}        Victorias jugador 2: {victorias_usuario2}")

    # Comprobación de cantidad de victorias

    if victorias_usuario1 == 3:
        print("\n============================")
        print("¡Victoria para el jugador 1!")
        print("============================")
        bandera = False
    elif victorias_usuario2 == 3:
        print("\n============================")
        print("¡Victoria para el jugador 2!")
        print("============================")
        bandera = False
    else:
        print("¡Siguiente ronda!")
