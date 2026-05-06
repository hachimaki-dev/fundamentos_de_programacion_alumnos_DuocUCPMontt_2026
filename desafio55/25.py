mensajes = ["hola","noob","genial","manco"] 
contador = 0
for i in mensajes:
    if "noob" or "manco":
        mensajes[contador] = "censurado"
    contador += 1
print(mensajes)
