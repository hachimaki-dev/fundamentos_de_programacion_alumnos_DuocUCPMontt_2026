while True:
    try:
        unidades = int(input("Ingrese cantidad de unidades: "))
        if unidades <= 0:
            print("El numero debe ser mayor a cero")
            continue
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
    else:
        print(f"Stock registrado: {unidades} unidades disponibles.")
        break
