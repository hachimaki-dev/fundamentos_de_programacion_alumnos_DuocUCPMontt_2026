códigos_respuesta_web = [200, 404, 500, 200, 500]
reintento_salvavidas = 1
contador = 0
for i in códigos_respuesta_web:
    if i == 200:
        print("OK")
    elif i == 404:
        print("No encontrado")
    else:
        print("FATAL ERROR")
        if reintento_salvavidas >= 1:
            print("reintentando...")
            reintento_salvavidas -= 1
        else:
            print("SERVIDOR CAÍDO")
            break
    