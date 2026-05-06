tus_puntos = 1500
puntos_rival = 1570

diferencia = abs(tus_puntos - puntos_rival)

diferencia_perfecta = 50
diferencia_justa = 100

if diferencia <= diferencia_perfecta:
    print("Partida Perfecta")
elif diferencia <= diferencia_justa:
    print("Partida Justa")
else:
    print("Buscando otro rival de tu mismo nivel..")