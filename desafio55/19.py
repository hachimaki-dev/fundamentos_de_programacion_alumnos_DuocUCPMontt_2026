mis_puntos = 1500
rival_puntos = 1570

diferencia = abs(mis_puntos - rival_puntos)
if diferencia <= 50:
    print("partida perfecta")
elif diferencia <= 100:
    print("partida justa")
else: 
    print("buscando otro rival ")

    