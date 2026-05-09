#Muestra el último video que vio el usuario en su perfil.

historial = ['Intro', 'Tutorial', 'Gameplay']

#Reglas de Negocio: A nadie le importa lo primero que viste, quieren ver lo más reciente. Necesitas dar vuelta la lista para que lo más nuevo quede de primero, y luego mostrar solo ese video.

#Restricciones: Usa `.reverse()` para dar vuelta la lista físicamente. Luego, imprime solo el elemento que quedó en la posición `0`.

historial.reverse()
print(historial[0])