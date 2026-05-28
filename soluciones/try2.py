pasajero = 0
while True:
    try:
        pasajero = int(input("ingrese numero de pasajeros: "))
        
        if pasajero > 0:
            print(f"Vuelo registrado con {pasajero} pasajeros")
            break
        elif pasajero < 0:
            print("Error: ingresa un número entero positivo de pasajeros.")

      


    except ValueError:
        print("no se permiten fracciones ni letra")
