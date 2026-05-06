print("Oponente Encontrado!\nTu ELO: 1500\nSu ELO: 1570")
tu_elo = 1500
elo_oponente = 1570
diferencia_puntos = abs(tu_elo - elo_oponente)

if diferencia_puntos <= 50:
    print("Partida PERFECTA!")
elif diferencia_puntos <= 100:
    print("Partida Justa.")
else:
    print("Buscando otro rival...")