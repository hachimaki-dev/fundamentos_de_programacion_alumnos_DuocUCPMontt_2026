lista_de_codigos=[200, 404, 500, 200, 500]
reintentos=1
for n in lista_de_codigos:
    if n==200:
        print("Ok")
    elif n==404:
        print("No encontrado")
    elif n==500:
        if reintentos>=1:
            reintentos-=1
            print("Reintentando")
        else:
            print("Servidor Caído")
