while True:
    try:
        numero = int(input("escriba un numero entero"))
        break
    except ValueError:
        print("Error: eso no es un número entero.")