print("=== ⚔️ 👺 === Batalla RPG === ⚔️ 👺 ===")

vida_jugador = 100
mana = 20
vida_jefe = 150

while vida_jugador > 0 and vida_jefe > 0:

    print("\nVida Jugador:", vida_jugador)
    print("Maná:", mana)
    print("Vida Jefe:", vida_jefe)

    print("\n1) Atacar")
    print("2) Magia")
    print("3) Poción de Vida")

    opcion = int(input("Elige una acción: "))

    if opcion == 1:
        vida_jefe = vida_jefe - 20
        print("Atacaste al jefe por 20 de daño")

    elif opcion == 2:
        if mana >= 5:
            mana = mana - 5
            vida_jefe = vida_jefe - 50
            print("Usaste magia y causaste 50 de daño")
        else:
            print("No tienes suficiente maná")

    elif opcion == 3:
        vida_jugador = vida_jugador + 30
        mana = 0
        print("Usaste una poción y recuperaste 30 de vida")

    else:
        print("Acción inválida")

    if vida_jefe > 0:
        vida_jugador = vida_jugador - 15
        print("El jefe te ataca y te quita 15 de vida")

if vida_jugador > 0:
    print("=== 🏆 ¡Ganaste la batalla! ===")
else:
    print("=== 💀 El jefe te derrotó ===")