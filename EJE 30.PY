codigos = [200, 404, 500, 200, 500]
reintentos = 1
 
for codigo in codigos:
    if codigo == 200:
        print("Ok")
    elif codigo == 404:
        print("No encontrado")
    elif codigo == 500:
        if reintentos > 0:
            print("Reintentando")
            reintentos -= 1
        else:
            print("Servidor Caido")
            break
 
print()
 
 