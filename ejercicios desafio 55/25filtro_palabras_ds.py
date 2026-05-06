mensajes = ["hola", "noob", "genial", "manco"]
for palabras in mensajes:
    if palabras in ["noob", "manco"]:
        print("CENSURADO")
    else:
        print(palabras)