#PENDIENTE

codigos_entrega_web = [200, 404, 500, 200, 500]

reintentos_maximos = 1

for codigo in codigos_entrega_web:

    if codigo == 200:
        print("OK")

    elif codigo == 404:
        print("No encontrado")

    elif codigo == 500 and reintentos_maximos < 1:
        print("Error del servidor, reintentando...")
        reintentos_maximos += 1

        if codigo == 500 and reintentos_maximos >= 1:
            print("Servidor Caido")
            break

    
   