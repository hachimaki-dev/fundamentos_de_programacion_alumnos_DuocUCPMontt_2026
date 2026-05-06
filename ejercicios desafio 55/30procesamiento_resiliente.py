codigos_de_respuesta_web = [200, 404, 500, 200, 500]
reintento_salvavidas = 1
for codigo in codigos_de_respuesta_web:
    if codigo == 200:
        print("OK")
    elif codigo == 404:
        print("no encontrado")
    if codigo == 500:
        if reintento_salvavidas > 0:
            reintento_salvavidas =- 1
            print("reintentando")
        else:
            print("servidor caido")
            break