#Ejercicio 53: Matchmaking Avanzado por ELO (Valorant)
#Busca al oponente más parejo en una lista de jugadores conectados.

#Datos Iniciales: Tú tienes 1500 puntos. Los rivales están en una lista de diccionarios: `[{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]`.

#Reglas de Negocio: Para que la pelea sea justa, debes emparejarte con el jugador que tenga la diferencia de puntos más pequeña comparada contigo.

#Restricciones: Crea una variable `diferencia_minima` y ponle un número gigante (como 9999). Recorre la lista de rivales con un `for`. Resta tus puntos con los de ellos usando la función `abs()` para que no hayan negativos. Si la diferencia es menor que tu `diferencia_minima`, actualiza tus variables guardando ese nuevo récord y guardando el `'id'` de ese rival. Imprime solo el id del rival elegido al final.

#Pista de Ayuda:
#Inicializa diferencia_minima = 9999 y rival_escogido = None antes del ciclo.

#Mis puntos. puntos de los rivales juntos con sus id y diferencia a
my_points = 1500
rivales = [{
    'id':1,
    'elo':1200
},
{
    'id':2,
    'elo':1490
},
{
    'id':3,
    'elo':1800
}]
diferencia_minima = 9999
rival_escogido = None

for player in rivales:
    diferencia = abs(my_points - player['elo'])

    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_escogido = player['id']

print(rival_escogido)