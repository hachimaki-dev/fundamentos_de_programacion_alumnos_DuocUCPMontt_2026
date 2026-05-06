mis_puntos = 1500
rival = 1570
diferencia = rival - mis_puntos
if diferencia <= 50:
    print("partida perfecta")
elif diferencia <= 100:
    print("partida justa")
else:
    diferencia > 100
    print("buscando otro rival")