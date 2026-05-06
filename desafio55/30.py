codigos_de_respuesta = [ 200, 404, 500, 200, 500 ]
reintentos = 1

for i in codigos_de_respuesta:
    if i == 200:
        print("Ok")
    elif i == 404:
        print("No encontrado")
    elif i == 500:
        if reintentos > 0:
            reintentos = reintentos - 1
            print("Reintentando")
        else:
            print("Servidor caído")
            break
    else:
        pass
