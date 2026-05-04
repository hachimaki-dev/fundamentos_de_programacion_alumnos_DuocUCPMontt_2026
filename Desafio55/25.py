mensajes = ['hola', 'noob', 'genial', 'manco']

for mensaje in mensajes:
    if mensaje in ["noob", "manco"]:
        print("[CENSURADO]")
    else:
        print(mensaje)