codigos_respuesta_web = [200, 404, 500, 200, 500]
reintento = 1
for i in codigos_respuesta_web:
    if i == 200:
        print("OK")
    elif i == 404:
        print("No encontrado.")
    elif i == 500:
        if reintento > 0:
            reintento-=1
            print("Reintentado.")
        else:
            print("Servidor Caído.")
            break