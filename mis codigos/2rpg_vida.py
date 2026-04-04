print("=== Derrota al Jefe ===")

vida_jefe = 1000

print("=== COMBATE RPG ===")
print("El jefe tiene", vida_jefe, "puntos de vida")

while vida_jefe > 0:

    dano = int(input("Ingresa el daño del ataque: "))

    if dano <= 0:
        print("El ataque falló")

    else:
        vida_jefe = vida_jefe - dano

        if vida_jefe > 0:
            print("Vida restante del jefe:", vida_jefe)
        else:
            print("¡Jefe derrotado!")