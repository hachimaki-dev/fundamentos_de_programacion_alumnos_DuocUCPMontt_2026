habitaciones_disponibles = 50
capacidad_habitaciones = 50 
ocupaciones = 0

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")

while True:
    try:
        print("=== MENÚ PRINCIPAL === \n1) Habitaciones disponibles \n2)Realizar Check-in \n3)Realizar Check-out \n4)Historial de ocupaciones \n5)Salir")
        eleccion = int(input("Eliga su opción: "))
        if eleccion <= 0 or eleccion > 5:
            print("Opción invalida, vuelta a intenarlo")
        
    except ValueError:
        print("Solo puede ingresar numeros enteros.")
    
    if eleccion == 1:
        print(f"Las habitaciones disponibles en este momento son {habitaciones_disponibles}")
        
    elif eleccion == 2:
        while True:
            try:
                reservar_habitacion = int(input("¿Cuantas habitaciones desea reservar?: "))
                if reservar_habitacion > 0:
                    if reservar_habitacion > habitaciones_disponibles:
                        print("No hay suficientes habitaciones disponibles.")
                    else:
                        print(f"Check-in realizado. se reservaron {reservar_habitacion} habitaciones.")
                        break
                else:
                    print("No puedes asignar habitaciones con numeros negativos.")
            except ValueError:
                print("Solo puedes ingresar numeros enteros.")
        
        habitaciones_disponibles -= reservar_habitacion
        ocupaciones += reservar_habitacion
        print(f"Actualmente hay {habitaciones_disponibles} Habitaciones disponibles")
        
    elif eleccion == 3:
        while True:
            try:
                liberar_habitaciones = int(input("¿Cuantas habitaciones desea liberar?"))
                if liberar_habitaciones > 0:
                    if liberar_habitaciones > capacidad_habitaciones - habitaciones_disponibles:
                        print("Supera el limite.")
                    else:
                        print(f"Check-out realizado. Se liberaron {liberar_habitaciones} Habitaciones.")
                        break
                else:
                    print("No puedes asignar habitaciones con numeros negativos.")
            except ValueError:
                print("Solo puedes ingresar numeros enteros.")
        
        habitaciones_disponibles += liberar_habitaciones
        ocupaciones -= liberar_habitaciones
        print(f"Habitaciones disponibles ahora {habitaciones_disponibles}")
        
    elif eleccion == 4:
        print(f"Historial neto de ocupaciones en esta sesión: {ocupaciones}")
        
    elif eleccion == 5:
        print("Gracias")
        break