palabras = ["hola", "noob", "genial", "manco"]

for i in range(len(palabras)):
    if palabras[i] in ["noob", "manco"]:
        palabras[i] = "[CENSURADO]"
    print(palabras[i])
