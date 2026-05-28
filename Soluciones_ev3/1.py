while True:
    try:
        numero = int(input("Ingrese un numero: "))
        print(f"Número recibido: {numero}")
        break
    except ValueError:
        print("Error: eso no es un número entero.")


