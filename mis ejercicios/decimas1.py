vida = 100
oro = 0
 
Enemigo_1 = {"daño": 20, "vida": 100, "defensa": 0, "oro": 15}
Enemigo_2 = {"daño": 15, "vida": 80,  "defensa": 0, "oro": 10}
Enemigo_3 = {"daño": 10, "vida": 60,  "defensa": 0, "oro": 5}
Jefe_final = {"daño": 30, "vida": 150, "defensa": 30, "oro": 100}
 
jugador = {"daño": 20, "defensa": 0}
 
enemigos_derrotados = 0
jefe_derrotado = False
 
print("===========================================")
print("   Bienvenido al juego de aventuras")
print("===========================================")
 
while vida > 0:
    print("Vida:", vida, "| Oro:", oro)
    print("¿Que quieres hacer?")
    print("1. Explorar")
    print("2. Comer    (+10 vida)")
    print("3. Descansar (+20 vida)")
    print("4. Comprar")
    print("5. Salir")
 
    opcion = input("Elige: ")
 
    if opcion == "1":
        if enemigos_derrotados == 0:
            enemigo = Enemigo_1
            print("¡Encuentras un enemigo! Vida:", enemigo["vida"], "| Daño:", enemigo["daño"])
        elif enemigos_derrotados == 1:
            enemigo = Enemigo_2
            print("¡Encuentras un enemigo! Vida:", enemigo["vida"], "| Daño:", enemigo["daño"])
        elif enemigos_derrotados == 2:
            enemigo = Enemigo_3
            print("¡Encuentras un enemigo! Vida:", enemigo["vida"], "| Daño:", enemigo["daño"])
        elif enemigos_derrotados == 3 and not jefe_derrotado:
            enemigo = Jefe_final
            print("¡¡APARECE EL JEFE FINAL!! Vida:", enemigo["vida"], "| Daño:", enemigo["daño"], "| Defensa:", enemigo["defensa"])
        else:
            print("No quedan enemigos. ¡Eres el campeon!")
            continue
 
        print("1. Pelear")
        print("2. Escapar")
        accion = input("Elige: ")
 
        if accion == "1":
            print("¡Comienza el combate!")
            while enemigo["vida"] > 0 and vida > 0:
                print("  Tu vida:", vida, " | Vida del enemigo:", enemigo["vida"])
                print("  1. Atacar")
                print("  2. Escapar")
                turno = input("  Elige: ")
 
                if turno == "1":
                    enemigo["vida"] = enemigo["vida"] - jugador["daño"] + enemigo["defensa"]
                    print("  ¡Golpeaste al enemigo!")
                    if enemigo["vida"] > 0:
                        vida = vida - (enemigo["daño"] - jugador["defensa"])
                        print("  ¡El enemigo te golpeo!")
                elif turno == "2":
                    print("  ¡Escapaste del combate!")
                    break
                else:
                    print("  Opcion invalida.")
 
            if enemigo["vida"] <= 0:
                oro = oro + enemigo["oro"]
                print("¡Derrotaste al enemigo y ganaste", enemigo["oro"], "de oro!")
                if enemigo == Jefe_final:
                    jefe_derrotado = True
                    print("¡¡FELICIDADES!! ¡Derrotaste al Jefe Final!")
                else:
                    enemigos_derrotados = enemigos_derrotados + 1
 
        elif accion == "2":
            print("Decidiste no pelear y te alejaste.")
        else:
            print("Opcion invalida.")
 
    elif opcion == "2":
        vida = vida + 10
        print("Comes algo y recuperas 10 de vida. Vida actual:", vida)
 
    elif opcion == "3":
        vida = vida + 20
        print("Descansas y recuperas 20 de vida. Vida actual:", vida)
 
    elif opcion == "4":
        print("Tienda — Oro disponible:", oro)
        print("1. Escudo        (-10 daño recibido)  — 20 oro")
        print("2. Espada Larga  (+20 daño)            — 30 oro")
        print("3. Cuchillas     (+10 daño)            — 20 oro")
        print("4. Pocion Magica (+50 vida)            — 40 oro")
        print("5. Salir de la tienda")
        compra = input("Elige: ")
 
        if compra == "1":
            if oro >= 20:
                jugador["defensa"] = jugador["defensa"] + 10
                oro = oro - 20
                print("¡Compraste el escudo! Tu defensa aumento en 10.")
            else:
                print("¡No tienes oro suficiente!")
        elif compra == "2":
            if oro >= 30:
                jugador["daño"] = jugador["daño"] + 20
                oro = oro - 30
                print("¡Compraste la Espada Larga! Tu daño aumento en 20.")
            else:
                print("¡No tienes oro suficiente!")
        elif compra == "3":
            if oro >= 20:
                jugador["daño"] = jugador["daño"] + 10
                oro = oro - 20
                print("¡Compraste las Cuchillas! Tu daño aumento en 10.")
            else:
                print("¡No tienes oro suficiente!")
        elif compra == "4":
            if oro >= 40:
                vida = vida + 50
                oro = oro - 40
                print("¡Bebiste la Pocion Magica! Ganaste 50 de vida. Vida actual:", vida)
            else:
                print("¡No tienes oro suficiente!")
        elif compra == "5":
            print("Saliste de la tienda.")
        else:
            print("Opcion invalida.")
 
    elif opcion == "5":
        print("Saliste del juego.")
        break
 
    else:
        print("Opcion invalida.")
 
if vida <= 0:
    print("Moriste. FIN DEL JUEGO.")
 