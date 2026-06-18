habitaciones_disponibles = 50

def mostrar_menú():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

def mostrar_habitaciones_disponibles():
    return

def realizar_chqk_in():
    while True:
        try:
            respuesta = int(input("¿Cuantas habitaciones desea reservar?: "))
            if respuesta > 0:
                break
            else:
                print("Infrese numero positivo")
        except ValueError:
            print("Ingrese un numerio")
    
    if esCkeck_in == True:
        habitaciones_disponibles >= respuesta
        habitaciones_disponibles -= respuesta
        


mostrar_menú()

mostrar_habitaciones_disponibles()