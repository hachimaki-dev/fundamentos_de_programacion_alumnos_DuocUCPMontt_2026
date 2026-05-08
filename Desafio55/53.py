mis_puntos = 1500
rivales = [{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]
dif_minima = 9999
rival_escogido = None
for rival in rivales:
    dif_de_puntos = abs(mis_puntos - rival["elo"])
    if dif_de_puntos < dif_minima:
        dif_minima = dif_de_puntos
        rival_escogido = rival["id"]
    
print(rival_escogido)