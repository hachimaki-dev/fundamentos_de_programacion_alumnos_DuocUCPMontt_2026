vengadores = []


#1-Agregar Avenger, 2-Mostrar Base y Modificar, 3-Salir.

while True:
    print("1. Agregar Avenger")
    print("2. Mostrar Base y Modificar")
    print("3. Salir")
    print("="*30) #para poner === de forma estetica, más rapido.

    select = int(input("Seleccione una opcion: "))
    if select == 1:
        nombreavenger = input("Nombre del Avenger: ")
        vengadores.append(nombreavenger)
        print(f"Bien, {nombreavenger} ha sido añadido.")
    elif select == 2:
        if len(vengadores) == 0:
            print("No hay vengadores")
        else:
             for i in range(len(vengadores)):
                 print(f" {i} - {vengadores[i]}")
                 vengadores[i] = vengadores[i].upper()
             print("Permitido poner en mayúsculas")
    elif select == 3:
        print("Cerrando el sistema.")
        break
