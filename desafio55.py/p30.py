respuestas = [200, 404, 500, 200, 500]
reintentos = 1

for codigo in respuestas:
    if codigo == 200:
        print("Ok")
    elif codigo == 404:
        print("No encontrado")
    elif codigo == 500:
        reintentos = reintentos - 1
        if reintentos < 0:
            print("Servidor caído")
            break
        print("Reintentando")