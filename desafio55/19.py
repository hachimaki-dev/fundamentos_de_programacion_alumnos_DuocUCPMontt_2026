puntos_jugador = 1500
puntos_rival = 1570

diferencia_puntos = abs(puntos_jugador - puntos_rival)

if diferencia_puntos <= 50:
    print("Partida Perfecta")
elif diferencia_puntos <= 100:
    print("Partida Justa")
else:
    print("Buscando otro rival...")
