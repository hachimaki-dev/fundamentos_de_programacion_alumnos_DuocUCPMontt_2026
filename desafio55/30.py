codigos = [200 , 404, 500,200,500]
salvavidas = 1 
for numeros in codigos:
    if numeros == 200:
        print("OK")
    elif numeros == 404:
        print("No encontrado")
    elif numeros == 500:
        salvavidas -= 1
        if salvavidas < 0:
            print("Servidor caido")
            break
        else:
            print("Reintentando")
        