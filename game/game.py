tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turno = "X"
ganador = ""
jugando = True

print("========================================")
print("          JUEGO DEL GATO               ")
print("========================================")
print()
print("Posiciones:")
print(" 1 | 2 | 3")
print("---+---+---")
print(" 4 | 5 | 6")
print("---+---+---")
print(" 7 | 8 | 9")
print()

while jugando:

    print()
    print(" " + tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("---+---+---")
    print(" " + tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("---+---+---")
    print(" " + tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print()

    print("Turno del jugador:", turno)
    posicion = input("Elige una posicion (1-9): ")

    if posicion != "1" and posicion != "2" and posicion != "3" and posicion != "4" and posicion != "5" and posicion != "6" and posicion != "7" and posicion != "8" and posicion != "9":
        print("Posicion invalida.")
        continue

    numero = int(posicion) - 1

    if tablero[numero] != " ":
        print("Esa casilla ya esta ocupada.")
        continue

    tablero[numero] = turno

    if tablero[0] == tablero[1] == tablero[2] and tablero[0] != " ":
        ganador = tablero[0]
    elif tablero[3] == tablero[4] == tablero[5] and tablero[3] != " ":
        ganador = tablero[3]
    elif tablero[6] == tablero[7] == tablero[8] and tablero[6] != " ":
        ganador = tablero[6]
    elif tablero[0] == tablero[3] == tablero[6] and tablero[0] != " ":
        ganador = tablero[0]
    elif tablero[1] == tablero[4] == tablero[7] and tablero[1] != " ":
        ganador = tablero[1]
    elif tablero[2] == tablero[5] == tablero[8] and tablero[2] != " ":
        ganador = tablero[2]
    elif tablero[0] == tablero[4] == tablero[8] and tablero[0] != " ":
        ganador = tablero[0]
    elif tablero[2] == tablero[4] == tablero[6] and tablero[2] != " ":
        ganador = tablero[2]

    if ganador != "":
        print()
        print(" " + tablero[0] + " | " + tablero[1] + " | " + tablero[2])
        print("---+---+---")
        print(" " + tablero[3] + " | " + tablero[4] + " | " + tablero[5])
        print("---+---+---")
        print(" " + tablero[6] + " | " + tablero[7] + " | " + tablero[8])
        print()
        print("========================================")
        print("GANO EL JUGADOR:", ganador)
        print("========================================")
        jugando = False

    elif tablero[0] != " " and tablero[1] != " " and tablero[2] != " " and tablero[3] != " " and tablero[4] != " " and tablero[5] != " " and tablero[6] != " " and tablero[7] != " " and tablero[8] != " ":
        print()
        print(" " + tablero[0] + " | " + tablero[1] + " | " + tablero[2])
        print("---+---+---")
        print(" " + tablero[3] + " | " + tablero[4] + " | " + tablero[5])
        print("---+---+---")
        print(" " + tablero[6] + " | " + tablero[7] + " | " + tablero[8])
        print()
        print("========================================")
        print("EMPATE! Nadie gano.")
        print("========================================")
        jugando = False

    else:
        if turno == "X":
            turno = "O"
        else:
            turno = "X"