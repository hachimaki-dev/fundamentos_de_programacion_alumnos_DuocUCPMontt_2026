respuesta_web = [200, 404, 500, 200, 500]
salvavidas = 1

for i in respuesta_web:
    if i == 200:
        print("Ok")
    elif i == 404:
        print("No encontrado")
    elif i == 500:
        if salvavidas >= 1:
            print("Reintentando")
            salvavidas -= 1
        else:
            print("Servidor caido")
            break
        