mensajes = ["hola", "noob", "genial", "manco"]
insultos = ["noob", "manco"]

for mensaje in mensajes :
    palabra_censurada = False

    for insulto in insultos :
        if mensaje == insulto :
            palabra_censurada = True
            break

    if palabra_censurada :
        print("[CENSURADO]")
    else :
        print(mensaje)