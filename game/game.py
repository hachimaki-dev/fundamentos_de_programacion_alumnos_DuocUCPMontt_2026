print ("/=======================/")
print ("/=====/Tres en Raya/=====/")
print ("/=======================/\n")

while True:

    print ("================")
    print ("======Menú======")
    print ("================\n")

    print ("1.  - Jugar  -  ")
    print ("2.  - Salir  -  ")

    desicion = int(input("\nEscoga una opción : "))

    if desicion == 1:

        print("\nBienvenido al Tres en Raya.")
        print ("Ahora vamos a repasar las instrucciones.\n")

        opcion = str(input("¿Desea repasar las instrucciones? : ")).lower()

        if opcion == "si":
            print ("/\n====================/")
            print ("/===/INSTRUCCIONES/===/")
            print ("/====================/\n")

            print ("1. - Ganas con tres en raya.") 
            print ("2. - Turnos entre jugadores.") 
            print ("3. - Ingresa fila y columna (0-2)\n")
            

        tablero_real = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        turno = 0
        jugador = "X"
        juego = True

        while juego:

            print ("\nTABLERO:\n")

            for i in range (3):
                for j in range (3):
                    print(tablero_real[i][j], end="")
                    if j < 2 :
                        print (" | ", end="")
                print ()
                if i < 2:
                    print ("--+---+--")

            print ("\nTurno del jugador", jugador)

            fila = int(input("Fila (0-2): "))
            columna = int(input("Columna (0-2): "))

            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print ("Selección inválida.\n")
                continue

            if tablero_real[fila][columna] != " ":
                print ("Casilla ocupada.\n")
                continue

            tablero_real[fila][columna] = jugador
            turno += 1

            ganador = False

            # FILAS
            for i in range(3):
                if tablero_real[i][0] == jugador and tablero_real[i][1] == jugador and tablero_real[i][2] == jugador:
                    ganador = True

            for j in range(3):
                if tablero_real[0][j] == jugador and tablero_real[1][j] == jugador and tablero_real[2][j] == jugador:
                    ganador = True

            if tablero_real[0][0] == jugador and tablero_real[1][1] == jugador and tablero_real[2][2] == jugador:
                ganador = True

            if tablero_real[0][2] == jugador and tablero_real[1][1] == jugador and tablero_real[2][0] == jugador:
                ganador = True

            if ganador:
                print("\n¡Ganó el jugador", jugador, "!")
                juego = False

            elif turno == 9:
                print("\nEmpate!")
                juego = False

            else:
                if jugador == "X":
                    jugador = "O"
                else:
                    jugador = "X"
    elif desicion == 2:
        print("Saliendo del juego...")
        break
    else:
        print("Ingrese una opción válida")