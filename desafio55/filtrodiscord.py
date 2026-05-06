#Crea un robot moderador de chat que censure insultos.

#Datos Iniciales: Tienes una lista de mensajes en el chat: `['hola', 'noob', 'genial', 'manco']`.

#Reglas de Negocio: El bot revisa las palabras una por una. Las palabras 'noob' y 'manco' están prohibidas. Si el bot ve una de esas palabras, debe cambiarla por el texto '[CENSURADO]'. Si la palabra es buena, la deja igual.

#Restricciones: Recorre la lista con un `for`. Adentro, usa un `if` para revisar si la palabra es mala e imprimir la censura, sino, imprime la palabra original.
mensajes = ["hola" , "noob" , "genial" , "manco"]
mensajes_malos = ["noob" , "manco"]
for mensaje in mensajes:
    if mensaje in mensajes_malos:
        print("censurado")
    else:
        print(mensaje)