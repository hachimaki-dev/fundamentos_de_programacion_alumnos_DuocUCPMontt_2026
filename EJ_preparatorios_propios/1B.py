#EJERCICIO 1B

while True:
    try:
        pasajeros_registrados = int(input("Ingrese cuantos pasajeros van a ser registrados en este viaje : "))
        if pasajeros_registrados <= 0:
            print("Error : ingrese un numero entero positivo de pasajeros ")
            continue
        else:    
            print(f"Vuelo registrado  con {pasajeros_registrados}  pasajeros")
            break
    except ValueError:
        print("Error : ingrese un numero entero positivo de pasajeros ")
