#HOLA =D

stock_habitaciones=50
stock_maximo=50
reserva=0
ocupaciones=0

print("\n¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
while True:
    print("\n=== MENÚ PRINCIPAL ===\n1. Habitaciones disponibles\n2. Realizar check-in\n3. Realizar check-out\n4. Historial de ocupaciones\n5. Salir\n")
    while True:
        try:
            opcion_usuario=int(input("Por favor ingrese una opcion: "))
            break
        except ValueError:
            print("Por favor ingresea una opcion valida (Una cantidad porfavor)")
    if opcion_usuario==5:
        print("Gracias por utilizar nuestro software, hasta la próxima")
        break
    elif opcion_usuario<1 or opcion_usuario>5:
        print("\nPor favor selecciona una opción del 1 al 5.")
    elif opcion_usuario==1:
        print(f"\nHabitaciones disponibles ahora: {stock_habitaciones}.")
    elif opcion_usuario==2:
        while True:
            try:
                reserva=int(input("\n¿Cuántas habitaciones deseas reservar? "))
                break
            except ValueError:
                print("Por favor ingresea una opcion valida (Una cantidad porfavor)")
        if reserva>0 and reserva<=stock_habitaciones:
            stock_habitaciones-=reserva
            print(f"Reservaste {reserva} habitaciones")
            print(f"Habitaciones disponibles ahora: {stock_habitaciones}.")
            ocupaciones+=reserva
        elif reserva>stock_habitaciones:
            print("\nDisculpe no contamos con la cantidad de habiaciones que nos solicita")
        elif reserva<1:
            print("\nPor favor indique bien cuantas habitaciones desea reservar")
    elif opcion_usuario==3:
        while True:
            try:
                devolucion=int(input("\n¿Cuantas habitaciones desea devolver? "))
                break
            except ValueError:
                print("Por favor ingresea una opcion valida (Una cantidad porfavor)")
        if devolucion>0 and devolucion<=reserva:
            reserva-=devolucion
            stock_habitaciones+=devolucion
            print(stock_habitaciones)
            ocupaciones-=devolucion
        elif devolucion>reserva:
            print("No cuentas con las habitaciones que me estas indicando")
        elif devolucion>stock_maximo:
            print("No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel (50 habitaciones).")
        elif devolucion<1:
            print("Por favor indique bien cuantas habitaciones desea devolver")
    elif opcion_usuario==4:
        print(f"En tu poder tienes {ocupaciones} habitaciones")