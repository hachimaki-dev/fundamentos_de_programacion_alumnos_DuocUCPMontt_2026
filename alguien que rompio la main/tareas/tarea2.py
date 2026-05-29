while True:
    try:
       numero_de_pasajeros = int(input("Ingrese el numero de pasajero: "))
       if numero_de_pasajeros <= 0:
            print("El numero debe ser un numero mayor a 0")
            continue       
    except ValueError:
        print("Ingresa un numero entero de pasajeros")
    else:
        print(f"vuelo registrado con {numero_de_pasajeros}")
        break
            