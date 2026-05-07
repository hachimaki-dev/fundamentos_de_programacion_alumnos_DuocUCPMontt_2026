mis_puntos = 1500
rivales = [{"id": 1,"elo": 1200},
           {"id": 2,"elo": 1490},
           {"id": 3,"elo": 1800}]
rival_escogido = None
diferencia_minima = 99999999999
for r in rivales:
    diferencia = abs(mis_puntos - r["elo"])
    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_escogido = r["id"]
print(rival_escogido)