elo = 1500
elo_rival = 1570
if abs(elo - elo_rival) <= 50:
    print("Partida Perfecta")
elif abs(elo - elo_rival) <= 100:
    print("Partida Justa")
else:
    print("Buscando rival...")