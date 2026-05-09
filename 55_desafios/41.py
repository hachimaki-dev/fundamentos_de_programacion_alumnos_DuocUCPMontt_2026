#Crea el perfil de un jugador usando diccionarios (la mejor forma de guardar datos complejos).

#Datos Iniciales: Vas a crear un jugador nuevo.

#Reglas de Negocio: Un diccionario guarda datos en parejas (una 'llave' y su 'valor'). El jugador debe tener la llave `'nombre'` (pon tu nombre de valor) y la llave `'nivel'` (que parte en 1).

#Restricciones: Escribe el diccionario a mano usando las llaves `{}`. Luego, haz que Python extraiga tu nombre accediendo a la llave `'nombre'` usando corchetes. Imprime solo tu nombre.

jugador = {
    "nombre": "Vicente",
    "nivel": 1
}

print(jugador["nombre"])