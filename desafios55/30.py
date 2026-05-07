codigos = [200, 404, 500, 200, 500]
reintentos = 1
for codigo in codigos:
    if codigo == 200:
        print("OK")
    elif codigo == 400:
        print("No encontrado")
    elif codigo == 500:
        reintentos -= 1
        if reintentos >= 0:
            print("reintentando")
        else:
            print("Servidor caído")
            break