puntos_jugador = 1500
puntos_rival = 1570
diferencia = abs(puntos_rival - puntos_jugador)
if diferencia <= 50:
    partida = "Perfecta"
elif diferencia <= 100 and diferencia > 50:
    partida = "Justa"
elif diferencia > 100:
    partida = "Buscando otro rival..."
print(partida)