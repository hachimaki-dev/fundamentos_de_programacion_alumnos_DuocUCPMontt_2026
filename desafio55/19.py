j_puntos = 1500
r_puntos = 1570
d_puntos = r_puntos - j_puntos
if d_puntos <= 50:
    print("partida perfecta")
elif d_puntos <= 100:
    print("partida justa")
elif d_puntos > 100:
    print("buscando otro rival")