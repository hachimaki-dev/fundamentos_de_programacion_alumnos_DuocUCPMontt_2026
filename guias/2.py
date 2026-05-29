while True :

    try :

        cantidad_medicamentos_unidades = int(input("ingrese su cantidad de medicamentos: "))

        if cantidad_medicamentos_unidades < 1 :
            print("Ingrese un numero mayor a 0")
            continue
        else: 
            print(f"Stock registrado: {cantidad_medicamentos_unidades} unidades disponibles")

    except ValueError :
        print("Error: ingrese un numero entero positivo")
        
