codigos_de_respuesta = [200, 404, 500, 200, 500]
reintentos = 2

for respuestas in codigos_de_respuesta:
        if respuestas == 200:
            print("OK")
        elif respuestas == 404:
            print("No encontrado")
        elif respuestas == 500:
            reintentos -= 1 
            if reintentos == 0:
                print("servidor caido")
            else:
                print("Reitentando")