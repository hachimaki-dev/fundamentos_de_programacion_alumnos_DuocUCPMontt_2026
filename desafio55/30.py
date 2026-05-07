respustas =[200, 404, 500, 200, 500]
reintentos = 1
for i in respustas:
    if i == 200:
        print("ok")
    elif i == 404:
        print("no encontrado")
    elif i == 500 and reintentos == 0:
        print("servidor caido")
        break
    elif i == 500:
        reintentos -= 1
        print("reintentando")