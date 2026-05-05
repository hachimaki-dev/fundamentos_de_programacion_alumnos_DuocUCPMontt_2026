respuestas = [200, 404, 500, 200, 500]
reintento = 1

for respuesta in respuestas:
    if respuesta == 200:
        print("Ok")
    elif respuesta == 404:
        print("No encontrado")
    elif reintento > 0:
        reintento -= 1
        print("Reintentando")
    else:
        print("Servidor caido")