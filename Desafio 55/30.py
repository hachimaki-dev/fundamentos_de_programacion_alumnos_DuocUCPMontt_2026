codigos = [200, 404, 500, 200, 500]

reintentos = 1

for codigo in codigos :
    match codigo :
        case 200 :
            print("Ok")
        case 404 :
            print("No encontrado")
        case 500 :
            if reintentos >= 1 :
                reintentos -= 1
                print("Reintentando")
            else :
                print("Servidor Caído")
                break