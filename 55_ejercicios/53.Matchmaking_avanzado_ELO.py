ELO_user = 1500
ELO_rivales_encontrados = [
    {'id': 1, 'elo' : 1200},
    {'id' : 2, 'elo' : 1490},
    {'id' : 3, 'elo' : 1800}
]
rival_escogido = None
diferencia_minima = 9999

for rival in ELO_rivales_encontrados:
    diferencia = abs(ELO_user - rival['elo'])
    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_escogido = rival['id']
print(rival_escogido)