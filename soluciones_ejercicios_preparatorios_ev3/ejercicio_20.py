stock_equipos_biblioteca_universidad = 60
historial_de_prestamos = 0
menu_opciones = {"Ver equipos disponibles":1,
                 "Prestar equipos":2,
                 "Recibir devolución":3,
                 "Ver historial de prestamos activos":4,
                 "Salir":5}
opcion_del_usuario = None

while opcion_del_usuario != 5:
    print(f"\n=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===\n1. Ver equipos disponibles\n2. Prestar equipo(s)\n3. Recibir devolución\n4. Ver historial de préstamos activos\n5. Salir")
    while True:
        try:
            opcion_del_usuario = int(input("\nIngrese el número de una opción (ejemplo: 1 para ver los equipos disponibles)"))
            if opcion_del_usuario < 1 or opcion_del_usuario > 5:
                print("Ingrese una opción válida")
            else:
                break
        except ValueError:
            print("Ingrese una opción válida")
    if opcion_del_usuario == menu_opciones["Ver equipos disponibles"]:
        print(f"Hay {stock_equipos_biblioteca_universidad} equipos disponibles en la biblioteca")
    elif opcion_del_usuario == menu_opciones["Recibir devolución"]:
        if historial_de_prestamos == 0:
            print("Actualmente no hay ningun equipo para recibir")
        else:
            while True:
                try:
                    equipos_para_devolver = int(input("Ingrese la cantidad de equipos a devolver: "))
                    if equipos_para_devolver <= historial_de_prestamos and equipos_para_devolver >= 1:
                        print(f"Se recibieron {equipos_para_devolver} equipos")
                        
                        historial_de_prestamos -= equipos_para_devolver
                        stock_equipos_biblioteca_universidad += equipos_para_devolver
                        break
                    else:
                        print("Ingrese un numero de equipos válido")
                except ValueError:
                    print("Ingrese un numero de equipos válido")
    elif opcion_del_usuario == menu_opciones["Ver historial de prestamos activos"]:
        print(f"Actualmente hay {historial_de_prestamos} equipos prestados")
    elif opcion_del_usuario == menu_opciones["Prestar equipos"]:
        while True:
            try:
                equipos_para_prestar = int(input("Ingrese la cantidad de equipos para prestar: "))
                if equipos_para_prestar <= stock_equipos_biblioteca_universidad and equipos_para_prestar >= 1:
                    print(f"Se prestaron {equipos_para_prestar} equipos")
                    historial_de_prestamos += equipos_para_prestar
                    stock_equipos_biblioteca_universidad -= equipos_para_prestar
                    break
                else:
                    print("Ingrese un número de equipos válido")
            except ValueError:
                print("Ingrese un número de equipos válido")
    else:
        print("si")

        