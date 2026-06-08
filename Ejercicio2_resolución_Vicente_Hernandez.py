habitaciones_disponibles = 50
historial_de_ocupaciones = 0
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")


    eleccion_del_usuario = input("Ingrese una de la opciones para continuar: ")

    if eleccion_del_usuario == "1":
        print(f"Hay disponibles {habitaciones_disponibles} habitaciones")    
    elif eleccion_del_usuario == "2":
        while True:
            try:
                if habitaciones_disponibles == 0:
                    print("No hay habitaciones disponibles")
                    break
                else:
                    reserva_de_habitacion = int(input("Ingrese la cantidad de habitaciones que reservara: "))
                    if 0 < reserva_de_habitacion <= habitaciones_disponibles:
                    
                        habitaciones_disponibles -= reserva_de_habitacion
                        historial_de_ocupaciones += reserva_de_habitacion
                        if reserva_de_habitacion == 1:
                            print("Se a reservado una habitacion")
                        else:
                            print(f"Se han reservado {reserva_de_habitacion} habitaciones")
                        break
                    elif reserva_de_habitacion <= 0:
                        print("Ingrese una cantidad valida de habitaciones ha solicitar")
                    else:
                        print(f"No hay suficientes habitaciones disponibles. Solo quedan {habitaciones_disponibles}.")
            except ValueError:
                print("Ingrese una cantidad valida de habitaciones ha solicitar")
    elif eleccion_del_usuario == "3":
        while True:
            try:
                if historial_de_ocupaciones == 0:
                    print("No hay habitaciones ocupadas")
                    break
                else:
                    liberacion_de_habitaciones_del_usuario = int(input("Ingrese la cantidad de habitaciones que desocupara: "))
                    if 0 < liberacion_de_habitaciones_del_usuario <= historial_de_ocupaciones:
                        habitaciones_disponibles += liberacion_de_habitaciones_del_usuario
                        historial_de_ocupaciones -= liberacion_de_habitaciones_del_usuario
                        if liberacion_de_habitaciones_del_usuario == 1:
                            print("Se a liberado una habitacion")
                        else:
                            print(f"Se han liberado {liberacion_de_habitaciones_del_usuario}")
                        break
                    elif liberacion_de_habitaciones_del_usuario <= 0:
                        print("Ingrese una cantidad valida de habitaciones ha liberar")
                    else:
                        print("No puedes liberar esa cantidad. Superarías las reservas actuales")
            except ValueError:
                print("Ingrese una cantidad valida de habitaciones ha liberar")
    elif eleccion_del_usuario == "4":
        print(f"Han sido ocuapadas {historial_de_ocupaciones} habitaciones")
    elif eleccion_del_usuario == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("Ingrese un numero entero positivo de los que se muestran en pantalla")