boss = 1000
print("Un enemigo fuerte ha aparecido, debes bajar su vida de 1000 puntos a 0 para ganar")
while True:
    if boss >= 1000:
        boss = 1000
    daño = int(input("Escribe el daño que quieres hacer: "))
    if daño <= 0:
        print(f"El ataque ha fallado, no has hecho daño, la vida del jefe es de: {boss}")
    elif daño >= 1:
        boss = boss - daño
        if boss < 0:
            boss = 0
        print(f"Has hecho daño al jefe, la vida del jefe ahora es de: {boss}")
        if boss == 0:
            print("¡Jefe derrotado!, has ganado :D")
            break