ROJO = "\033[91m"
RESET = "\033[0m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"

print ("⬛⬛⬛⬛💣💣💣💣💣⬛⬛⬛⬛")
print ("⬛ 💣 \033[91m Busca  Minas\033[0m 💣  ⬛")
print ("⬛⬛⬛⬛💣💣💣💣💣⬛⬛⬛⬛\n")


while True :

    print ("/==============/")
    print ("/====/\033[93mMenú\033[0m/====/")
    print ("/==============/\n")

    print ("1. 🔥 \033[92mJUGAR.\033[0m")
    print ("2. ❌  \033[91mSALIR.\033[0m\n")

    decision = int(input("ESCOGA UNA OPCIÓN : "))

    if decision == 1:

        print ("\nBienvenido al busca minas.")
        print ("Vamos a ver las intrucciones.\n")

        opcion = str(input("¿Desea ver las intrucciones de juego? : ")).lower()

        # =========================
        # TABLERO (MISMO PARA AMBOS)
        # =========================
        tablero_jugable = [
            ["💣","1","💣","1","0","0","1","💣","2","💣"],
            ["2","3","💣","💣","💣","💣","0","0","0","2"],
            ["💣","3","💣","1","0","0","1","💣","2","💣"],
            ["0","2","💣","1","0","0","1","💣","2","💣"],
            ["0","1","💣","1","2","💣","2","💣","💣","1"],
            ["0","0","0","0","0","0","1","💣","0","3"],
            ["💣","💣","💣","3","0","0","2","💣","2","💣"],
            ["0","0","0","💣","1","0","0","0","1","0"],
            ["1","3","2","💣","💣","1","0","0","0","1"],
            ["💣","2","0","1","💣","0","0","0","1","💣"]
        ]

        # =========================
        # TABLERO VISIBLE (ARREGLADO)
        # =========================
        tablero_visible = []

        for i in range(10):
            fila = []
            for j in range(10):
                fila.append("⬜")
            tablero_visible.append(fila)

        jugando = True

        while jugando:

            print ("/==============================/")
            print ("/====/ \033[92mTablero disponible\033[0m /====/")
            print ("/==============================/")

            for fila in tablero_visible:
                for casilla in fila:
                    print(casilla, end=" ")
                print()

            f = int(input("\n\033[92mFila (0-9) : \033[0m"))
            c = int(input("\033[92mColumna (0-9): \033[0m"))

            print ("\n\033[92mRevelando casilla...\033[0m\n")

            # 💣 SI PIERDE
            if tablero_jugable[f][c] == "💣":

                print ("💥\033[91mAcabas de explotar\033[0m 💥\n")

                for fila in tablero_jugable:
                    for casilla in fila:
                        print(casilla, end=" ")
                    print()

                print("\033[91mGAME OVER\033[0m☠️\n")
                break

            # ✔ REVELAR (ARREGLADO)
            tablero_visible[f][c] = tablero_jugable[f][c]

            # =========================
            # 🏆 VICTORIA (ARREGLADO)
            # =========================
            victoria = True

            for i in range(10):
                for j in range(10):
                    if tablero_jugable[i][j] != "💣" and tablero_visible[i][j] == "⬜":
                        victoria = False

            if victoria:
                print("\n🎉 ¡GANASTE!\n")
                jugando = False

    else:
        print ("\033[92mCERRANDO JUEGO...\033[0m")
        break