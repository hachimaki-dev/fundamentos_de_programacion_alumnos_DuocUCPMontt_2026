"""Ejercicio 25: Filtro de Palabras (Discord)
Crea un robot moderador de chat que censure insultos.

Datos Iniciales: Tienes una lista de mensajes en el chat: `['hola', 'noob', 'genial', 'manco']`.

Reglas de Negocio: El bot revisa las palabras una por una. Las palabras 'noob' y 'manco' están prohibidas. 

Si el bot ve una de esas palabras, debe cambiarla por el texto '[CENSURADO]'. Si la palabra es buena, la deja igual.

Restricciones: Recorre la lista con un `for`. Adentro, usa un `if` para revisar si la palabra es mala e imprimir la censura, sino, imprime la palabra original."""
import time
Mensajes_Chat = ["hola", "noob", "genial", "manco"]

for Mensaje in Mensajes_Chat:
    if Mensaje == "noob" or Mensaje == "manco":
        time.sleep(0.5)
        print("[CENSURADO]")
        continue
    time.sleep(0.5)
    print(Mensaje)
    