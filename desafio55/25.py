lista_de_mensajes = ["hola", "noob" , "genial", "manco"]
contador = 0
for mensaje in lista_de_mensajes:
    if mensaje == "noob" or mensaje == "manco":
        lista_de_mensajes[contador] = "CENSURADO"
    contador +=1
    
print(lista_de_mensajes)