chat = ["hola", "noob", "genial", "manco"]
ocultar = "CENSURADO"
#texto = "hola noob genial manco"
for palabra in chat:
    if (palabra == "noob") or (palabra == "manco"):
        palabra = palabra.replace("noob", ocultar)
        palabra = palabra.replace("manco", ocultar)
        print(palabra)
    else:
        print(palabra)