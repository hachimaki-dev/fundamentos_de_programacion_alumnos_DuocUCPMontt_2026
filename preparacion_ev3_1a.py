while True:
    try:
        numero_entero = int(input("Ingrese un número entero: "))
        print(f"Número recibido: {numero_entero}")
        break
    except ValueError:
        print("Error, eso no es un número entero")