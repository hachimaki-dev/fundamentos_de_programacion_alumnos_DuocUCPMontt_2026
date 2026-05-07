Lista_Web = [200, 404, 500, 200, 500]
reintentos = 1

for i in Lista_Web:
    
    if i == 200:
        print ("OK")

    
    elif i == 404:
        print ("No Encontrado")


    elif i == 500:
        reintentos -= 1
        print ("Error, reintentado.")
        print (f"Tienes {reintentos} reintetos disponible")

        if reintentos == 0:
            break

print ("PROGRAMA CAIDO")
