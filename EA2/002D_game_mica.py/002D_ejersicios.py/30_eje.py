
web = [200, 404, 500, 200, 500]
reintento = 1

for respuesta in web:
    if respuesta == 200:
        print("ok")
    elif respuesta == 404:
        print("No encontrado")
    elif respuesta == 500:
        reintento -=1
        if reintento < 0:
            print("servidor caido")
            break
        print("reintentando")