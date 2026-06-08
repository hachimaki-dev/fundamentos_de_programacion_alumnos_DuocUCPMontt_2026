#HOLA =D

stock_habitaciones=50
stock_maximo=50
reservadas=0
devoluciones=0

print("\n¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
while True:
    print("\n=== MENÚ PRINCIPAL ===\n1. Habitaciones disponibles\n2. Realizar check-in\n3. Realizar check-out\n4. Historial de ocupaciones\n5. Salir\n")
    while True:
        opcion_usuario=input("Por favor ingrese una opcion: ")
        break
    if opcion_usuario=="1":
        print(f"\nHabitaciones disponibles ahora: {stock_habitaciones}.")
    elif opcion_usuario=="2":
        while True:
            try:
                reservadas=int(input("\n¿Cuántas habitaciones deseas reservar? "))
                break
            except ValueError:
                print("Por favor ingresea una opcion valida (Una cantidad porfavor)")
        if reservadas>0 and reservadas<=stock_habitaciones:
            stock_habitaciones-=reservadas
            print(f"Reservaste {reservadas} habitaciones")
            print(f"Habitaciones disponibles ahora: {stock_habitaciones}.")
            ocupaciones+=reservadas
        elif reservadas>stock_habitaciones:
            print("\nDisculpe no contamos con la cantidad de habiaciones que nos solicita")
        elif reservadas<1:
            print("\nPor favor indique bien cuantas habitaciones desea reservar")
    elif opcion_usuario=="3":
        while True:
            try:
                devolucion=int(input("\n¿Cuantas habitaciones desea devolver? "))
                break
            except ValueError:
                print("Por favor ingresea una opcion valida (Una cantidad porfavor)")
        if devoluciones>0 and devoluciones<=reservadas:
            stock_habitaciones+=devoluciones
            reservadas-=devoluciones
            print(stock_habitaciones)
            ocupaciones-=devoluciones
        elif devoluciones>reservadas:
            print("No cuentas con las habitaciones que me estas indicando")
        elif devoluciones>stock_maximo:
            print("No puedes liberar esa cantidad. Superarías la capacidad máxima del hotel (50 habitaciones).")
        elif devoluciones<1:
            print("Por favor indique bien cuantas habitaciones desea devolver")
    elif opcion_usuario=="4":
        print(f"En tu poder tienes {reservadas} habitaciones")
    elif opcion_usuario=="5":
        print("Gracias por utilizar nuestro software, hasta la próxima")
        break
    else:           
        print("\nPor favor selecciona una opción del 1 al 5.")
