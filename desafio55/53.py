elo = {"puntos": 1500}
elo_rival = [{"id":1, "elo":1200}, {"id":2, "elo": 1490}, {"id":3, "elo":1800}]
diferencia_minima = 9999
rival_escogido = None
for rival in elo_rival:
    diferencia = abs(elo["puntos"] - rival["elo"])

    if diferencia < diferencia_minima:
        diferencia_minima = diferencia      #Cambia el valor de diferencia_minima al del jugador recurrente.
        rival_escogido = rival["id"]

print(rival_escogido)