
habitaciones = 50

while True:
    
    print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
    print(" === MENÚ PRINCIPAL ===")
    print("que opcion le gustario ver")

    print(" 1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    
    
    opcion = int(input("que opcion quieres ver?: "))
    
    
    if opcion == 1:
        print(f"actualmente hay {habitaciones} habitaciones disponibles")
        
    elif opcion == 2:
        while True:
            try:
                habitaciones_disponible = int(input("cuantas habitaciones quiere reservar?: "))
                if habitaciones_disponible > 0 and habitaciones_disponible <= 50:
                    habitaciones -= habitaciones_disponible
                    print(f"check-in realizado, se han reservado {habitaciones_disponible} habitaciones")
                    print(f"habitaciones disponibles ahora: {habitaciones}")
                    break
                elif habitaciones_disponible == 0:
                    print("Valor inválido. Debes ingresar un número entero mayor a 0.")
                else:
                    print("No hay suficientes habitaciones disponibles. Solo quedan 50.")
            except ValueError:
                print("No hay suficientes habitaciones disponibles. Solo quedan 50.")
                
    elif opcion == 3:
                
        while True:
            try:
                habilitar_habitacion = int(input("cuantas habitaciones quiere liberar?: "))
                if habilitar_habitacion > 0 and habilitar_habitacion <= 50:
                    habitaciones += habilitar_habitacion
                    print(f"check-out realizado, se han liberado {habilitar_habitacion} habitaciones")
                    
                    print(f"habitaciones disponibles ahora: {habitaciones}")
                    break
                else:
                    print(" No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel (50 habitaciones)")
            except ValueError:
                print(" No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel (50 habitaciones)")
    elif opcion == 4:
        
        historial = habitaciones_disponible - habilitar_habitacion
        print("este es tu historial:")
        print(f"se han reservado {habitaciones_disponible} habitaciones")
        print(f"se han cancelado {habilitar_habitacion} habitaciones")
        print(f" Historial neto de ocupaciones en esta sesión: {historial} habitaciones")
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("opcion invalida, por favor seleccione una opcion del 1 al 5")
