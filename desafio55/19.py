puntos_usuario = 1500
puntos_adversario = 1570
dif_puntos = abs(puntos_usuario - puntos_adversario)
if dif_puntos <= 5:
    print("Partida Perfecta")
elif dif_puntos <= 100:
    print("Partida Justa")
else:
    print("Buscando otro rival...")
