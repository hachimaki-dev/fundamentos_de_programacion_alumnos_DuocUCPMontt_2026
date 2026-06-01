while True:
    try:
        pasajeros = int(input("ingrese la cantidad de pasajeros: "))
        
    except ValueError:
        print("Solo puede añadir numeros enteros")
        
    except: 
        print("El numero de pasajeros no puede ser 0")
        
    else:
        print(f"Vuelo registrado con {pasajeros}pasajeros")
        break
        