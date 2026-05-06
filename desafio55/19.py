puntos = 1500
rival = 1570

if abs(puntos - rival) <= 50:
    print("Partida Perfecta")
elif abs(puntos - rival) < 100:
    print("Partida Justa")
elif abs(puntos - rival) >= 100:
    print("Buscando otro rival...")