mensajes_chat = ["hola", "noob", "genial", "manco"]
palabras_prohibidas = ["noob", "manco"]
for palabra in mensajes_chat:
    if palabra in palabras_prohibidas:
        print("CENSURADO")
    else:
        print(palabra)