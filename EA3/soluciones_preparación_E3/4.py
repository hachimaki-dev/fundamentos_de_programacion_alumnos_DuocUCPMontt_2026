while True:
    try:
        edad = int(input("Ingrese la edad del conductor: "))
        if edad > 0:
            print("Edad ingresada correctamente, tiene", {edad}, "años.")
            break
        else:           print("La edad debe ser un número positivo. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero para la edad.")