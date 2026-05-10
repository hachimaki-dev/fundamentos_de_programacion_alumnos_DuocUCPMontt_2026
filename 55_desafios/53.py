#Busca al oponente más parejo en una lista de jugadores conectados.

puntos_propios = 1500
rivales = [
    {'id': 1, 'elo': 1200}, {'id': 2, 'elo': 1490}, {'id': 3, 'elo': 1800}
]

#Reglas de Negocio: Para que la pelea sea justa, debes emparejarte con el jugador que tenga la diferencia de puntos más pequeña comparada contigo.

#Restricciones: Crea una variable `diferencia_minima` y ponle un número gigante (como 9999). Recorre la lista de rivales con un `for`. Resta tus puntos con los de ellos usando la función `abs()` para que no hayan negativos. Si la diferencia es menor que tu `diferencia_minima`, actualiza tus variables guardando ese nuevo récord y guardando el `'id'` de ese rival. Imprime solo el id del rival elegido al final.

diferencia_minima = 9999
rival_elegido = ""

for rival in rivales:
    diferencia = abs(puntos_propios - rival["elo"])

    if diferencia < diferencia_minima:
        diferencia_minima = diferencia
        rival_elegido = rival["id"]

print(rival_elegido)