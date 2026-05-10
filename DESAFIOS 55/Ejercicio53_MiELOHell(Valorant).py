#Datos Iniciales: Tú tienes 1500 puntos. Los rivales están en una lista de diccionarios: ``.

#Reglas de Negocio: Para que la pelea sea justa, debes emparejarte con el jugador que tenga la diferencia de puntos más pequeña comparada contigo.

#Restricciones: Crea una variable `diferencia_minima` y ponle un número gigante (como 9999). Recorre la lista de rivales con un `for`. Resta tus puntos con los de ellos usando la función `abs()` para que no hayan negativos. Si la diferencia es menor que tu `diferencia_minima`, actualiza tus variables guardando ese nuevo récord y guardando el `'id'` de ese rival. Imprime solo el id del rival elegido al final.
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