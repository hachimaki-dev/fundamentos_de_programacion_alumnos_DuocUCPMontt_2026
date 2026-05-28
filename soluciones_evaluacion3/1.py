while True:
    try:
        numero_ingresado = int(input("ingresa un numero: "))
        break
    except ValueError:
        print("Error: eso no es un numero entero")