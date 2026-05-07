mensajes_chat = ["Hola", "Noob", "genial", "Manco"]
for palabras in mensajes_chat:
    if palabras in ["Noob", "Manco"]:
        print("[CENSURADO]")
    else:
        print(palabras)