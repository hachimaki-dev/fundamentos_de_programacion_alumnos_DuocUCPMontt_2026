#Irina Sovenko, Blanca Troncoso, Kevin Cueto
import random

print("\n=== BIENVENIDO AL JUEGO --- LEAGUE OF THREE RPG ===\n")

while True:
    heroe = int(input("Elige tu héroe:\n1. Espadachín\n2. Arquero\n3. Mago\nOpción: "))

    if heroe == 1 or heroe == 2 or heroe == 3:
        break
    else:
        print("Elige 1, 2 o 3.\n")

if heroe == 1:
    nombre_heroe = "Espadachín"
    vida_jugador = 120
elif heroe == 2:
    nombre_heroe = "Arquero"
    vida_jugador = 100
else:
    nombre_heroe = "Mago"
    vida_jugador = 80

vida_jefe = 100
jefe = "Dragón Oscuro"

berserker = False
wind_walker = False
arcane_shield = False
congelado = False

exp = 0
job = 0
carta = ""

for turno in range(1, 11):

    if vida_jugador <= 0 or vida_jefe <= 0:
        break

    print("\n------------------")
    print("Turno:", turno)
    print("Héroe:", nombre_heroe)
    print("Tu vida:", vida_jugador)
    print("Vida del jefe:", vida_jefe)

    if heroe == 1:
        print("1. Ataque básico")
        print("2. Magnum Break")
        print("3. Berserker")
    elif heroe == 2:
        print("1. Ataque básico")
        print("2. Falcon Assault")
        print("3. Wind Walker")
    else:
        print("1. Meteor Storm")
        print("2. Frost Ruin")
        print("3. Arcane Shield")

    while True:
        accion = int(input("Elige una acción: "))

        if accion == 1 or accion == 2 or accion == 3:
            break
        else:
            print("Elige 1, 2 o 3.")

    daño = 0

    if heroe == 1:

        if accion == 1:
            if berserker:
                daño = 40
                print("Berserker potenció tu ataque")
                berserker = False
            else:
                critico = random.randint(1, 5)
                if critico == 1:
                    daño = 30
                    print("¡Crítico!")
                else:
                    daño = 15

        elif accion == 2:
            if berserker:
                daño = 50
                print("Magnum Break potenciado")
                berserker = False
            else:
                daño = 25

        elif accion == 3:
            prob = random.randint(1, 2)
            if prob == 1:
                berserker = True
                print("Berserker activado")
            else:
                print("Falló")

    elif heroe == 2:

        if accion == 1:
            critico = random.randint(1, 5)
            if critico == 1:
                daño = 28
                print("¡Crítico!")
            else:
                daño = 14

        elif accion == 2:
            daño = 22
            print("Falcon Assault ejecutado")

        elif accion == 3:
            prob = random.randint(1, 2)
            if prob == 1:
                wind_walker = True
                print("Wind Walker activado")
            else:
                print("Falló")

    else:

        if accion == 1:
            if arcane_shield:
                daño = 35
                print("Meteor Storm potenciado")
                arcane_shield = False
            else:
                daño = 20

        elif accion == 2:
            daño = 18
            print("Frost Ruin ejecutado")

            prob = random.randint(1, 3)
            if prob == 1:
                congelado = True
                print("El jefe se congeló")

        elif accion == 3:
            prob = random.randint(1, 2)
            if prob == 1:
                arcane_shield = True
                print("Arcane Shield activado")
            else:
                print("Falló")

    if accion == 1 or accion == 2:
        vida_jefe = vida_jefe - daño
        print("Daño al jefe:", daño)

    if vida_jefe <= 0:
        carta = jefe
        exp = exp + 1000
        job = job + 300

        print("\nHas derrotado al jefe")
        print("Recompensas:")
        print("Carta:", carta)
        print("EXP:", exp)
        print("Job:", job)
        break

    print("\nTurno del jefe")

    if congelado:
        print("El jefe pierde el turno")
        congelado = False

    elif wind_walker:
        print("El jefe falló")
        wind_walker = False

    else:
        daño_jefe = random.randint(10, 18)

        if arcane_shield:
            daño_jefe = daño_jefe // 2
            print("Arcane Shield redujo daño")

        vida_jugador = vida_jugador - daño_jefe
        print("El jefe te dañó:", daño_jefe)

print("\n=== RESULTADO ===")

if vida_jugador <= 0:
    print("Perdiste")
elif vida_jefe <= 0:
    print("Ganaste")
else:
    print("Empate")