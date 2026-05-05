#Ejercicio 19: Matchmaking por ELO (Juegos)

jugador = 1500
oponente = 1570

diferencia = abs(jugador - oponente)

if diferencia <= 50:
    print("Partida perfecta")
elif diferencia <= 100:
    print("Partida justa")
else:
    print("Buscando otro rival")