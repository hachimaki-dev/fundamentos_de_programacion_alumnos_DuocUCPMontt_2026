lista_mensajes = ["hola", "noob", "genial", "manco"]

contador = 0
for i in lista_mensajes:
    
    if i == "noob" or i == "manco":
        lista_mensajes[contador] = "CENSURADO"

    contador += 1
print(lista_mensajes)