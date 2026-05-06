mensajes = ["hola", "noob", "genial", "manco"]

contador = 0

for mensaje in mensajes:
    if mensaje == "genial" or mensaje == "manco":
        mensajes[contador] = "CENSURADO"

    contador = contador + 1 
print(mensajes)