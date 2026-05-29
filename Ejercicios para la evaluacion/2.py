flag = True
while flag:
    try:
        unidaes_disponibles_medicamento = int(input("Ingrese la cantidad de stock que hay para este medicamento: \n"))
        if unidaes_disponibles_medicamento <= 0 :
            print("Error, debe ingresar un número entero positivo sobre cero para el stock.")
        else:
            print(f"Stock registrado : {unidaes_disponibles_medicamento} unidades disponibles.")
            flag = False
    except ValueError:
        print("Error: Debe ingresar números enteros para el stock.")
