lista_de_mensajes = ["hola", "noob" , "genial", "manco"]
for mensaje in lista_de_mensajes:
    if mensaje == "noob":
        lista_de_mensajes.remove("noob")
        lista_de_mensajes.insert(1,"CENSURADO")
    elif mensaje == "manco":
        lista_de_mensajes.remove("manco")
        lista_de_mensajes.insert(3, "CENSURADO")
        
print(lista_de_mensajes)