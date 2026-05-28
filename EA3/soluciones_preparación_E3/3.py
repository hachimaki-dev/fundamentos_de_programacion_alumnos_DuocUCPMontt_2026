while True:
    try:
        
        entrada = input("Ingresa la cantidad de unidades: ")
        cantidad = int(entrada) 

        
        if cantidad > 0:
            print(f"Stock registrado: {cantidad} unidades disponibles.")
            break 
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")

    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
        
