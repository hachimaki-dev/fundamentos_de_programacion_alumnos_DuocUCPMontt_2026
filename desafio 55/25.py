chat = ["hola", "noob", "genial", "manco"]
censura = ["noob", "manco"]

for palabra in chat:
    if palabra in censura:
        print("CENSURADO")
    else:
        print(palabra)