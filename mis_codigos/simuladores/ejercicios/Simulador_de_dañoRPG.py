
jefe_vida = 1000
while jefe_vida > 0:
    daño = int(input("ingresa el daño: "))
    if daño < 0:
        print("El ataque fallo")
    else:   
        jefe_vida = jefe_vida - daño
        print("menos", jefe_vida)

        if jefe_vida > 0:
            print("vida restante", jefe_vida)
        else:
            print("vida restante del jefe")
            print("¡Jefe derrotado!")