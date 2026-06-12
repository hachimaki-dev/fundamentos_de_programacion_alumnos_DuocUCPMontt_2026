while True:
    
    try:
        cantidad_medicamentos = int(input("ingrese la cantidad disponible de medicamentos:"))
        if cantidad_medicamentos > 0:
            break
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
    
print("stock registrado:", cantidad_medicamentos, "medicamentos disponibles")

