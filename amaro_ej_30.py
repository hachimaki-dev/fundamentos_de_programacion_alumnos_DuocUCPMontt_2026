respuesta_web = [200, 404, 500, 200, 500]
reintento = 1

for codigos in respuesta_web:
    if codigos == 200:
        print("OK")
    if codigos == 404:
        print("No encontrado")
    if codigos == 500:
        reintento -= 1
        if reintento < 0:
            print("Servidor caído")
            break
        else:
            print("Reintentando")