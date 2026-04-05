Vida_Jefe = 1000
daño_usuario = 0

while Vida_Jefe > 0:
    daño_usuario = int(input("Daño de Ataque"))
    if daño_usuario < 0:
        print("El ataque falló")
    else:
        daño_usuario >= 0
        Vida_Jefe -= daño_usuario
        print(f"El jefe tiene {Vida_Jefe} de vida restante")


print("Jefe derrotado")