tus_puntos = 1500
puntos_rival = 1570
diferencia = abs(tus_puntos - puntos_rival)

if diferencia <= 50:
    print("Partida perfecta")
elif diferencia <= 100:
    print("Partida justa")
else:
    print("Buscando otro rival")