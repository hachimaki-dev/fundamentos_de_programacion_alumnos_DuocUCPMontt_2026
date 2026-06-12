import random

vida_jugador = 100
ataque_jugador = 20

vida_enemigo = 80
ataque_enemigo = 15

print("=== DUNGEON RPG ===")
print("Entraste a una mazmorra oscura...")

while vida_jugador > 0 and vida_enemigo > 0:
    print("\nTu vida:", vida_jugador)
    print("Vida enemigo:", vida_enemigo)

    print("\n1. Atacar")
    print("2. Curarse")
    print("3. Escapar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        daño = random.randint(10, ataque_jugador)
        vida_enemigo -= daño
        print("Atacaste e hiciste", daño, "de daño")

    elif opcion == "2":
        curacion = random.randint(10, 25)
        vida_jugador += curacion
        print("Te curaste", curacion, "puntos de vida")

    elif opcion == "3":
        print("Escapaste de la mazmorra")
        break

    else:
        print("Opción inválida")

    if vida_enemigo > 0:
        daño_enemigo = random.randint(5, ataque_enemigo)
        vida_jugador -= daño_enemigo
        print("El enemigo te atacó e hizo", daño_enemigo, "de daño")

if vida_jugador <= 0:
    print("\nPerdiste, el enemigo te derrotó")

elif vida_enemigo <= 0:
    print("\nGanaste, derrotaste al enemigo")