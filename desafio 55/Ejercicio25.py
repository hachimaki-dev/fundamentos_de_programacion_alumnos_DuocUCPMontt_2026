chat = ["hola", "noob", "genial", "manco"]
for i in range(len(chat)):
    print(chat[i])
    if chat[i] == "noob" or chat[i] == "manco":
        chat[i] = "CENSURADO"

print(chat)