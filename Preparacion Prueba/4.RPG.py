#Crea un simulador de combate de un juego de rol. El jugador tiene 100 de Vida y 20 de Maná. El Jefe Final tiene 150 de Vida.

#Requerimientos:
#1. El programa corre mientras ambos sigan vivos (Vida > 0).
#2. En cada turno, el jugador elige una opción:
#- Atacar: Quita 20 de vida al Jefe.
#- Magia (Gasta 5 maná): Quita 50 de vida al Jefe. Solo funciona si tienes maná suficiente.
#- Poción de Vida: Te cura 30 de vida pero gasta todo tu Maná restante.
#3. Tras el turno del jugador, si el Jefe sigue vivo, este ataca quitándote 15 de vida.
#4. Al final, indica si ganaste o el Jefe te derrotó.


vidajugador = 100
vidajefe = 150
manajugador = 20

while vidajugador >0 and vidajefe > 0:
    print(f"""Dark Bowser
          HP = {vidajefe}""")
    
    print(f"""\n¿Que deberia hacer Mario?
          1) Atacar = Ataque sin mana
          2) Magia = Bola de Fuego (Cuesta 5 de mana)
          3) Cura = Champiñon magico (Cuesta todo el mana restante, cura 30 de HP)
          
          MARIO HP {vidajugador} MANA {manajugador}""")
    
    opcion = input("")
    if opcion == "atacar" or opcion == "Atacar" or opcion == "1":
        vidajefe = vidajefe - 20
        print ("Mario ataca causando 20 de daño")
    elif opcion == "Magia" or opcion == "magia" or opcion == "2":
        vidajefe = vidajefe - 20
        print ("Mario ataca causando 20 de daño")