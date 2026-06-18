def solicitar_cantidad_de_ingenieros():
    while True:
        try:
            cantidad_de_ingenieros = int(input("Ingrese la cantidad de ingenieros: "))

            if cantidad_de_ingenieros > 0:
                return cantidad_de_ingenieros
            else:
                print("Ingrese un numero mayor")