# ⏻🕹️ Juego propio Python [+..••] 🎮🕹️👾

print("====================")
print("= Super Smash Bros =")
print("====================")
while True:
    print("\nMenú, seleccione una opcion:")
    print("1. Jugar")
    print("2. Tutorial")
    print("3. Salir")
    menu = input("Seleccione una opcion: ")
    if menu == "1":
        print("\nSelecciona tu personaje:")
        print("1. Mario")
        print("2. Donkey Kong")
        print("3. Link")
        print("4. Samus")
        print("5. Yoshi")
        print("6. Kirby")
        print("7. Fox")
        print("8. Pikachu")
        personaje = input("Elige tu personaje: ")
        print("Tu mision es Vencer a Master Hand")
        print("")
        if personaje == "1":
            nombre = "Mario"
            daño = 12
        elif personaje == "2":
            nombre = "Donkey Kong"
            daño = 18
        elif personaje == "3":
            nombre = "Link"
            daño = 15
        elif personaje == "4":
            nombre = "Samus"
            daño = 14
        elif personaje == "5":
            nombre = "Yoshi"
            daño = 13
        elif personaje == "6":
            nombre = "Kirby"
            daño = 11
        elif personaje == "7":
            nombre = "Fox"
            daño = 16
        elif personaje == "8":
            nombre = "Pikachu"
            daño = 14
        else:
            nombre = "Desconocido"
            daño = 10
        print("\nElegiste a:", nombre)
        vida_jugador = 150
        vida_enemigo = 150
        enemigo = "Master Hand"
        escudos = 3
        print("\n¡La batalla comienza!")
        print("El enemigo es:", enemigo)
        while vida_jugador > 0 and vida_enemigo > 0:
            print("===================")
            print("Vida jugador:", vida_jugador)
            print("Vida enemigo:", vida_enemigo)
            print("Escudos de Master Hand:", escudos)
            print("===================")
            print("1. ATAQUE")
            print("2. DEFENSA")
            print("3. ULTIMATE ATTACK")
            accion = input("Elige una acción: ")
            if accion == "1":
                vida_enemigo -= daño
                print(nombre, "hizo", daño, "de daño")
            elif accion == "2":
                vida_jugador += 5
                print("Te defendiste y recuperaste 5 de vida")
            elif accion == "3":
                if escudos > 0:
                    escudos -= 1
                    print("Master Hand uso un ESCUDO")
                    print("Escudos restantes:", escudos)
                else:
                    vida_enemigo -= (daño + 15)
                    print("ULTIMATE ATTACK hizo", daño + 15, "de daño")
            else:
                print("Opcion invalida")
            if vida_enemigo > 0:
                print("Turno de Master Hand")
                if vida_enemigo <= 60:
                    vida_jugador -= 20
                    print("Master Hand usa ULTIMATE ATTACK")
                else:
                    vida_jugador -= 10
                    print("Master Hand ataca")
        if vida_jugador <= 0:
            print("\nPerdiste la batalla")
        else:
            print("\nGanaste la batalla")
    elif menu == "2":
        print("===== TUTORIAL =====")
        tutorial = [
            "1. Primero debes elegir un personaje.",
            "2. Cada personaje tiene un daño diferente.",
            "3. Tu objetivo es derrotar a Master Hand.",
            "4. En cada turno puedes elegir una accion.",
            "5. ATAQUE hace daño directo.",
            "6. DEFENSA recupera vida.",
            "7. ULTIMATE ATTACK hace mucho daño.",
            "8. Master Hand tiene 3 escudos.",
            "9. Los escudos bloquean tu Ultimate Attack.",
            "10. Cuando se acaben los escudos podrás dañarlo."
        ]
        for paso in tutorial:
            print(paso)
        print("Volviendo al menú...")
    elif menu == "3":
        print("Saliendo del juego...")
        break
    else:
        print("Opcion no valida")