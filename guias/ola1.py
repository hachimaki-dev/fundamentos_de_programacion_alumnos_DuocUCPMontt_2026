while True:
    try:
        numero = int(input("Ingrese su numero: "))
        break
    except ValueError:
        print("Error: Eso no es un numero entero.")
