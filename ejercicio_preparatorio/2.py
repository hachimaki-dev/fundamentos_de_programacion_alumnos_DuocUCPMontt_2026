while True:
    try:
        cantidad = int(input("Ingresa la cantidad de unidades disponibles: "))
        
        if cantidad > 0:
            print(f"Stock registrado: {cantidad} unidades disponibles.")
            break
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
            
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")