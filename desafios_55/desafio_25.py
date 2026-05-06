chat = ['hola', 'noob', 'genial', 'manco']

for palabras in chat:
    if palabras in ["noob", "manco"]:
        print("[CENSURADO]")

    else:
        print(palabras)