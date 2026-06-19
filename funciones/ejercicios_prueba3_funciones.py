habitaciones_disponibles = 50

def mostrar():
    print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
    print(" === MENÚ PRINCIPAL ===")
    print("que opcion le gustario ver")

    print(" 1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir") 

def preguntaOpcion():
    while True:
        try:
            opcion = int(input("ingresa una opcion: "))
            break
        except ValueError:
            print("ingresa opcion valida")
    return opcion

def mostrarHabitacionesDisponibles():
    return habitaciones_disponibles

def validar_opcion_menu(opcion):
    opcion = preguntaOpcion()
    if opcion == 1:
        respuestaHabitacionesDisponibles = mostrarHabitacionesDisponibles()
        print(f"habitacion disponibles: {respuestaHabitacionesDisponibles}")
    elif opcion == 2:
        print("esta")
    elif opcion == 3:
        print("esta opcion")
    elif opcion == 4:
        print("esta opcion por 4")
    elif opcion == 5:
        print("esta opcion por 5")
    else: 
        print("")


mostrar()
validar_opcion_menu()