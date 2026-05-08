mis_puntos = 1500
rivales = [{"id": 1, "elo": 1200}, {"id": 2, "elo": 1490}, {"id": 3, "elo": 1800}]
diferencia_minima = 9999
rival_escogido = None
for rival in rivales:
    diferencia = abs(mis_puntos - rival["elo"])

    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_escogido = rival["id"]

print(rival_escogido)

