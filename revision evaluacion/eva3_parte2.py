habitaciones_disponibles_para_los_visitantes = 50
habitaciones_ocupadas_por_visitantes = 0

print("====================================================================")
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
print("====================================================================")

while True:

    print("=== MÉNU PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-ouk")
    print("4. Historial de ocupaciones")
    print("5. Salida")

    opcion_elegida_por_el_usuario = (input("Ingrese su opcion por favor:"))

    if opcion_elegida_por_el_usuario == "1":
        print(f"Actualmente hay {habitaciones_disponibles_para_los_visitantes} habitaciones dispoibles para los visitantes.")
    
    elif opcion_elegida_por_el_usuario == "2":

        while True:
            try:
                cantidad_de_habiotaciones_a_reservar = int(input("Ingrese el numero de habitacion que desea reservar: "))
                if cantidad_de_habiotaciones_a_reservar > 0:
                    break
                else:
                    print("Ingrese un numero positivo valido por favor.")
            except ValueError:
                print("Error, por favor ingrese un numero valido")

        if habitaciones_disponibles_para_los_visitantes > cantidad_de_habiotaciones_a_reservar:
            #Si se puede reservar
            habitaciones_disponibles_para_los_visitantes -= cantidad_de_habiotaciones_a_reservar
            habitaciones_ocupadas_por_visitantes -= cantidad_de_habiotaciones_a_reservar
        else:
            print("No puedes reservar una habitacion que ya este ocupada, por favor reserve una o más habitacion disponible.")

    elif opcion_elegida_por_el_usuario == "3":
        while True:
            try:
                cantidad_de_habiotaciones_a_liberar = int(input("Ingrese el numero de habitacion que desesa liberar: "))
                if cantidad_de_habiotaciones_a_liberar > 0:
                    break
                else:
                    print("Ingrese un numero positivo valido por favor.")
            except ValueError:
                print("Error, por favor ingrese un numero valido")

        if habitaciones_disponibles_para_los_visitantes > cantidad_de_habiotaciones_a_liberar:
            #Si se puede reservar
            habitaciones_disponibles_para_los_visitantes += cantidad_de_habiotaciones_a_liberar
            habitaciones_ocupadas_por_visitantes -= cantidad_de_habiotaciones_a_liberar
        else:
            print("No puedes liberar una cantidad de habitacion que ya este ocupada, por favor reserve una o más habitacion disponible.")

    elif opcion_elegida_por_el_usuario == "4":
        print(f"Historial de habitaciones ocupadas {habitaciones_ocupadas_por_visitantes}")
    elif opcion_elegida_por_el_usuario == "5":
        print("Gracias por usar el programa, vuelva pronto")
        break
    else:
        print("Ingrese un numero que este dentro del menú por favor.")