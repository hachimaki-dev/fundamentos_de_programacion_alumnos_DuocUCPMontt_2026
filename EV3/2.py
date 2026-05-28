error = True
while error:
    try:
        cant_medicamentos = int(input("Ingrese la cantidad del medicamento: "))
        error = False
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")

    if not error:
        if cant_medicamentos > 0:
            print(f"Stock registrado: {cant_medicamentos} unidades disponibles.")
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
            error = True