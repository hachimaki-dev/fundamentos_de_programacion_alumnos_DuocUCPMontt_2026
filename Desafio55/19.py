tu_elo=1500
rival=1570
diferencia_de_elo= abs(tu_elo-rival)
if diferencia_de_elo<=50:
    print("Partida Perfecta")
elif 50<diferencia_de_elo<=100:
    print("Partida Justa")
else:
    print("Buscando otro rival")