codigos_web = [200, 404, 500, 200, 500]
reintentos = 1
for codigo in codigos_web:
    if codigo == 200:
        print("Ok")
    elif codigo == 404:
        print("No encontrado")
    elif codigo == 500:
        reintentos -= 1
        if reintentos < 0:
            print("Servidor Caido")
            break
        print("Reintentando")