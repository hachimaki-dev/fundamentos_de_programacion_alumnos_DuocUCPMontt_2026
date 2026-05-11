Mi_elo =  1500
Enemigos = [{"id": 1, 'elo': 1200},{'id': 2, 'elo': 1490},{'id': 3, 'elo': 1800}]
diferencia_minima = 9999
rival_escogido = None
for rivales in Enemigos:
    diferencia = abs(Mi_elo - rivales['elo'])
    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_escogido = rivales['id']
print(rival_escogido)