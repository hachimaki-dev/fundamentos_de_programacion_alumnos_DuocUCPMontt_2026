palabras = ["hola", "noob", "genial", "manco"]
for palabra in palabras:
    if palabra == "noob" or palabra == "manco":
        print("CENSURADO")
    else:
        print(palabra)