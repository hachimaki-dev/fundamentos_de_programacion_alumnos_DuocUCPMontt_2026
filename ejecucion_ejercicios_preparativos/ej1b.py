while True:
    try:
        numero_pasajeros = int(input("¿Cuántos pasajeros hay abordo del avión el día de hoy? "))
        if numero_pasajeros > 0:
            print(f"Vuelo registrado con {numero_pasajeros} pasajeros en total, buen viaje.")
            break
        else:
             print("No pueden haber 0 o menos pasajeros en el vuelo, reintete.")
    except ValueError:
        print("Error: Ingrese un número entero positivo de pasajeros.")