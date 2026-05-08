chat_sucio = ["hola" , "noob" , "genial" , "manco"]
contador = 0

for i in chat_sucio:
    if i == "noob" or i == "manco":
        chat_sucio[contador] = "CENSURADO"
    
    contador = contador + 1
    
print(chat_sucio)