# Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

"""
1. El programa corre mientras ambos sigan vivos (Vida > 0).
2. En cada turno, el jugador elige una opción:
- Atacar: Quita 20 de vida al Jefe.
- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.
3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.
4. Al final, indica si ganaste o el Jefe te derrotó.
"""

vida_del_jugador = 165
vida_del_jefe = 200
contador_de_turno = 0
mana = 30

print("El jefe se acerca!")
while vida_del_jefe > 0:
    vida_del_jugador -= 15
    print(f"Vida del Jugardor: {vida_del_jugador} | Mana: {mana} | Vida del Jefe: {vida_del_jefe} | Turno: {contador_de_turno}")
    print("Elija su accion! (1-3)")
    print("1. Atacar (-20 HP)")
    print("2. Magia (Gastas 5 de Mana | -50 HP)")
    print("3. Pocion de Vida (Cura 30 HP | Gasta todo el mana restante!)")
    seleccion = int(input("[]: "))
    if seleccion == 1:
        vida_del_jefe -= 20
        contador_de_turno += 1
    if seleccion == 2:
        if mana > 0:
            vida_del_jefe -= 50
            contador_de_turno += 1
        else:
            print("Mana insuficiente!")
    if seleccion == 3:
        if mana > 0:
            vida_del_jugador += 30
            mana = 0
        else:
            print("Mana insuficiente!")
    if vida_del_jugador <= 0:
        break

if vida_del_jefe > 0:
    print("Has sido derrotado")
if vida_del_jefe <= 0:
    print("Eres victorioso!")