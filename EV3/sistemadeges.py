estacionamiento = 20
max_estacionamiento = 20
jornada = 0

while True: 
        print("--- Estacionamiento ---")
        print("1.Espacios disponibles")
        print("2.Entrada de Vehiculos")
        print("3.Salida de Vehiculos")
        print("4.Autos que han entrado")
        print("5.Salir del programa")
        opcion =input("Ingrese una opcion: ")
        
        if opcion == "1":
            print(f"Espacios disponibles {estacionamiento} ")
        elif opcion == "2":
            while True:
                try:
                    entrada = int(input("Vehiculos que ingresan: "))
                    if entrada > 0:
                        print("El numero debe ser mayor a cero")
                    elif entrada > estacionamiento:
                        print(f"No hay espacio disponible. Solo queda {estacionamiento} lugares")
                        break
                except ValueError:
                    print("Ingrese un entero valido")
        elif opcion == "3":
            while True:
                try:
                    salida = int(input("Vehiculos que salen: "))
                    if salida > 0:
                        print("El numero debe ser mayor a cero")
                    elif estacionamiento + salida > max_estacionamiento:
                        print("Operacion invalida. excede la capacidad maxima del estacionamiento")
                        break
                except ValueError:
                    print("Ingrese un entero valido")
        
        elif opcion == "4":
            print(f"Balance neto de vehiculos ingresados hoy fue de {jornada}")
        elif opcion == "5":
            print("Cerrando sistema. Hasta luego :)")
            break
        else:
            print("Opcion no reconocida. Seleccione del 1 al 5")
                         
                
        