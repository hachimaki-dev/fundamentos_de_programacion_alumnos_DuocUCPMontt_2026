tus_puntos = 1500
sus_puntos = 1570

diferencia = abs(tus_puntos - sus_puntos)

if diferencia <= 50:
    print('Perfecta')
elif diferencia <= 100:
    print('Justa')
else:
    print('Buscando otro rival...')