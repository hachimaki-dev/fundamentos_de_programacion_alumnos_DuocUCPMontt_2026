while True:
    try:
        numero_pasajero = int(input("Ingresa el numero de pasajeros:"))
            
        if numero_pasajero < 1:
            print("Error: ingresa un número entero positivo de pasajeros.")
            continue
        else:
            print(f"Vuelo registrado con {numero_pasajero} pasajeros.")
            break
    except ValueError:
        print("ingresa un valor valido.")


            

