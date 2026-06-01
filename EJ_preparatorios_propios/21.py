mesas_disponibles = 20
mesas_ocupadas = 0

print("==="*14)
print("SISTEMA DE MESAS - RESTAURANTE EL FARO")
print("==="*14)

while True:
    print("1. Ver mesas disponibles \n2. Asignar mesa(s) \n3. Liberar mesa(s) \n4. Mesas ocupadas actualmente \n5. Salir")

    try:
        opcion_elegida = int(input("Ingrese la opcion que va a realizar :       "))

        if opcion_elegida == 5:
            print("Servicio finalizado. Buenas noches.")
            break
        elif opcion_elegida == 1:
            print(f"Mesas Disponibles : {mesas_disponibles}")
        elif opcion_elegida == 2:
            while True:
                try:
                    asignar_mesas = int(input("Ingrese cuantas mesas se van a asignar :     "))
                    if asignar_mesas > mesas_disponibles:
                        print("No se puede asignar mas mesas de las que hay disponibles")
                    else:
                        mesas_ocupadas += asignar_mesas
                        mesas_disponibles -= asignar_mesas
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elegida == 3:
            while True:
                try:
                    liberar_mesas = int(input("Ingrese cuantas mesas se van a liberar :     "))
                    if liberar_mesas > mesas_ocupadas:
                        print("No se pueden liberar mas mesas de las que estan ocupadas")
                    else:
                        mesas_ocupadas -=  liberar_mesas
                        mesas_disponibles += liberar_mesas
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elegida == 4:
            print()
            print("#####"*6)
            print("Mesas ocupadas actualmente ")
            print("#####"*6)
            print()
            print(f"Las mesas Ocupadas actualmente son {mesas_ocupadas}")
    except ValueError:
        print("Ingrese una opcion valida")
