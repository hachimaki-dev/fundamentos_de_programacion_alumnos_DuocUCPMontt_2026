while True:
    try:
        medicamentos = int(input("Ingresa la cantidad de unidades disponibles del medicamento: "))
        
        if medicamentos > 0:
            print(print(f"Stock registrado: {medicamentos} unidades disponibles."))
            break
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")

    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
