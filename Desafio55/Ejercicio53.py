'''Ejercicio 53: Matchmaking Avanzado por ELO (Valorant)
Busca al oponente más parejo en una lista de jugadores conectados.

Datos Iniciales: Tú tienes 1500 puntos. Los rivales están en una lista de diccionarios: `[{'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}]`.

Reglas de Negocio: Para que la pelea sea justa, debes emparejarte con el jugador que tenga la diferencia de puntos más pequeña comparada contigo.

Restricciones: Crea una variable `diferencia_minima` y ponle un número gigante (como 9999). 

Recorre la lista de rivales con un `for`. Resta tus puntos con los de ellos usando la función `abs()` para que no hayan negativos.

 Si la diferencia es menor que tu `diferencia_minima`, 
 actualiza tus variables guardando ese nuevo récord y guardando el `'id'` de ese rival. Imprime solo el id del rival elegido al final.'''

Rivales = [{'ID': 1, 'Elo': 1200}, {'ID': 2, 'Elo': 1490}, {'ID': 3, 'Elo': 1800}]

ID_mas_acertada = []

Diferencias = []

Mis_puntos = 1500

for Rival in Rivales:

    Diferencias.append(abs(Rival['Elo'] - Mis_puntos))

for ID in Rivales:

    if min(Diferencias) == abs(ID['Elo'] - Mis_puntos):

        ID_mas_acertada.append(ID['ID'])

print(ID_mas_acertada)