tus_puntos = 1500
sus_puntos = 1570
diferencia = abs(tus_puntos - sus_puntos)
if diferencia <= 50:
    print("Partida Perfecta")
elif diferencia <= 100:
    print("Partida Justa")
else:
    print("Buscando a otro rival...")
