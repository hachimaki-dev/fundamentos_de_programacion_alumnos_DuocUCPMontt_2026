import random

# VIDA Y MANA INICIAL
vida_mimikyu = 100
mana_mimikyu = 50

vida_rattata = 60
mana_rattata = 40

vida_ditto = 90
mana_ditto = 60

vida_charizard = 120
mana_charizard = 60

turno = 1

# BATALLA
while vida_charizard > 0 and (vida_mimikyu > 0 or vida_rattata > 0 or vida_ditto > 0):

    print("====================")
    print("TURNO", turno)
    print("====================")

    # MOSTRAR ESTADO
    print("\n---EQUIPO X---")
    print("1. Mimikyu -> Vida:", vida_mimikyu, "Mana:", mana_mimikyu)
    print("2. Rattata -> Vida:", vida_rattata, "Mana:", mana_rattata)
    print("3. Ditto -> Vida:", vida_ditto, "Mana:", mana_ditto)

    print("\n---EQUIPO ROJO---")
    print("Charizard -> Vida:", vida_charizard, "Mana:", mana_charizard)

    # ELEGIR POKÉMON
    eleccion = input("\n1-Mimikyu / 2-Rattata / 3-Ditto: ")

    # MIMIKYU
    if eleccion == "1" and vida_mimikyu > 0:

        print("\nTurno de Mimikyu")
        print("1. Carantoña (15 daño)")
        print("2. Garra Umbría (25 daño, 10 mana)")
        print("3. Sombra Vil (30 daño, 15 mana)")

        accion = input("Acción: ")

        if accion == "1":
            vida_charizard -= 15
            print("Mimikyu usó Carantoña")

        elif accion == "2" and mana_mimikyu >= 10:
            vida_charizard -= 25
            mana_mimikyu -= 10
            print("Mimikyu usó Garra Umbría")

        elif accion == "3" and mana_mimikyu >= 15:
            vida_charizard -= 30
            mana_mimikyu -= 15
            print("Mimikyu usó Sombra Vil")

        else:
            print("Acción inválida o sin mana")

    # RATTATA
    elif eleccion == "2" and vida_rattata > 0:

        print("\nTurno de Rattata")
        print("1. Placaje (10 daño)")
        print("2. Mordisco (20 daño, 10 mana)")
        print("3. Curarse (15 vida, 5 mana)")

        accion = input("Acción: ")

        if accion == "1":
            vida_charizard -= 10
            print("Rattata usa Placaje")

        elif accion == "2" and mana_rattata >= 10:
            vida_charizard -= 20
            mana_rattata -= 10
            print("Rattata usa Mordisco")

        elif accion == "3" and mana_rattata >= 5:
            vida_rattata += 15
            mana_rattata -= 5
            print("Rattata se cura")

        else:
            print("Acción inválida o sin mana")

    # DITTO
    elif eleccion == "3" and vida_ditto > 0:

        print("\nTurno de Ditto")
        print("1. Golpe (12 daño)")
        print("2. Transformación (22 daño, 10 mana)")
        print("3. Curarse (18 vida, 5 mana)")

        accion = input("Acción: ")

        if accion == "1":
            vida_charizard -= 12
            print("Ditto usa Golpe")

        elif accion == "2" and mana_ditto >= 10:
            vida_charizard -= 22
            mana_ditto -= 10
            print("Ditto usa Transformación")

        elif accion == "3" and mana_ditto >= 5:
            vida_ditto += 18
            mana_ditto -= 5
            print("Ditto se cura")

        else:
            print("Acción inválida o sin mana")

    else:
        print("Pokémon inválido o debilitado")

    # VER SI GANA JUGADOR
    if vida_charizard <= 0:
        print("\nGANA EL EQUIPO X")
        break

    # TURNO CHARIZARD (CPU)
    print("\nTurno de Charizard")

    accion_cpu = random.randint(1, 3)

    if accion_cpu == 1:
        daño = 20
        print("Charizard usa Lanzallamas")

    elif accion_cpu == 2 and mana_charizard >= 10:
        daño = 30
        mana_charizard -= 10
        print("Charizard usa Garra Dragón")

    else:
        daño = 15
        print("Charizard usa ataque básico")

    # Elegir objetivo
    objetivo = random.randint(1, 3)

    if objetivo == 1 and vida_mimikyu > 0:
        vida_mimikyu -= daño
        print("Mimikyu recibe", daño)

    elif objetivo == 2 and vida_rattata > 0:
        vida_rattata -= daño
        print("Rattata recibe", daño)

    elif objetivo == 3 and vida_ditto > 0:
        vida_ditto -= daño
        print("Ditto recibe", daño)

    # VER SI GANA CPU
    if vida_mimikyu <= 0 and vida_rattata <= 0 and vida_ditto <= 0:
        print("\n¡Equipo Rojo gana!")
        break

    turno += 1

# RESULTADO FINAL
print("\n===== RESULTADO FINAL =====")

print("\nEquipo X:")
print("Mimikyu -> Vida:", vida_mimikyu)
print("Rattata -> Vida:", vida_rattata)
print("Ditto -> Vida:", vida_ditto)

print("\nEquipo Rojo:")
print("Charizard -> Vida:", vida_charizard)