while True:
    try:
        cantidad_de_unidades = int(input("Ingrese stock: "))
        if cantidad_de_unidades <= 0:
            print("Stock debe ser mayor a cero")
            continue
        else:
            print(f"Stock registrado: {cantidad_de_unidades} unidades disponibles.")
            break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock")
    