tiempo_total = 0
while True:
    opcion_menu = int(input("Registro de actividades diarias. \n1. Registrar actividades \n2. Mostrar análisis del tiempo \n3. Salir \nIngrese su opción: "))
    if opcion_menu == 1:
        actividad = int(input("Ingrese la cantidad de actividades a registrar: "))
        if actividad >=3:
            for contador in range(actividad):
                nombre_actividad = input("Ingrese actividad: ")
                tiempo_actividad = int(input("Tiempo de la actividad: "))
                tiempo_total += tiempo_actividad
            print(f"Numero de actividades registradas {actividad} \nTiempo total de actividades: {tiempo_total}")
        else:
            print("Debe registrar al menos 3 actividades")
    elif opcion_menu == 2:
        print(f"El tiempo total acumulado de las actividades registradas {tiempo_total}")
        if tiempo_total > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")
    elif opcion_menu == 3:
        print("Fin del registro")
        break
    else:
        print("Opción inválida")