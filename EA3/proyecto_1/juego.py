# ==========================================================
# Nombre del juego: Las Catacumbas del Código Perdido
# Autor: John Brandon Rios Gonzalez
# Fecha: 18/05/2026
#
# En esta mazmorra el jugador explora antiguos túneles
# llenos de errores digitales y criaturas corruptas.
# El objetivo es encontrar el núcleo perdido y restaurar
# el sistema antes de que todo colapse.
#
# Héroe:
# Un programador explorador experto en tecnología antigua.
#
# Enemigos:
# Bugs gigantes, virus corruptos y guardianes digitales.
# ==========================================================
import random


HP_INICIAL = 20
ATAQUE_INICIAL = 5
SALAS_TOTALES = 5
HP_POCION = 8
DAÑO_HUIDA = 2



def crear_jugador(nombre):

    print(f"[DEBUG] Creando jugador: {nombre}")

    jugador = {
        "nombre": nombre,
        "hp": HP_INICIAL,
        "hp_max": HP_INICIAL,
        "ataque": ATAQUE_INICIAL,
        "xp": 0,
        "oro": 0,
        "nivel": 1,
        "energia_codigo": 100,
        "inventario": ["pocion", "cafe"]
    }

    print(f"[DEBUG] Jugador creado + {jugador}")

    return jugador


def crear_enemigo():
    enemigos_disponibles = [
        {
            "nombre": "Bug corrupto",
            "hp": 8,
            "ataque": 2,
            "oro": 3,
            "xp": 5
        },

        {
            "nombre": "Virus gigante",
            "hp": 12,
            "ataque": 4,
            "oro": 6,
            "xp": 8
        },

        {
            "nombre": "IA descontrolada",
            "hp": 18,
            "ataque": 6,
            "oro": 10,
            "xp": 12
        }
    ]

    enemigo = random.choice(enemigos_disponibles)

    print(f"[DEBUG] Enemigo generado = {enemigo['nombre']}")

    return enemigo


def mostrar_estado_jugador(jugador):


    barra_hp = (
        "█" * jugador["hp"] +
         "░" * (jugador["hp_max"] - jugador["hp"])
    )

    print("\n" + "=" * 45)
    print(f" 👨 Heroe: {jugador['nombre']}")
    print(f" ❤️ Vida: {jugador['hp']}/{jugador['hp_max']}")
    print(f" {barra_hp}")
    print(f"  ⚔ Ataque: {jugador['ataque']}")
    print(f" ⭐ Nivel: {jugador['nivel']}")
    print(f" ✨ XP: {jugador['xp']}")
    print(f" 💰 oro: {jugador['oro']}")
    print(f" 🔋 energia: {jugador['energia_codigo']}")
    print(f" 🎒 inventario: {jugador['inventario']}")
    print("=" * 45)


def mostrar_estado_combate(jugador, enemigo):

    mostrar_estado_jugador(jugador)

    print(f"\n 👾 enemigo: {enemigo['nombre']} ")
    print(f" ❤️ HP enemigo: {enemigo['hp']}")
    print(f"=" * 45)


def mostrar_menu_combate(jugador):

    print("\n¿Que deseas hacer?")
    print("[1] Atacar")
    print("[2] Usar pocion")
    print("[3] Huir (-2 HP)")

    if "cafe" in jugador["inventario"]:
        cantidad = jugador["inventario"].count("cafe")
        print(f"[4] Usar cafe ({cantidad})")

    opcion = input("opcion: ").strip()

    print(f"[DEBUG] Opcion ingresada: {opcion}")

    return opcion


def jugador_ataca(jugador, enemigo):

    daño = jugador["ataque"] + random.randint(0,3)


    if random.random() < 0.2:
        daño *= 2
        print("[DEBUG] ¡CRITICO!")
    
    enemigo["hp"] -= daño

    if enemigo["hp"] < 0:
        enemigo["hp"] = 0

    print(f"[DEBUG] Jugador hace {daño} de daño")

    return daño


def enemigo_ataca(jugador, enemigo):

    daño = enemigo["ataque"] + random.randint(0,2)


    jugador["hp"] -= daño


    if jugador["hp"] <= 0:
        jugador["hp"] = 0

    print(f"[DEBUG] Enemigo hace {daño} de daño")

    return daño


def esta_vivo(personaje):

    return personaje["hp"] > 0


def dar_recompensa(jugador, enemigo):

    jugador["oro"] += enemigo["oro"]

    encontro_pocion = random.random() <= 0.5

    if encontro_pocion:
        jugador["inventario"].append("pocion")

    print(f"[DEBUG] Oro ganado: {enemigo['oro']}")

    return encontro_pocion

