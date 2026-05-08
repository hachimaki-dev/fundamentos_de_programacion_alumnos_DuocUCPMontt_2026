vida = 100
oro = 0
Jefe_final = 150
Enemigo_1 = 50
Enemigo_2 = 50
Enemigo_3 = 30

Enemigo_1 ={
    "daño": 20,
    "vida": 100,
    "defensa": 0
}
Enemigo_2 ={
    "daño": 15,
    "vida": 100,
    "defensa": 0
}
Enemigo_3 ={
    "daño": 15,
    "vida": 100,
    "defensa": 0
}
Jefe_final ={
    "daño":30,
    "defensa":30
}
jugador ={
    "daño": 20,
    "defensa": 0
}

print("Bienvenido al juego")

while vida > 0:
    print ("tienes", vida, "de vida y", oro,"de oro")
    
    print("¿Que quieres hacer?")
    print("1. Explorar")
    print("2. Comer")
    print("3. Descansar")
    print("4. Comprar")
    print("5. Salir")
    
    opcion = input("Elige: ")
    if opcion == "1":
        print("¡Encuentras un enemigo!")
        print("¿Que quieres hacer?")
        print("1. Pelear")
        print("2. Escapar")
        accion = input("Elige:  ")
        if accion == "1":
            print("¡Comienza el combate!")
            while Enemigo_1["vida"] > 0 and vida > 0:
                 print("Tu vida:", vida)
                 print("Vida del enemigo:", Enemigo_1["vida"])
                 print("1. Atacar")
                 print("2. Escapar")
                 turno = input("Elige: ")
                 if turno == "1":
                    Enemigo_1["vida"] = Enemigo_1["vida"] - jugador["daño"]
                    print("Golpeaste al enemigo!")
                    if Enemigo_1["vida"] > 0:
                       vida = vida - (Enemigo_1["daño"] - jugador["defensa"])
                    print("El enemigo te golpeó!")
                
    elif opcion == "2":
        print("Comes y recuperas 10 de vida")
        vida = vida + 10
    elif opcion == "3":
        print("Descansas y recuperas 20 de vida")
        vida = vida + 10
    elif opcion == "4":
        print("¿Que deseas comprar?")
        print("1.Escudo -10 de daño ")
        print("2.Espada Larga + 20 de daño")
        print("3.Cuchillas + 10 de daño")
        print("4.Posion Magica misteriosa ????") 
        print("5.Salir")
        compra = input("Elige: ")
        if compra == "1": 
            if oro >= 20:
                print("¡Compraste el escudo!")
                print("Obtienes un escudo que reduce en 10 el daño de enemigos")
                jugador["defensa"] = jugador["defensa"] + 10
                oro = oro - 20
            else:
                print("¡¡¡No tienes oro suficiente!!!!")
        if compra == "2":
            if oro >= 30:
                print("¡compraste una espada larga!")
                print("Obtuviste una espada larga y obtienes 20 mas de daño a enemigos")
                jugador["daño"] = jugador["daño"] + 20
                oro = oro - 30
            else:
                print("¡¡¡No tienes oro suficiente!!!")
        if compra == "3":
            if oro >= 20:
                print("¡¡¡Compraste cuchillas!!!")
                print("Obtienes cuchillas y obtienes 10 mas de daño a enemigos")
                jugador["daño"] = jugador["daño"] + 10
            else:
                print("¡¡¡No tienes oro suficiente!!!")
        if compra == "4":
            if oro >= 40:
                print("¡¡¡Compraste una pocion magica misteriosa!!!")
                print("¡Obtienes una pocion magica y ganas 50 de vida!")
                jugador["vida"] = jugador["vida"] + 50
        else:
            print("¡¡¡No tienes oro suficiente!!!")
    elif opcion == "5":
        print("Saliste del juego")
        break
    else: 
        print("opcion invalida")
if vida <= 0:
    print("Moriste, FIN DEL JUEGO")
    