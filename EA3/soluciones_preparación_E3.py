while True:
    try:
        numero = int(input("ingrese un numero"))
    except ValueError:
        print("error: eso no es un número entero")
    