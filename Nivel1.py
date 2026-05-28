while True:
    try:
        numero_ingresado = int(input("Ingresa un número: "))
        print(f"Número recibido {numero_ingresado}.")
        break
    except ValueError:
        print("ERROR, ingresa algo valido!")