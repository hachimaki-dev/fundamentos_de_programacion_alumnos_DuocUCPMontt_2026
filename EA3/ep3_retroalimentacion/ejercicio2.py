habitaciones_disponibles = 50
historial_neto = 0
capacidad_maxima = 50
elecciones_posibles = [1,2,3,4,5]
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")
while True:
    try:
        eleccion_usuario = int(input(": "))
        if eleccion_usuario in elecciones_posibles:
            break
        else:
            print("Opcion no valida. por favor selecciona una opccion del 1 al 5")
    except ValueError:
        print("Tiene que ser un numero del 1 al 5")
    if eleccion_usuario == 1:
        print(f"La cantidad de habitaciones disponibles es de {habitaciones_disponibles}")
    elif eleccion_usuario == 2:
        while True:
            try:
                print("Si desea salir ingrese 0")
                check_in = int(input("Ingrese la cantidad de habitaciones a registrar: "))
                if check_in == 0:
                    break
                if check_in > 0:
                    if check_in > habitaciones_disponibles:
                        print(f"La cantidad de habitaciones disponibles es menor que las habitaciones a registrar. Habitaciones disponibles: {habitaciones_disponibles}")
                    else:
                        print(f"Habitaciones registradas: {check_in}")
                        break
                else:
                    print("El valor tiene que ser mayor que cero")
            except ValueError:
                print("El valor tiene que ser un numero")
        habitaciones_disponibles -= check_in
        historial_neto += check_in
        print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}")
    elif eleccion_usuario == 3:
        while True:
            try:
                print("Si desea salir ingrese 0")
                check_out = int(input("Ingrese la cantidad de habitaciones a liberar: "))
                if check_out == 0:
                    break
                if check_out > 0:
                    if check_out > capacidad_maxima - habitaciones_disponibles:
                        print(f"La cantidad de habitaciones ocupadas es menor que las habitaciones a liberar. Habitaciones ocupadas: {capacidad_maxima - habitaciones_disponibles}")
                    else:
                        print(f"Habitaciones liberadas: {check_out}")
                        break
                else:
                    print("El valor tiene que ser mayor que cero")
            except ValueError:
                print("El valor tiene que ser un numero")
        habitaciones_disponibles += check_out
        historial_neto -= check_out
        print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}")
    elif eleccion_usuario == 4:
        print(f"La cantidad de habitaciones actualmente ocupadas es de: {capacidad_maxima -habitaciones_disponibles}")
    elif eleccion_usuario == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima")
        break
