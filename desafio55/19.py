puntos = 1500
puntos_rival = 1570
diferencia_puntos = puntos_rival - puntos
if diferencia_puntos <= 50:
    print("partida perfecta")
elif diferencia_puntos <= 100:
    print("partida justa")
elif diferencia_puntos > 100:
    print("buscando otro rival")