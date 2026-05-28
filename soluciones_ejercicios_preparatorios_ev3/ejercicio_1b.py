while True:
    try:
        numero_de_pasajeros = int(input("Ingrese el numero de pasajeros de este vuelo: "))
        if numero_de_pasajeros <= 0:
            continue
        else:
            print(f"Excelente registrando {numero_de_pasajeros} pasajeros en este vuelo")
            break
    except ValueError:
        print("ERROR: ingrese un número entero positivo de pasajeros")