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
        except ValueError:
            print("Error, ingrese un numero valido")
        return opcion

def validarOpcionMenu(opcion):
    if opcion == "1":
        habitacionesDisponibles()
    elif opcion == "2":
        realizarCheckIn(HabitacionesDisponibles)
        HabitacionesDisponibles = realizarCheckIn()
    elif opcion == "3":
        print("Se ha seleccionado la opción 3")
    elif opcion == "4":
        print("Se ha seleccionado la opción 4")
    elif opcion == "5":
        print("Se ha seleccionado la opción 5")
    else:
        print("Opción no valida, por favor, vuelva a intentarlo")

def habitacionesDisponibles():
    print(f"Actualmente hay {HabitacionesDisponibles} habitaciones disponibles")

def realizarCheckIn(Cantidad_disponible):
    while True:
        try:
            CantidadUser = int(input("¿Cuantas habitaciones desea reservar? "))
            if CantidadUser > Cantidad_disponible or CantidadUser <= 0:
                print("Error, por favor ingrese una cantidad valida, recuerde que el numero de habitaciones a reservar tiene que ser acorde a la cantidad de habitaciones disponibles, por ende, tiene que ser un numero mayor a 0 y no excederse de la cifra de habitaciones disponibles actuales.")
            else:
                Cantidad_disponible -= CantidadUser
                print("Se ha realizado el checkIn con exito")
                return Cantidad_disponible
        except ValueError:
            print("Por favor ingrese un numero natural valido")


while True:
    mostrarMenu()
    OpcionElegida = validarInput()
    validarOpcionMenu(OpcionElegida)




