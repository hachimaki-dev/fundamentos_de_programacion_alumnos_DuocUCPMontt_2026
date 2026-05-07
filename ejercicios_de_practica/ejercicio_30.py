codigos_de_respuesta = [200, 404, 500, 200, 500]
reintentos = 1

for respuestas in codigos_de_respuesta:
    if respuestas == 200:
        print("Ok")
        continue
    elif respuestas == 404:
        print("No Encontrado")
        continue
    elif respuestas == 500 and reintentos != 0:
        print("Reintentado")
        reintentos -= 1
        continue
    elif reintentos == 0:
        print("Servidor Caido")
        break