"""
Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

Requerimientos:
1. El programa corre mientras ambos sigan vivos (Vida > 0).
2. En cada turno, el jugador elige una opción:
- Atacar: Quita 20 de vida al Jefe.
- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.
3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.
4. Al final, indica si ganaste o el Jefe te derrotó.
"""

Jefe = 150
Jugador = 100
Mana = 20

while Jefe > 0 and Jugador > 0:
    print("Escoge una opcion:")
    print("""- Atacar: Quita 20 de vida al Jefe.
- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.""")
    Respuesta = input()
    if Respuesta == "Atacar":
        Jefe = Jefe - 20
        if Jefe < 0:
            Jefe = 0
            print(f"Vida restante Jefe: {Jefe}")
        else:
            print(f"Le queda {Jefe} puntos de vida al jefe")
    elif Respuesta == "Magia":
        if Mana > 0:
            Jefe = Jefe - 50
            if Jefe < 0:
                Jefe = 0
                print(f"Le queda {Jefe} puntos de vida al jefe")
            else:   
                print(f"Le queda {Jefe} puntos de vida al jefe")
        else:
            print("No tienes suficente Mana")
    elif Respuesta == "Pocion de Vida":
        if Jugador + 30 > 100:
            print("No se puede usar en este momento")
        elif Mana > 0:
            Jugador = Jugador + 30
            Mana = Mana * 0
            print(f"Tienes {Jugador} puntos vida, pero te queda {Mana} de mana")
        else:
            print("No tienes suficiente Mana")   
    else:
        print("???")
    Jugador = Jugador - 15
    if Jugador < 0:
        Jugador = 0
        print(f"Vida restante: {Jugador}")
    else:
        print(f"Vida restante: {Jugador}")
if Jefe > 0:
    print("Esta vez gano el Jefe")
elif Jugador > 0:
    print("Jugador gano")    