yo = 1500
rivales = [{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]
diferencia_minima = 9999
rival_elegido = None
for i in rivales:
    diferencia = abs(yo - i['elo'])
    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_elegido = i['id']
print(rival_elegido)