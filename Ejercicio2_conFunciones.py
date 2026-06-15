HabitacionesDisponibles = 50

def mostrarMenu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

def validarInput():
    while True:
        try:
            opcion = int(input("Ingrese la opción que desea utilizar: "))
            break
        except ValueError:
            print("Error, ingrese un numero valido")
    return opcion

def accionEnElMenu(opcion):
    if opcion == 1:
        print("Se ha seleccionado la opción 1")
    elif opcion == 2:
        print("Se ha seleccionado la opción 2")
    elif opcion == 3:
        print("Se ha seleccionado la opción 3")
    elif opcion == 4:
        print("Se ha seleccionado la opción 4")
    elif opcion == 5:
        print("Gracias por utilizar el software, hasta la proxima")
        return "Basta"
    else:
        print("Opción no valida, por favor, vuelva a intentarlo")

while True:
    mostrarMenu()
    respuesta = validarInput()
    Alternativa = accionEnElMenu(respuesta)
    if Alternativa == "Basta":
        break