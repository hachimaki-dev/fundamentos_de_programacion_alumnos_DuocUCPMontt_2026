while True:
    try:
        unidades = int(input("Ingresa la cantidad de medicamentos: "))
        if unidades <= 0:
            print("Dato invalido, ingresa un numero entero positivo para el stock")
            continue
    except ValueError:
        print("Ingrese un numero entero.")
    else:
        print(F"Stock registrado: {unidades} de unidades disponibles")
        break

        
        
    
