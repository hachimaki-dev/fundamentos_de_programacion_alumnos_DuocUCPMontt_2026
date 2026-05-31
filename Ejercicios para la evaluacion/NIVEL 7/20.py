equipos_disponibles = 60
capacidad_maxima = 60
historial = 0
while True:
    print("=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
    while True:
        try:
            eleccion_usuario = int(input("1. Ver equipos disponibles\n2. Prestamo de equipo\n3. Recibir devolución\n4. Ver historial de préstamos activos\n5. Salir\n===> "))
            if eleccion_usuario > 5 or eleccion_usuario < 1:
                print("Porfavor ingrese una opción válida.")
            else:
                break
        except ValueError:
            print("Porfavor ingrese números enteros que se ven en las opciones.")
    if eleccion_usuario == 1:
        print(f"Equipos disponibles : {equipos_disponibles}.")
    elif eleccion_usuario == 2:
        while True:
            try:
                prestamo_equipo = int(input("Cuantos equipos va a querer de prestamo? "))
                if prestamo_equipo <= 0:
                    print("ERROR, si va a querer un prestamo debe ingresar una cantidad válida.")
                    continue
                elif prestamo_equipo > equipos_disponibles:
                    print("ERROR, el prestamo no puede ser mayor al stock disponible.")
                    continue
                else:
                    equipos_disponibles -= prestamo_equipo
                    historial += prestamo_equipo
                    print(f"La cantidad de equipos prestados es de {prestamo_equipo}.")
                    break
            except ValueError:
                print("ERROR, debe ingresar numeros enteros para nosotros poder registrar el prestamo.")
    elif eleccion_usuario == 3:
        while True:
            try:
                devolucion_equipo = int(input("Cuantos equipos va a devolver? "))
                if devolucion_equipo <= 0:
                    print("ERROR, si va hacer devolucion, debe ingresar una cantidad válida.")
                    continue
                if devolucion_equipo <= historial:
                    print("No se pueden devolver más equipos de los que esten prestados.")
                    continue
                else:
                    equipos_disponibles += devolucion_equipo
                    historial -= devolucion_equipo
                    print(f"La cantidad de equipos devueltos es de {devolucion_equipo}.")
                    break
            except ValueError:
                print("ERROR, debe ingresar numeros enteros para nosotros poder registrar la devolucion.")
    elif eleccion_usuario == 4:
        print(f"Historial de prestamos activos: {historial}.")
    else:
        print("Gracias por utilizar el sistema, hasta pronto.")