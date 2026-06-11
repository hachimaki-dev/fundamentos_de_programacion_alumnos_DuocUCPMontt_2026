habitaciones_disponibles = 50
historial_de_ocupaciones = 0

def darbienvenida():
    print("==="*24)
    print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
    print("==="*24)

def menu():
    print("==="*6)
    print("Menu Principal")
    print("==="*6)
    print()
    print("1. Habitaciones disponibles \n2. Realizar check-in \n3. Realizar check-out \n4. Historial de ocupaciones \n5. Salir\n")

def mostrar_mensaje_final():
    print("Gracias por utilizar nuestro software, hasta la próxima.\n")

def mostrar_habitaciones_disponibles():
    print(f"Las habitaciones que estan disponibles son : {habitaciones_disponibles}\n")

def reservar_habitaciones():
    while True:
        try:
            reservar_habitaciones = int(input("Ingrese cuantas mesas se van a Reservar : "))
            if reservar_habitaciones <= 0 or reservar_habitaciones > habitaciones_disponibles :
                print("El numero ingresado debe de ser mayor a 0 Y no puede exceder el limite de Habitaciones Disponibles")
            else:
                habitaciones_disponibles -= reservar_habitaciones
                historial_de_ocupaciones += reservar_habitaciones
                break
        except ValueError:
            print("Ingrese una opcion valida")        

def liberar_habitaciones():
    while True:
        try:
            liberar_habitaciones = int(input("Ingrese cuantas mesas se van a Liberar : "))
            if liberar_habitaciones <= 0 or liberar_habitaciones > historial_de_ocupaciones:
                print("El numero ingresado debe de ser mayor que 0 Y No debe de pasar de el Limite de mesas Disponibles")
            else:
                habitaciones_disponibles += liberar_habitaciones
                historial_de_ocupaciones -= liberar_habitaciones
                break
        except ValueError:
                    print("Ingrese una opcion valida")

def historial_habitaciones_ocupadas():
    print("===="*6)
    print("Historial de Ocupaciones")
    print("===="*6)
    print()
    print(f"Las Habitaciones Ocupadas actualmente son : {historial_de_ocupaciones}\n")

darbienvenida()



while True:
    menu()
    try:
        opcion_a_realizar = int(input("Ingrese la opcion que va a realizar : "))
        
        if opcion_a_realizar == 5:
            mostrar_mensaje_final()
            break
        elif opcion_a_realizar == 1:
            mostrar_habitaciones_disponibles()
        elif opcion_a_realizar == 2:
            reservar_habitaciones()
        elif opcion_a_realizar == 3:
            liberar_habitaciones()
        elif opcion_a_realizar == 4:
            historial_habitaciones_ocupadas()
        else:
            print("Ingrese una opcion valida") 
    except ValueError:
        print("Ingrese una opcion valida que Este en el Menu")
