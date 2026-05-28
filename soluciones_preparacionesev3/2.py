while True:
    try:    
        cantidad_disponible_medicamento = int(input("ingrese las unidades disponibles de medicamento"))
        if cantidad_disponible_medicamento < 0:
            print("ingrese un numero mayor a 0")
            continue
        else:
             print(f"Stock registrado: {cantidad_disponible_medicamento} unidades disponibles.")
             break
    except:
        print("Dato inválido. Ingresa un entero positivo para el stock.")