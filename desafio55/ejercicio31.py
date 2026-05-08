#Controla el orden en que se reproducen las canciones de tu playlist.
#Datos Iniciales: Tienes esta lista de canciones: `['B', 'C']`.
#Reglas de Negocio: El usuario apretó 'Agregar a la cola' en la canción 'D' (eso la manda al final). Luego apretó 'Reproducir siguiente' en la canción 'A' (eso la manda al inicio de todo, empujando a las demás).
#Restricciones: Usa la herramienta `.append()` para meter cosas al final de la lista. Usa `.insert(0, ...)` para obligar a una canción a ponerse en la posición cero (el principio). Imprime la lista completa al terminar.
playlist = ['B', 'C']
playlist.append("D")
playlist.insert(0,"A")
print(playlist)