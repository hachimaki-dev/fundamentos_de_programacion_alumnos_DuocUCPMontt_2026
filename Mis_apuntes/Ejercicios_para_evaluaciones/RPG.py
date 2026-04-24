hp = 100
mana = 20
bosshp = 150
turnos = 1
print("====|||HAZ ENTRADO EN COMBATE|||====")
while hp > 0 and bosshp > 0:
    atk = 1
    Magia = 2
    Pocion_de_vida = 3
    accion = int(input("Rápido escoge tu acción!! \n 1. Atacar \n 2. Magia \n 3. Poción de Vida. "))
    if accion == 1:
        bosshp -= 20
        turnos += 1
        print(f"Haz hecho un ataque eficaz, los puntos de vida del jefe descendieron a {bosshp}.")
        if bosshp == 0:
            print(f"Felicidades derrotaste al jefe, te ganaste un Chocman!")
            break
        else:
             hp -= 15
             print(f"El jefe no se ha quedado parado y te atacó también dejandote a {hp} de vida, procura matarlo rápido!")

    elif accion ==2:
        if mana > 0:
            bosshp -= 50
            turnos +=1
            mana -= 5
            print(f"Le lanzas un hechizo potente al jefe dejandolo en {bosshp} puntos de vida. Te quedan {mana} puntos de maná.")
            if bosshp == 0:
                print(f"Felicidades derrotaste al jefe, te ganaste un Chocman!")
                break
            else:
                hp -= 15
                print(f"El jefe no se ha quedado parado y te atacó también dejandote a {hp} de vida, procura matarlo rápido!")
        else:
            print("Te haz quedado sin maná! Realiza otra acción.")
            continue
    elif accion == 3:
        turnos += 1
        hp += 30
        mana -= mana
        print(f"Te haz curado! Tus puntos vitales subieron hasta {hp}. \n Pero tu maná se ha agotado : {mana}.")
    else:
        print("Escoge una acción válida.")
        continue
print(f"Haz realizado {turnos} turnos para derrotar al jefe.")