

capacidad_maxima = 50
habitaciones_disponibles = capacidad_maxima
historial_neto = 0

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Opción no válida. Por favor selecciona una opción del 1 al 5.")
        continue

    if opcion == 1:
        print(f"Actualmente hay {habitaciones_disponibles} habitaciones disponibles.")

    elif opcion == 2:
        try:
            cantidad = int(input("¿Cuántas habitaciones deseas reservar? "))
        except ValueError:
            print("Valor inválido. Debes ingresar un número entero mayor a 0.")
            continue

        if cantidad <= 0:
            print("Valor inválido. Debes ingresar un número entero mayor a 0.")
        elif cantidad > habitaciones_disponibles:
            print(f"No hay suficientes habitaciones disponibles. Solo quedan {habitaciones_disponibles}.")
        else:
            habitaciones_disponibles -= cantidad
            historial_neto += cantidad
            print(f"Check-in realizado. Se reservaron {cantidad} habitaciones.")
            print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}.")

    elif opcion == 3:
        try:
            cantidad = int(input("¿Cuántas habitaciones deseas liberar? "))
        except ValueError:
            print("Valor inválido. Debes ingresar un número entero mayor a 0.")
            continue

        if cantidad <= 0:
            print("Valor inválido. Debes ingresar un número entero mayor a 0.")
        elif habitaciones_disponibles + cantidad > capacidad_maxima:
            print(f"No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel ({capacidad_maxima} habitaciones).")
        else:
            habitaciones_disponibles += cantidad
            historial_neto -= cantidad
            print(f"Check-out realizado. Se liberaron {cantidad} habitaciones.")
            print(f"Habitaciones disponibles ahora: {habitaciones_disponibles}.")

    elif opcion == 4:
        print(f"Historial neto de ocupaciones en esta sesión: {historial_neto} habitaciones.")

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Opción no válida. Por favor selecciona una opción del 1 al 5.")
