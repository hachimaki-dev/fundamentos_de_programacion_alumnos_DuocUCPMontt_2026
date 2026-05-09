puntos_yo = 1500
puntos_rival = 1570
diferencia = puntos_yo - puntos_rival
if -50 <= diferencia <= 50:
    print("Partida Perfecta")
elif -100 <= diferencia <= 100:
    print("Partida Justa")
else:
    print("Buscando otro rival")