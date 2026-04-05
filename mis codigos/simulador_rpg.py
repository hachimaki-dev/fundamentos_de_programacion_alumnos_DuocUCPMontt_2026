vida_jefe = 1000

while vida_jefe > 0:
    daño = int(input("¿Cuanto daño de ataque haras?: "))

    if daño < 0:
        print(f"El ataque fallo, la vida restante del jefe es de {vida_jefe}")

    else:
        vida_jefe -= daño
        print(f"Ataque efectivo, has hecho {daño} de daño, la vida restante del jefe es de {vida_jefe}!!!")

    if vida_jefe <= 0:
        print("¡Jefe derrotado!")
        break