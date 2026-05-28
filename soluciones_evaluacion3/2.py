while True:
    try:
        stock_medicamentos = int(input("Ingresa el stock de medicamentos: "))
        if stock_medicamentos > 0:
            print(f"Stock registrado: {stock_medicamentos} unidades disponibles.")
            break
        elif numero_pasajeros < 0:
            print("Dato invalido. Ingresa un entero positivo para el stock.")
    except:
        print("Dato invalido. Ingresa un entero positivo para el stock.")