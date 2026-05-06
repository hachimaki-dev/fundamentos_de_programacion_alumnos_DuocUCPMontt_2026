mensajes_en_chat = ["hola", "noob", "genial", "manco"]

for i in mensajes_en_chat:
    if i in [ "noob", "manco" ]:
        i = "[CENSURADO]"
        print(i)
    else:
        print(i)
