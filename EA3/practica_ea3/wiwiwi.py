capacidad = 20
disponibles = 20
historial = 0
opciones_validas = [1,2,3,4,5]

while True:
    print("""=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===
1. Ver mesas disponibles
2. Asignar mesa(s)
3. Liberar mesa(s)
4. Mesas ocupadas actualmente
5. Salir""")
    while True:
        try:
            eleccion = int(input("ingrese su eleccion"))
            if eleccion in opciones_validas:
                break
            else:
                print("opcion discapacitada")
        except ValueError:
            print("tiene que ser un numero")
    if eleccion == 1:
        print(disponibles)
    elif eleccion == 2:
        while True:
            try:
                asignar_mesas = int(input("cuantas mesas quiere asignar"))
                if asignar_mesas > 0:
                    if asignar_mesas > disponibles:
                        print("no hay mesas disponibles suficientes")
                    else:
                        break
                else:
                    print("tiene que ser positivo")
            except ValueError:
                print("tiene que ser un numero")
        disponibles -= asignar_mesas
        historial += asignar_mesas
    elif eleccion == 3:
        while True:
            try:
                liberar_mesas = int(input("cuantas mesas quiere liberar"))
                if liberar_mesas > 0:
                    if asignar_mesas > capacidad - disponibles:
                        print("no puedes liberar mas mesas de las ue estan ocupadas")
                    else:
                        break
                else:
                    print("el numero tiene que ser positivo")
            except ValueError:
                print("tiene que ser un numero")
        disponibles += liberar_mesas
        historial -= liberar_mesas
    elif eleccion == 4:
        print(f"mesas ocupadas :{capacidad - disponibles}")
    elif eleccion == 5:
        print("Servicio finalizado. Buenas noches.")
        break
    