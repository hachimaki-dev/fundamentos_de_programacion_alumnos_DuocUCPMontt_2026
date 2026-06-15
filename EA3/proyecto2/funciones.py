habitacionesdisponibles = 50

def mostrarMenu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")
def mostrarHabitacionesDisponibles():

    return habitacionesdisponibles
def preguntarOpcion():
    while True:
        try:
            opcion_validada = int(input("ingrese opcion valida"))
            break
        except ValueError:
            print("nuh uh")
    return opcion_validada


def validarOpcioMenu():
    opcion = preguntarOpcion()
    if opcion ==1:
        pass
    elif opcion ==2:
        pass
    elif opcion ==3:
        pass
    elif opcion ==4:
        pass
    elif opcion ==5:
        pass

mostrarMenu()
validarOpcioMenu()