def usar_pocion(jugador):

    if "pocion" in jugador["inventario"]:

        jugador["inventario"].remove("pocion")

        hp_antes = jugador["hp"]

        jugador["hp"] += HP_POCION

        if jugador["hp"] > jugador["hp_max"]:
            jugador["hp"] = jugador["hp_max"]

        print(f"[DEBUG] HP: {hp_antes} =  {jugador['hp']}")

        return True

    print("[DEBUG]  No tienes pociones")

    return False


def usar_cafe(jugador):

    if "cafe" in jugador["inventario"]:

        jugador["inventario"].remove("cafe")

        ataque_antes = jugador["ataque"]

        jugador["ataque"] += 2

        print(f"[DEBUG] Cafe usado = ataque: {ataque_antes} = {jugador['ataque']}")

        return True

    print("[DEBUG] No tienes cafe")

    return False


def ganar_xp(jugador, enemigo):

    jugador["xp"] += enemigo["xp"]

    print(f"[DEBUG] XP ganada: +{enemigo["xp"]}")

    if jugador["xp"] >=  20:

        jugador["nivel"] += 1
        jugador["xp"] = 0


        jugador["ataque"] += 1
        jugador["hp_max"] += 5
        jugador["hp"] = jugador["hp_max"]

        print("\n★ Subiste de nivel ★")
        print(f"Nivel actual: {jugador["nivel"]}")
        print("+1 ataque")
        print("+5 HP MAX")
        print(f"Vida restaurada")




def combate(jugador, enemigo):

    print(f"n\⚔ COMIENZA EL COMBATE VS {enemigo["nombre"]}")

    while esta_vivo(jugador) and esta_vivo(enemigo):

        mostrar_estado_combate(jugador, enemigo)

        opcion = mostrar_menu_combate(jugador)
        if opcion == "1":

            daño = jugador_ataca(jugador, enemigo)

            print(f"Golpeas al enemigo y haces {daño} de daño")

            if not esta_vivo(enemigo):


                print(f"\n🎉 Derrotaste a {enemigo["nombre"]}")

                ganar_xp(jugador, enemigo)

                encontro = dar_recompensa(jugador, enemigo)

                print(f"Ganas {enemigo["oro"]} de oro")

                if encontro:
                    print("Encontraste una pocion")

                break


            daño_recibido = enemigo_ataca(jugador, enemigo)

            print(f"{enemigo["nombre"]} te hace {daño_recibido} de daño")


        elif opcion == "2":

            if usar_pocion(jugador):
                print("Usaste una pocion")
            else:
                print("No tienes pociones")

            if esta_vivo(enemigo):


                daño_recibido = enemigo_ataca(jugador, enemigo)

                print(f"{enemigo["nombre"]} te hace {daño_recibido} de daño")



        elif opcion == "3":

            jugador["hp"] -= DAÑO_HUIDA

            if jugador["hp"] < 0:
                jugador["hp"] = 0


            print(f"Huyes del combate y pierdes {DAÑO_HUIDA} HP")


            break


        elif opcion == "4":

            if usar_cafe(jugador):
                print("☕ Tomas cafe y aumentas tu ataque")
            else:
                print("No tienes cafe")

            if esta_vivo(enemigo):

                daño_recibido = enemigo_ataca(jugador, enemigo)

                print(f"{enemigo["nombre"]} te hace {daño_recibido} de daño")


        else:


            print("Opcion invalida")


        return esta_vivo(jugador)
    


def jugar():

    print("\n" + "=" * 45)
    print(" ⚔ LAS CATACUMBAS DEL CODIGO PERDIDO ⚔")
    print("=" * 45)

    nombre = input("Ingresa el nombre de tu heroe: ").strip()

    if nombre == "":
        nombre = "Heroe anonimo"

    jugador = crear_jugador(nombre)

    sala_actual = 1

    while sala_actual <= SALAS_TOTALES and esta_vivo(jugador):

        print("\n" + "-" * 45)
        print(f" SALA {sala_actual} DE {SALAS_TOTALES}")
        print("-" * 45)

        enemigo = crear_enemigo()

        sobrevivio = combate(jugador, enemigo)


        if not sobrevivio:
            print("\n☠ Has sido derrotado...")
            break

        print(f"\n✅ Sala {sala_actual} completada")


        if sala_actual < SALAS_TOTALES:

            jugador["hp"] += 3

            if jugador["hp"] > jugador["hp_max"]:
                jugador["hp"] = jugador["hp_max"]

            print("✨ Recuperas 3 HP antes de continuar")

        sala_actual += 1

        if sala_actual <= SALAS_TOTALES:
            input("\n[ENTER para continuar]")



        print("🏆 ¡VICTORIA!")
        print("Has limpiado las catacumbas.")

    else:

        print("💀 DERROTA")
        print(f"Llegaste hasta la sala {sala_actual}")

    mostrar_estado_jugador(jugador)

    print("=" * 45)


if __name__ == "__main__":
    jugar()
    



        



