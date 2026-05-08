respuestas = [200, 404, 500, 200, 500]
contador = 1

for respuesta in respuestas:
    if respuesta in [200]:
        print("Ok")

    elif respuesta in [404]:
        print("No encontrado")

    elif respuesta in [500]:
        contador = contador - 1

        if contador < 0:
            print("servidor Caído")
            break

        else:
            print("Reintentando") 
        
    
