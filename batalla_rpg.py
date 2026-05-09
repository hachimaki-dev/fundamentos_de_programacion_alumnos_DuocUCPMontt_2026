""" Crea un simulador de combate de un juego de rol.
 El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

Requerimientos:
1. El programa corre mientras ambos sigan vivos (Vida > 0).

2. En cada turno, el jugador elige una opción:
- Atacar: Quita 20 de vida al Jefe.

- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. 
Solo funciona si tienes maná suficiente.
- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.

3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 
15 de vida.

4. Al final, indica si ganaste o el Jefe te derrotó."""

jugador = 100
mana = 20
jefe_final = 150

while jugador > 0 and jefe_final > 0:
    opcion = int(input("1.ataque al jefe   2.ataque de magia  3.pocion de vida -20 de mana"))
    
    if opcion == 1:
        jefe_final = jefe_final - 20
        print(f"has hecho 20 de hp, la vida del jefe es {jefe_final}")
        jugador = jugador - 15
        print(f"el jefe ta ha atacado -15hp, tu vida es {jugador}")

    
    elif opcion == 2:
        mana = mana - 5
        print(f"-5 de mana te queda: {mana} de mana.")
        jefe_final = jefe_final - 50
        print(f"has hecho 50 de hp , la vida del jefe es {jefe_final}")
        jugador = jugador - 15
        print(f"el jefe te ha atacado -15hp, tu vida es {jugador}")
    
    elif opcion == 3:
        mana = mana - mana 
        jugador = jugador + 30
        print(f"te has curado, tu vida es: {jugador}")
        jugador = jugador - 15
        print(f"el jefe ta ha atacado -15hp, tu vida es {jugador}")
    
    if jugador <= 0:
        print(" el jefe te a derrotado")
        
    
    elif jefe_final <= 0:
        print("ganaste lo has vencido")
        
    
    