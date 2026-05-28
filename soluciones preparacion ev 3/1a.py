while True :
    try :
        numero = int(input("Ingrese un número: "))
        break
    except ValueError :
        print("Error. eso no es un número entero")

print(f"Número recibido: {numero}")