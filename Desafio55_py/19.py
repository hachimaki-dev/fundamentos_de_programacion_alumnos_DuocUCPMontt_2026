puntos = 1500
rival = 1570

diferencia = rival - puntos


if diferencia <= 50:
    print("LA PARTIDA ES PERFECTA")
elif diferencia <= 100:
    print("LA PARTIDA ES JUSTA")
elif diferencia > 100:
    print("BUSCANDO OTRO RIVAL . . .")

