while True:
    try:
        cantidad_stock = int(input("Ingrese la cantidad de stock disponible: "))

        if cantidad_stock > 0:
            print(f"El stock dispnible es de {cantidad_stock} unidades.")
            break
        else:
            print("Ingresa stock mayor que 0.")
    except ValueError:
        print("Dato invalido!, Ingresa un entero positivo para el stock.")