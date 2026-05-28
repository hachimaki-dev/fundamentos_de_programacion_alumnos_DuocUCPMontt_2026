while True:
    try:
        numero = int(input("Ingresa un numero: "))
        #esta parte es lo que se ejecuta cuando el usuario ingresa un valor válido:
        break
    except ValueError:
        print("ERROR: eso no es un numero entero mi pana")