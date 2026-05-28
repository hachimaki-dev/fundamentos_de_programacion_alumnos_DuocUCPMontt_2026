while True:
    try:
        numero_ingresado = int(input("Ingrese un número entero "))
        print(f"Número Recibido: {numero_ingresado}")
        break
    except ValueError:
        print("Este número NO es entero, ingrese un número válido")
