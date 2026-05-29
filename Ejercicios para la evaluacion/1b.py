continuar = True
while continuar:
    try:
        pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
        if pasajeros > 0:
            print(f"La cantidad de pasajeros que hay es de {pasajeros}.")
            continuar = False
        else:
            print("¡Error! Ingrese un número entero positivo de pasajeros.")
    except ValueError:
        print("¡Error! Debe ingresar números enteros.")