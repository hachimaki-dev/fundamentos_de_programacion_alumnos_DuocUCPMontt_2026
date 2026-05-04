elo_jugador=1500
elo_rival=1570

matchmaking=abs(elo_jugador-elo_rival)

if matchmaking <=50:
    print('Partida Perfecta')
elif matchmaking <= 100:
    print('Partida Justa') 
elif matchmaking > 100:
    print('Buscando otro rival...')