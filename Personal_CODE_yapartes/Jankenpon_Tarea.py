Piedra = 1
Papel = 2
Tijera = 3
Opción_Player1 = 0
Opción_Player2 = 0
Marcador_Player1 = 0
Marcador_Player2 = 0
Resultado_Final = abs(Marcador_Player1 - Marcador_Player2)

print(f"""Bienvenido al PIEDRA PAPEL O TIJERAS
    
            じゃんけんぽん 
      
      """)
while Marcador_Player1 !=3 and Marcador_Player2 !=3:
    print(f"""==Jugador 1 tiene ({Marcador_Player1}) puntos y el Jugador 2 tiene ({Marcador_Player2}) puntos==""")
    Opción_Player1=int(input("""
          Turno del jugador 1 Elija:
                              
         (1)Piedra (2)Papel (3)Tijera
          ¡JUGADOR 2 NO DEBE MIRAR! """))
    
    Opción_Player2 = int(input("""
          Turno del jugador 2 Elija:
                               
        (1)Piedra (2)Papel (3)Tijera
          ¡JUGADOR 1 NO DEBE MIRAR! """))
    if Opción_Player1 == 1 and Opción_Player2 == 3:
        Marcador_Player1 = Marcador_Player1 +1
    
        print("El jugador 1 usó piedra y jugador 2 usó tijeras")
    if Opción_Player1 == 1 and Opción_Player2 == 2:
        Marcador_Player2 = Marcador_Player2 +1
        print("El jugador 1 usó piedra y jugador 2 usó Papel")
    if Opción_Player1 == 2 and Opción_Player2 == 1:
        Marcador_Player1 = Marcador_Player1 +1
        print("El jugador 1 usó Papel y jugador 2 usó Piedra")
    if Opción_Player1 == 2 and Opción_Player2 == 3:
        Marcador_Player2 = Marcador_Player2 +1
        print("El Jugador 1 usó Papel y jugado3 2 usó Tijeras")
    if Opción_Player1 == 3 and Opción_Player2 == 1:
        Marcador_Player2 = Marcador_Player2 +1
        print("El Jugador 1 usó Tijeras y jugado3 2 usó Piedra")
    if Opción_Player1 == 3 and Opción_Player2 == 2:
        Marcador_Player1 = Marcador_Player1 +1
        print("El Jugador 1 usó Tijeras y jugado3 2 usó Papel")
    if Opción_Player1 == Opción_Player2:
        Marcador_Player1 = Marcador_Player1 +1
        Marcador_Player2 = Marcador_Player2 +1
        if Opción_Player1 == 1:
            print("ES UN EMPATE. Ambos jugadores usaron PIEDRA")
        if Opción_Player1 == 2:
            print("ES UN EMPATE. Ambos jugadores usaron PAPEL")
        if Opción_Player1 == 3:
            print("ES UN EMPATE. Ambos jugadores usaron TIJERAS")

if Marcador_Player1 > Marcador_Player2:
    print("el Ganador es el jugador 1")
elif Marcador_Player2 > Marcador_Player1:
    print("El ganador es el jugador 2")
else: 
    print("""
          =====ES UN EMPATE=====""")
       
Resultado_Final = abs(Marcador_Player1 - Marcador_Player2)

print(f"""PUNTAJE FINAL:    
      ===Jugador 1 ({Marcador_Player1} --- {Marcador_Player2}) Jugador 2===
      DIFERENCIA: {Resultado_Final} puntos""")
print("""
      =======Fin del juego=======""")


