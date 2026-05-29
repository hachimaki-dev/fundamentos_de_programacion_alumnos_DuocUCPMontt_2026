while True:
    try:
        unidades_medicamentos = int(input("Ingresa el numero de pasajeros:"))
            
        if unidades_medicamentos < 1:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
        else:
            print(f"Stock registrado: {unidades_medicamentos} unidades disponibles.")
            break
    except ValueError:
        print("ingresa un valor valido.")        


        
