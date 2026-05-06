mensajes_chat= ['hola', 'noob', 'genial', 'manco']

for palabra in mensajes_chat:
    if palabra in ['noob', 'manco']:
        print("[CENSURADO]")
    else:
        print(palabra)