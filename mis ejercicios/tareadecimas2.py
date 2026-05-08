vida = 100
oro = 0

jugador = {
    "daño": 20,
    "defensa": 0
}

enemigo = {
    "daño": 15,
    "vida": 50
}

print("Bienvenido al juego")
print("Tienes", vida, "de vida y", oro, "de oro")

while vida > 0:
    print("\n¿Que quieres hacer?")
    print("1. Explorar")
    print("2. Comer")
    print("3. Descansar")
    print("4. Comprar")
    print("5. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        print("¡Encuentras un enemigo!")
        print("1. Pelear")
        print("2. Escapar")
        accion = input("Elige: ")
        if accion == "1":
            enemigo["vida"] = 50
            print("¡Comienza el combate!")
            while enemigo["vida"] > 0 and vida > 0:
                print("Tu vida:", vida, "| Vida enemigo:", enemigo["vida"])
                print("1. Atacar")
                print("2. Escapar")
                turno = input("Elige: ")
                if turno == "1":
                    enemigo["vida"] = enemigo["vida"] - jugador["daño"]
                    print("¡Golpeaste al enemigo!")
                    if enemigo["vida"] > 0:
                        vida = vida - (enemigo["daño"] - jugador["defensa"])
                        print("¡El enemigo te golpeó!")
                elif turno == "2":
                    print("¡Escapas pero pierdes 20 de vida!")
                    vida = vida - 20
                    break
            if enemigo["vida"] <= 0:
                print("¡Venciste! Ganas 15 de oro")
                oro = oro + 15
        else:
            print("Escapas sin daño")

    elif opcion == "2":
        print("\n¿Que quieres comer?")
        print("1. Pan (5 oro) - recupera 15 de vida")
        print("2. Manzana (8 oro) - recupera 25 de vida")
        print("3. Sopa (12 oro) - recupera 40 de vida")
        print("4. Salir")
        comida = input("Elige: ")
        if comida == "1":
            if oro >= 5:
                vida = vida + 15
                oro = oro - 5
                print("Comiste pan y recuperaste 15 de vida")
            else:
                print("No tienes suficiente oro")
        elif comida == "2":
            if oro >= 8:
                vida = vida + 25
                oro = oro - 8
                print("Comiste una manzana y recuperaste 25 de vida")
            else:
                print("No tienes suficiente oro")
        elif comida == "3":
            if oro >= 12:
                vida = vida + 40
                oro = oro - 12
                print("Comiste sopa y recuperaste 40 de vida")
            else:
                print("No tienes suficiente oro")
        elif comida == "4":
            print("Saliste sin comer")

    elif opcion == "3":
        print("Descansas y recuperas 20 de vida")
        vida = vida + 20

    elif opcion == "4":
        print("\n¿Que deseas comprar?")
        print("1. Escudo (20 oro) - reduce daño en 10")
        print("2. Espada (30 oro) - aumenta daño en 20")
        print("3. Pocion (15 oro) - recupera 50 de vida")
        print("4. Salir")
        compra = input("Elige: ")
        if compra == "1":
            if oro >= 20:
                jugador["defensa"] = jugador["defensa"] + 10
                oro = oro - 20
                print("¡Compraste el escudo!")
            else:
                print("No tienes suficiente oro")
        elif compra == "2":
            if oro >= 30:
                jugador["daño"] = jugador["daño"] + 20
                oro = oro - 30
                print("¡Compraste la espada!")
            else:
                print("No tienes suficiente oro")
        elif compra == "3":
            if oro >= 15:
                vida = vida + 50
                oro = oro - 15
                print("¡Compraste una pocion! +50 vida")
            else:
                print("No tienes suficiente oro")
        elif compra == "4":
            print("Saliste de la tienda")

    elif opcion == "5":
        print("Saliste del juego")
        break
    else:
        print("Opcion invalida")

    print("\nVida:", vida, "| Oro:", oro, "| Daño:", jugador["daño"], "| Defensa:", jugador["defensa"])

if vida <= 0:
    print("¡Moriste! Fin del juego")