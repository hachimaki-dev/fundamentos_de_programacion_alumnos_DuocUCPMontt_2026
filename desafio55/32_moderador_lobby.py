# Ejercicio 32: Moderador de Lobby (LoL)
# Echa a un jugador tóxico de la sala de espera antes de empezar el juego.

# Datos Iniciales: Los jugadores en la sala son `['P1', 'Troll99', 'P2']`.

# Reglas de Negocio: Troll99 fue reportado y no puede jugar. 
# Tienes que sacarlo de la lista para que la partida pueda empezar.

# Restricciones: No escribas la lista de nuevo a mano, eso es trampa. 
# Usa la herramienta `.remove()` escribiendo exactamente el nombre del jugador que quieres borrar. 
# Imprime la lista limpia.

jugadores = ["P1", "Troll99", "P2"]
jugadores.remove("Troll99")

print(jugadores)