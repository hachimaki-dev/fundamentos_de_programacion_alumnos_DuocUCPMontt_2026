mensajes = ["hola","noob","genial","manco"]
contador = 0
for i in mensajes:
    
    if i == "noob" or i == "manco":
        mensajes[contador] = "CENSURADO"
    contador = contador + 1
  

print(mensajes)