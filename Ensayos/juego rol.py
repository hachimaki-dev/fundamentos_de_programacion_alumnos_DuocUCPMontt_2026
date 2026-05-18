vida_jugador=100
vida_jefe=150
mana_jugador=20

print("¡comienza la batalla!")

while vida_jugador>0 and vida_jefe>0:
    print(f"vida del jugador:{vida_jugador},mana del jugador:{mana_jugador}")
    print(f"vida del jefe:{vida_jefe}")

    print("elije una accion:")
    print("1.atacar")
    print("2.magia")
    print("3.curacion")

    accion=int(input("realizar una accion"))
    if accion == 1 :
        vida_jefe=vida_jefe-20
        print(f"¡has atacado al jefe!,vida del jefe:{vida_jefe}")
    elif accion ==2:
        if mana_jugador>=5:
            mana_jugador=mana_jugador-5
            vida_jefe=vida_jefe-50
            print(f"haz lanzado un hechizo al jefe,vida del jefe:{vida_jefe},mana del jugador:{mana_jugador}")
        else:
            print("no tiene suficiente mana para lanzar hechizo,pierde turno")
    elif accion == 3:
        vida_jugador=vida_jugador + 30
        mana_jugador=0
        print(f"¡haz utilizado una pocion de curacion,vida del jugador:{vida_jugador},mana del jugador:{mana_jugador}")
    else:
        print("accion no valida,perder turno")

        if vida_jefe>0:
            vida_jugador=vida_jugador-15
            print(f"¡el jefe ha atacado al jugador,vida del jugador:{vida_jugador}")

        if vida_jugador<=0:
            print("¡haz sido vencido por el jefe")
        else:
            print("felicitacion haz derrotado al jefe")
            