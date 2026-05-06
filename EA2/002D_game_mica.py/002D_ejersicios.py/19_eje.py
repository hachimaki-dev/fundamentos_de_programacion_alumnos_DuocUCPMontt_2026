tienes_puntos = 1500
rival_puntos = 1570

diferencia = abs(tienes_puntos - rival_puntos)

if diferencia <= 50:
    print("la pelea es perfecta")
elif diferencia <= 100:
    print("la pelea es justa")
else:
    print("buscando otro rival")
