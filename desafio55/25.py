mensajes_chat = ['hola', 'noob', 'genial', 'manco']
for mensaje in mensajes_chat:
    if mensaje in ["noob", "manco"]:
        print("[CENSURADO]")
    else:
        print(mensaje)
