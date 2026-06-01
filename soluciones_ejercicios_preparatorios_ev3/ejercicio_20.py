stock_equipos_biblioteca_universidad = 60
historial_de_prestamos = 0
menu_opciones = {"Ver equipos disponibles":1,
                 "Prestar equipos":2,
                 "Recibir devolución":3,
                 "Ver historial de prestamos activos":4,
                 "Salir":5}
opcion_del_usuario = None

while opcion_del_usuario != 5:
    print(f"=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===\n1. Ver equipos disponibles\n2. Prestar equipo(s)\n3. Recibir devolución\n4. Ver historial de préstamos activos\n5. Salir")
    while True:
        try:
            opcion_del_usuario = int(input("Ingrese el número de una opción (ejemplo: 1 para ver los equipos disponibles)")).strip()
            if opcion_del_usuario <= 0 and opcion_del_usuario > 5:
                print("Ingrese una opción válida")
            else:
                break
        except ValueError:
            print("Ingrese una opción válida")
    if opcion_del_usuario == menu_opciones["Ver equipos disponibles"]:
        print(f"Hay {stock_equipos_biblioteca_universidad} equipos disponibles en la biblioteca")
    elif opcion_del_usuario == menu_opciones["Recibir devolución"]:
        while True:
            try:
                equipos_para_devolver = int(input("Ingrese la cantidad de equipos a devolver: ")).strip()
                if equipos_para_devolver <= historial_de_prestamos:
                    print(f"Se recibieron {equipos_para_devolver} equipos")
                    break
                else:
                    print("Ingrese un numero de equipos válido")
            except ValueError:
                print("Ingrese una opción válida")
        