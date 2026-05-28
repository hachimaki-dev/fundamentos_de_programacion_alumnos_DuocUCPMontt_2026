cantidad_de_medicina = 0
while True:
    try:
        cantidad_de_medicina = int(input("ingrese la cantidad de medicina que hay de stock"))
        
        if cantidad_de_medicina > 0:
            print(f"Stock registrado: {cantidad_de_medicina}unidades disponibles.")
            break
        elif cantidad_de_medicina < 0:
            print("Dato inválido. Ingresa un entero positivo para el stock.")

      


    except ValueError:
        print("no se permiten fracciones ni letra")
