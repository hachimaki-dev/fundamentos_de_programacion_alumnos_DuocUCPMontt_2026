mensajes_del_chat = ["Hola", "noob", "genial", "manco"]

for mensaje in mensajes_del_chat:
    if mensaje in ["noob", "manco"]:
        print("CENSURADO")
    else:
        print(mensaje)