while True:
    entrada = input("Ingresa el número de pasajeros: ")
    
    try:
        pasajeros = int(entrada)
        
        
        if pasajeros > 0:
            print(f"Vuelo registrado con {pasajeros} pasajeros.")
            break
        else:
            print("Error: ingresa un número entero positivo de pasajeros.")
            
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
