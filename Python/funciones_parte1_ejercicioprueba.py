def menu():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Habitaciones disponibles")
        print("2. Realizar check-in")
        print("3. Realizar check-out")
        print("4. Historial de ocupaciones")
        print("5. Salir")

habitaciones_disponibles = 50

habitaciones_ocupadas = 0

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")



menu()
opcion_elegida_por_el_usuario = input("Ingrese su opción")
if opcion_elegida_por_el_usuario == "1":
    print(f"Actualmente hay {habitaciones_disponibles} habitaciones disponibles")
elif opcion_elegida_por_el_usuario == "2":
    while True:
        try:
            cantidad_de_habitaciones_a_reservar = int(input("¿Cuántas habitaciones deseas reservar?"))
            if cantidad_de_habitaciones_a_reservar > 0:
                break
            else:
                print("Ingrese un número posito")
            except ValueError:
                print("Ingresé un número entero valido superior a 0")
    if habitaciones_disponibles >= cantidad_de_habitaciones_a_reservar :
        #Si puede reservar
        habitaciones_disponibles -= cantidad_de_habitaciones_a_reservar
        habitaciones_ocupadas += cantidad_de_habitaciones_a_reservar
    else:
        print("No puedes reservar una cantidad de habitaciones superior a las disponibles")
    elif opcion_elegida_por_el_usuario == "3":
        while True:
            try:
                cantidad_de_habitaciones_a_liberar = int(input("¿Cuántas habitaciones deseas liberar?"))
                if cantidad_de_habitaciones_a_liberar > 0:
                    break
                else:
                    print("Ingrese un número posito")
            except ValueError:
                print("Ingresé un número entero valido superior a 0")
            
        if cantidad_de_habitaciones_a_liberar <= habitaciones_ocupadas :
            #Si puede liberar
            habitaciones_disponibles += cantidad_de_habitaciones_a_reservar
            habitaciones_ocupadas -= cantidad_de_habitaciones_a_reservar
        else:
            print("No puedes liberar una cantidad de habitaciones superior a las ocupadas")
    elif opcion_elegida_por_el_usuario == "4":
        print(f"Historial neto de ocupaciones en esta sesión: {habitaciones_ocupadas} habitaciones ocupadas.")
    elif opcion_elegida_por_el_usuario == "5":
        print("Saliendo del programa. Gracias por usarnos, regrese pronto <3")
        break
    else:
    print("Ingrese una opción valida")