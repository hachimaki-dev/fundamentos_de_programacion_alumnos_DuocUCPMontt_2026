
jugador=1500
rivales=[{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]
diferencia_minima=9999
rival_escogido=None
diferencia_jugador=0
for i in rivales:
    diferencia_jugador=abs(jugador-i['elo'])
    if diferencia_jugador < diferencia_minima:
        diferencia_minima= diferencia_jugador
        rival_escogido= i['id'] 
        
print(rival_escogido)        