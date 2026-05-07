mis_puntos = 1500

puntos_rival = 1570

diferencia = abs(mis_puntos - puntos_rival)

if diferencia <= 50:
    print("Partida Perfecta")
elif diferencia <= 100:
    print("Partida Justa")
elif diferencia > 100:
    print("Buscando otro rival...")