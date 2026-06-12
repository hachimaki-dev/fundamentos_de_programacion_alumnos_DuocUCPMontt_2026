habitaciones_disponibles = 50
historial_de_ocupaciones = 0
capacidad_maxima = 50
while True:
    print("===MENU PRINCIPAL===")
    print("1.habitaciones disponible")
    print("2.realizar check-in")
    print("3.realizar check-out")
    print("4.historial de ocupaciones")
    print("5.salir")

    opcion = int(input("ingrese una opcion:"))
    if opcion == 1:
        print("actualmente hay",habitaciones_disponibles,"habitaciones disponibles:")
    elif opcion == 2:
        try:
            reservar = int(input("cuantas habitaciones desea reservar:"))
            if reservar <= 0:
                print("Valor inválido. Debes ingresar un número entero mayor a 0.")
            elif reservar > habitaciones_disponibles:
                print("no hay suficientes habitaciones disponibles")
            else:
                habitaciones_disponibles -= reservar
                historial_de_ocupaciones += reservar
                print("chek-in realizado: se reservaron",reservar,"habitaciones")
                print("habitaciones disponibles ahora",habitaciones_disponibles)
        except ValueError:
            print("ingrese una opcion valida") 
    elif opcion == 3:
        try:
            reservar = int(input("¿cuantas habitaciones desea liberar?"))
            if reservar <= 0:
                print("Valor inválido. Debes ingresar un número entero mayor a 0.")
            elif habitaciones_disponibles + reservar > capacidad_maxima:
                print("no se puede liberar esa cantidad")
                print("Superarías la capacidad máxima del hotel :",capacidad_maxima,"habitaciones")
            else:
                habitaciones_disponibles += reservar
                historial_de_ocupaciones -= reservar
                print("check-out realizado: se liberaron {reservar} de habitaciones")
                print("habitaciones disponibles ahora:",habitaciones_disponibles)
        except ValueError:
            print("debes ingesar un numero entero valido")
    elif opcion == 4:
        print("historial neto de ocupaciones esta sesion:",historial_de_ocupaciones,"de habitaciones")
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("opcion invalida:")
        print("porfavor ingrese una opcion del 1 al 5")