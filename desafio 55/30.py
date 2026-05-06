codigos = [200, 404, 500, 200, 500]
reintentos = 1

for estado in codigos:
    if estado == 200:
        print("Ok")
    elif estado == 404:
        print("No encontrado")
    elif estado == 500:
        if reintentos > 0:
            reintentos -= 1
            print("Reintentando")
        else:
            print("Servidor Caído")
            break
