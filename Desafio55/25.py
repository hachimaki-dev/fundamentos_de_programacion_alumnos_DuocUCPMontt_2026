mensajes_del_chat=["hola", "noob", "genial", "manco"]
contador=0
for x in mensajes_del_chat:
    if x=="noob" or x=="manco":
        mensajes_del_chat[contador]=["CENSURADO"]
    contador+=1
print(mensajes_del_chat)