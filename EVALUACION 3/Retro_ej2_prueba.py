habitaciones_disponibles = 50
habitaciones_ocupadas = 0

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    opcion_menu = input("Porfavor ingrese una opción: ")

    if opcion_menu == "1":
        #Habitaciones disponibles
        print(f"Actualmente hay {habitaciones_disponibles} habitaciones disponibles.")

    elif opcion_menu == "2":
        #check in
        while True
            try:
                cantidad_de_habitaciones_a_reservar = int(input("¿Cuántas habitaciones deseas reservar?"))
                break
            except ValueError:
                print("Ingrese una cantidad válida.")

        if habitaciones_disponibles > 0  and cantidad_de_habitaciones_a_reservar <= habitaciones_disponibles:
            habitaciones_disponibles -= cantidad_de_habitaciones_a_reservar
            #Esta variable es para abastecer la pción 4
            habitaciones_ocupadas += cantidad_de_habitaciones_a_reservar
            print(f"Check-in realizado. Se reservaron {cantidad_de_habitaciones_a_reservar} habitaciones.")
            print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}")
        
        else:
            print("HAGALO BIEN!")

    elif opcion_menu == "3":
        #checkout
        while True
            try:
                cantidad_de_habitaciones_a_liberar = int(input("¿Cuántas habitaciones deseas liberar?"))
                break
            except ValueError:
                print("Ingrese una cantidad válida.")

        if habitaciones_ocupadas > 0  and cantidad_de_habitaciones_a_liberar <= habitaciones_ocupadas:
            habitaciones_disponibles += cantidad_de_habitaciones_a_liberar
            habitaciones_ocupadas -= cantidad_de_habitaciones_a_liberar
            print(f"Check-out realizado. Se liberaron {cantidad_de_habitaciones_a_liberar} habitaciones.")
            print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}")
        else:
            print("HAGALO BIEN!")

    elif opcion_menu == "4":
        print(f"Actualmente hay {habitaciones_ocupadas} habitaciones ocupadas.")
    
    elif opcion_menu == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("Intentelo nuevamente")
