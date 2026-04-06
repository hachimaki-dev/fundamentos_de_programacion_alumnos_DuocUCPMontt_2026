hp_p1 = 100
mana_p1 = 20

hp_boss = 150

win_msg = "El jefe ha sido derrotado, ¡Ganaste!"
lose_msg = "Has sido derrotado, ¡Perdiste!"

while True:
    print("1) Atacar")
    print("2) Magia")
    print("3) Poción de vida")

    opcion_elegida = int(input("Ingrese su opción: "))

    match opcion_elegida:
        case 1:
            print("El jefe recibió 20 de daño")
            hp_boss -= 20

            if hp_boss <= 0:
                print(win_msg)
                break
        case 2:
            if mana_p1 - 5 >= 0:
                print("El jefe recibó 50 de daño, pero gastaste 5 de maná")
                hp_boss -= 50
                mana_p1 -= 5

                if hp_boss <= 0:
                    print(win_msg)
                    break
        case 3:
            print("Te curaste 30 de vida")
            hp_p1 += 30
        case _:
            print("Opción inválida")

    print("Recibiste 15 de daño")
    hp_p1 -= 15
    
    if hp_p1 <= 0:
        print(lose_msg)
        break

    print(f"Vida restatnte del jugador: {hp_p1} hp")
    print(f"Vida restante del jefe {hp_boss} hp")