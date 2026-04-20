vengadores = []

while True :
    print("1) Agregar Avenger.")
    print("2) Mostrar Base y Modificar.")
    print("3) Salir.")

    opcion = input("")

    match opcion :
        case "1" :
            nombre_avenger = input("Ingrese el nombre del héroe: ")
            vengadores.append(nombre_avenger)
        case "2" :
            print("Mostrando héroes: ")
            for i in range(len(vengadores)) :
                print(f"{i+1} - {vengadores[i]}")

            print("¿Quiere colocar los nombres de los héroes en mayúscula?")
            print("1) Sí.")
            print("2) No.")

            opcion = input("")

            if opcion == 1 : 
                print("Cambiando a mayúscula...")

                for i in range(len(vengadores)) :
                    vengadores[i] = vengadores[i].upper()
        case "3" :
            break
        case "Sacrificar" :
            if len(vengadores) == 0 :
                print("No hay héroes para sacrificar.")
                continue

            print(f"Se ha SACRIFICADO el héroe {vengadores[-1]}.")
            vengadores.pop()
        case _ :
            print("Error. Introduzca una opción correcta.")