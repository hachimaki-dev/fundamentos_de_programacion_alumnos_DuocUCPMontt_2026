tus_puntos = 1500
sus_puntos = 1570
diferencia = abs(tus_puntos - sus_puntos)
if diferencia <= 50:
    print("perfecta")
elif diferencia <= 100:
    print(" Partida justa")
else: 
    print("buscando otro rival...")