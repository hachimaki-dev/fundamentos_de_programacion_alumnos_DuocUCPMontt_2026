codigos = [200, 404, 500, 200, 500]
reintento = 1
for codigo in codigos:
    if codigo == 200:
        print("Ok")
    elif codigo == 404:
        print("No encontrado")
    elif codigo == 500:
        if reintento > 0:
            reintento -= 1
            print("Reintentando")
        else:
            print("Servidor Caído")