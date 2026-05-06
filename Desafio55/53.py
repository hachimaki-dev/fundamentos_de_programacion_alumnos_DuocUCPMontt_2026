elo_me = 1500
rivales = [{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]
diferencia_minima = rivales[0].get("elo")

for rival in rivales:
    diferencia_rival = abs(elo_me - rival.get("elo"))
    if diferencia_rival < diferencia_minima:
        diferencia_minima = diferencia_rival
        id_rival = rival.get("id")

print(id_rival)