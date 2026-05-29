while True:
    try:
        cantidad_unidades = int(input('Ingrese la cantidad de unidades disponibles del medicamento: '))
        if cantidad_unidades > 0:
            break
        else:
            print('Dato inválido. Ingresa un entero positivo para el stock.')
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
print(f'Stock registrado: {cantidad_unidades} unidades disponibles.')            