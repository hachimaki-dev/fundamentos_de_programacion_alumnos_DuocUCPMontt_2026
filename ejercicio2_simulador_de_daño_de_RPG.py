vida_jefe = 1000

while vida_jefe > 0 :
    daño = int(input("Ingresa el daño de tu ataque: "))

    if daño < 0:
        print("El ataque falló")
    else:
        vida_jefe -= daño
        if vida_jefe > 0:
            print(f"La vida restante del jefe es: {vida_jefe}")
        else:
            print("¡Jefe derrotado!")