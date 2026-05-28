while True:
    try:
        numero = int(input("Ingresa un numero: "))
        break
    except ValueError:
        print("ERROR: eso no es un numero entero mi pana")