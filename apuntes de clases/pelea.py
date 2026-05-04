vida_jefe = 200
vida_jugador = 75
mana_jugador = 25
pocion = 1

print("Estas preparado para la que viene?")

while True:
    opcion = input("¿Desea comenzar esta batalla?: (si/no): ")
    if opcion == "si":
        print("LA BATALLA COMIENZA!")
        break
    elif opcion == "no":
        print("jajaja, pendejo Bye.")
        exit()
    else:
        print("opción no valida")
print("Actualmente cuentas con 25 de mana y 1 botellas de vidas")
while vida_jefe >= 0 and vida_jugador >=0:
    print("Elige una opción [1] Atacar con tu espada, [2] Usar un hechizo, [3] Usar poción de vida:  ")
    
    opcion = input("selección\n:")

    if opcion == "1":
        print("Usaste un ataque muy letal con tu espada -20HP.\n")
        vida_jefe -= 20

    elif opcion == "2":
        if mana_jugador >= 5:
            print("Lanzas un poderoso hechizo -50HP.\n")
            vida_jefe -= 50
            mana_jugador -= 5
        else:
            print("no tienes suficiente mana, pierdes tu turno\n")

    elif opcion == "3":
        print("bebes una poción de vida +30HP")
        print("acabas de quedarte sin mana")
        vida_jugador += 30
        mana_jugador = 0
        pocion -= 1
        

    else:
        print("opción no valida, perdiste tu turno")
    if vida_jefe >= 0:
        print("El jefe ataca sin piedad -15HP")
    vida_jugador -=15

print("LA BATALLA ACABA DE CONCLUIR")
if vida_jugador > 0:
    print("Felicidades, lograste erradicar a la gran amaneza, VICTORIA!")
else:
    print("Lamentablemente caiste ante tu oponente")
