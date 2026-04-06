# 4. Batalla por Turnos: RPG de Texto
# Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

# Requerimientos:
# 1. El programa corre mientras ambos sigan vivos (Vida > 0).
# 2. En cada turno, el jugador elige una opción:
#   - Atacar: Quita 20 de vida al Jefe.
#   - Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
#   - Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.
# 3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.
# 4. Al final, indica si ganaste o el Jefe te derrotó.

print(" BATALLA RPG ".center(30, "-"))

vida_jugador = 100
mana_jugador = 20
vida_jefe_final = 150
opcion_elegida = ""

while vida_jugador > 0 and vida_jefe_final > 0:
    print("\n-----------------")
    print("TURNO JUGADOR: \n'Atacar'\n'Magia'\n'Pocion de vida'\n'Terminar'")
    print("-----------------")
    opcion_elegida = input("Ingrese su opcion: ").upper()

    if opcion_elegida == "ATACAR":
        vida_jefe_final -= 20
    elif opcion_elegida == "MAGIA":
        if mana_jugador >= 5:
            mana_jugador -= 5
            vida_jefe_final -= 50
        else:
            print("No tienes mana suficiente, necesitas 5")
            print(f"Mana restante: {mana_jugador}")
    elif opcion_elegida == "POCION DE VIDA":
        mana_jugador = 0
        vida_jugador = 100
    elif opcion_elegida == "TERMINAR":
        print("Juego finalizado. No hay ganador")
        break
    
    print(f"\nVida jugador: {vida_jugador} | Vida jefe: {vida_jefe_final}\nMana: {mana_jugador}")

    if vida_jefe_final > 0:
        print("\n--------------")
        print("TURNO DEL JEFE")
        print("---------------")
        vida_jugador -= 15
    

if vida_jugador <= 0:
    print("El jefe te ha derrotado")
elif vida_jefe_final <= 0:
    print("Has derrotado al jefe")

    


            

