puntos = 1500
puntos_rival = 1570

diferencia_puntos = abs(puntos - puntos_rival)

if diferencia_puntos <= 50:
    print("Partida Perfecta")

elif diferencia_puntos <= 100:
    print("Partida Justa")

elif diferencia_puntos > 100:
    print("Buscando otro rival...")
