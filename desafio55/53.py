elo = {"puntos": 1500}
elo_rival = [{"id":1, "elo":1200}, {"id":2, "elo": 1490}, {"id":3, "elo":1800}]
diferencia_minima = 9999
rival_escogido = None
for rival in elo_rival:
    if abs(elo["puntos"] - rival["elo"]) < diferencia_minima:
        rival_escogido = rival["id"]
        print(abs(elo["puntos"] - rival["elo"]))

print(rival_escogido)