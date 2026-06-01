while True:
    
    try:
        cantidad_disponibles_medicamento = int(input("Ingrese la cantidad de stock del medicamento: "))

        if cantidad_disponibles_medicamento <= 0:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
            
        else:
            print(f"Stock registrado: {cantidad_disponibles_medicamento} unidades disponibles.")
            break
    
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock")