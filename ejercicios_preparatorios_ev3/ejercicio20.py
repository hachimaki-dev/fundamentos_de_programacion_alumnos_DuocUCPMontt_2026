equipos_disponibles = 60
capacidad_maxima = 60
equipos_prestados = 0

print("=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Ver equipos disponibles")
    print("2. Prestar equipo(s)")
    print("3. Recibir devolución")
    print("4. Ver historial de préstamos activos")
    print("5. Salir")
    
    opcion_elegida = int(input("Selecciona una opción (1-5): "))

    if opcion_elegida == 1:
        print(f"Equipos actualmente disponibles en estantería: {equipos_disponibles}")

    elif opcion_elegida == 2:
        if equipos_disponibles == 0:
            print("No hay equipos disponibles para préstamo en este momento.")
        else:
            while True:
                try:
                    cantidad_prestada = int(input(f"Cuantos equipos desea prestar? (Disponibles:{equipos_disponibles}): "))

                    if cantidad_prestada <= 0:
                        print("Dato inválido. Debes ingresar un entero positivo.")
                    elif cantidad_prestada > equipos_disponibles:
                        print(f"Error. No puedes prestar {cantidad_prestada} equipos porque solo quedan {equipos_disponibles} disponibles.")
                    else:
                        equipos_disponibles -= cantidad_prestada
                        equipos_prestados += cantidad_prestada
                        print(f"Préstamo exitoso. Se han retirado {cantidad_prestada} equipos.")
                        break
                except ValueError:
                    print("Dato inválido. Por favor, ingresa un número entero.")
    
    elif opcion_elegida == 3:
        if equipos_prestados == 0:
            print("No se pueden recibir devoluciones. No hay equipos prestados en el sistema.")
        else:
            while True:
                try:
                    cantidad_devolucion = int(input(f"¿Cuántos equipos se van a devolver? (Prestados actualmente: {equipos_prestados}): "))

                    if cantidad_devolucion >= 0:
                        print("Dato inválido. Debes ingresar un entero positivo.")
                    elif cantidad_devolucion > equipos_prestados:
                        print(f"Error. No puedes devolver {cantidad_devolucion} equipos porque solo hay {equipos_prestados} en préstamo activo.")
                    else:
                        equipos_disponibles += cantidad_devolucion
                        equipos_prestados-= cantidad_devolucion
                        print(f"Devolución exitosa. Se han reincorporado {cantidad_devolucion} equipos al stock.")
                        break
                except ValueError:
                    print("Dato inválido. Por favor, ingresa un número entero.")
    
    elif opcion_elegida == 4:
        print(f"Historial actual: Hay {equipos_prestados} equipos en circulación (prestados).")
    
    elif opcion == "5":
        print("Gracias por utilizar el sistema. Hasta pronto.")
        break

    else:
        print("Opción no válida. Por favor, elige un número del 1 al 5.")

