mis_puntos = 1500
rivales = [{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]

diferencia_minima = 9999
rival_elegido_id = None

for rival in rivales:
    diferencia_actual = abs(mis_puntos - rival['elo'])
    
    if diferencia_actual < diferencia_minima:
        diferencia_minima = diferencia_actual
        rival_elegido_id = rival['id']

print(rival_elegido_id)