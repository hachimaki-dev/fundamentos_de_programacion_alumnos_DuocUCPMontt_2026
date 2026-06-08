habitaciones_disponibles = 50
historial_de_ocupaciones = 0

print("==="*24)
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
print("==="*24)

while True:
    print("==="*6)
    print("Menu Principal")
    print("==="*6)
    print()
    print("1. Habitaciones disponibles \n2. Realizar check-in \n3. Realizar check-out \n4. Historial de ocupaciones \n5. Salir")
    print()

    try:
        opcion_a_realizar = int(input("Ingrese la opcion que va a realizar : "))
        
        if opcion_a_realizar == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
        elif opcion_a_realizar == 1:
            print(f"La cantidad de habitaciones Disponibles son : {habitaciones_disponibles}")
            print()
        elif opcion_a_realizar == 2:
            while True:
                try:
                    reservar_mesas = int(input("Ingrese cuantas mesas se van a Reservar : "))
                    if reservar_mesas <= 0 or reservar_mesas > habitaciones_disponibles :
                        print("El numero ingresado debe de ser mayor a 0 Y no puede exceder el limite de Habitaciones Disponibles")
                    else:
                        habitaciones_disponibles -= reservar_mesas
                        historial_de_ocupaciones += reservar_mesas
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_a_realizar == 3:
            while True:
                try:
                    liberar_mesas = int(input("Ingrese cuantas mesas se van a Liberar : "))
                    if liberar_mesas <= 0 or liberar_mesas > historial_de_ocupaciones:
                        print("El numero ingresado debe de ser mayor que 0 Y No debe de pasar de el Limite de mesas Disponibles")
                    else:
                        habitaciones_disponibles += liberar_mesas
                        historial_de_ocupaciones -= liberar_mesas
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_a_realizar == 4:
            print("===="*6)
            print("Historial de Ocupaciones")
            print("===="*6)
            print()
            print(f"Las Habitaciones Ocupadas actualmente son : {historial_de_ocupaciones}")
            print()
        else:
            print("Ingrese una opcion valida") 
    except ValueError:
        print("Ingrese una opcion valida que Este en el Menu")
