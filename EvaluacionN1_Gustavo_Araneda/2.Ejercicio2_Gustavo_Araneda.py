print("Registro de actividades diarias")
contador_de_actividades = 1
cantidad_de_actividades = 0
tiempo_total = 0
tiempo_actividad = 0
while True:
    opcion_elegida_por_usuario = input("Opciones: \n1.Registrar actividades \n2.Mostrar analisis del tiempo \n3.Salir \nRespuesta: ")
    if opcion_elegida_por_usuario == '1':
        while cantidad_de_actividades < 3:
            cantidad_de_actividades = int(input("¿Cuantas actividades desea registrar? \nRespuesta: "))
            if cantidad_de_actividades < 3:
                print("Numero no valido")
            elif cantidad_de_actividades >=3:
                while contador_de_actividades <= cantidad_de_actividades:
                  nombre_actividad = input(f"¿Que nombre tiene la actividad N°{contador_de_actividades}? \nRespuesta: ")
                  tiempo_actividad = int(input(f"¿Cuanto tiempo toma la actividad: {nombre_actividad}? \nRespuesta: "))
                  tiempo_total += tiempo_actividad
                  contador_de_actividades += 1
    elif opcion_elegida_por_usuario == '2':
        print(f"El tiempo total de actividades registradas es de: {tiempo_total}")
        if tiempo_total > 180:
            print("Se ha detectado un tiempo diario de actividades excesivo")
        elif tiempo_actividad <=180:
            print("El tiempo registrado de actividades diarias es adecuado")
    elif opcion_elegida_por_usuario == '3':
        print("Fin del registro")
        break
    else:
        print("Opción no valida, intente nuevamente")