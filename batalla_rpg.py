'''
Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

Requerimientos:
1. El programa corre mientras ambos sigan vivos (Vida > 0).
2. En cada turno, el jugador elige una opción:
- Atacar: Quita 20 de vida al Jefe.
- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.
3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.
4. Al final, indica si ganaste o el Jefe te derrotó.
'''

vida_jugador = 100
mana_jugador = 20

vida_jefe_final = 150

while vida_jugador > 0 and vida_jefe_final > 0 :
    print("")
    print(f"Vida Jugador: {vida_jugador}")
    print(f"Maná Jugador: {mana_jugador}\n")
    print(f"Vida Jefe Final: {vida_jefe_final}\n")
    print("1) Atacar.")
    print("2) Magia.")
    print("3) Poción de vida")

    opcion = int (input("Seleccione una opción: "))

    match opcion :
        case 1 :
            vida_jefe_final -= 20
        case 2 :
            if mana_jugador > 5 :
                mana_jugador - 5
                vida_jefe_final -= 50
            else :
                print("No hay maná suficiente.")
                continue
        case 3 :
            if mana_jugador > 0 :
                mana_jugador = 0
                vida_jugador += 30
            else :
                print("No hay maná suficiente.")
                continue
    if vida_jefe_final > 0 :
        vida_jugador -= 15

if vida_jugador > 0 :
    print("¡HAS DERROTADO AL JEFE FINAL! ¡FELICIDADES!")
else :
    print("Has perdido :c")