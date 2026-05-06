mis_puntos = 1500
puntos_rival = 1570
diferencia = abs(mis_puntos - puntos_rival)
if diferencia <= 50:
    print("partida perfecta")
elif diferencia <= 100:
    print("partida justa")
else:
    print("buscando otro rival")