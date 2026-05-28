while True:
    try:
        cantidad = int(input("Ingrese la cantidad de unidades disponibles de un medicamento: "))
        if cantidad <= 0:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
        else:
            print(f"Stock registrado: {cantidad} unidades disponibles.")
            break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")