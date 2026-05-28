while True:
    try:
        stock_farmacia=int(input("Ingrese el stock de medicamentos en farmacia: "))
        if stock_farmacia>0:
            print(f"Stock registrado: {stock_farmacia} unidades disponibles.")
            break
        elif stock_farmacia<0:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
    except:
        print("Dato inválido. Ingresa un entero positivo para el stock.")