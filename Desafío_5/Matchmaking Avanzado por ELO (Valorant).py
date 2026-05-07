mi_elo = 1500

rivales = [
    {'id': 1, 'elo': 1200},
    {'id': 2, 'elo': 1490},
    {'id': 3, 'elo': 1800}
]

diferencia_minima = 9999
mejor_rival = None

for rival in rivales:

    diferencia = abs(mi_elo - rival['elo'])

    if diferencia < diferencia_minima:

        diferencia_minima = diferencia
        mejor_rival = rival['id']

print(mejor_rival)