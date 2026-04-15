salir = False
tiempo_total = 0

while salir == False:
    print("\n~~Registro de actividades diarias~~")
    print("\n1)Registrar actividades \n2)Mostrar análisis del tiempo \n3)Salir")
    seleccion = int(input("Seleccione una opcion (1-3)\n "))
    numero_actividades = 0
    if seleccion == 1:
        actividades_a_registrar = int(input("Ingrese las actividades a registrar (tiene que ser igual o mayor a 3)\n "))
        if actividades_a_registrar >= 3:
            while numero_actividades < actividades_a_registrar:
                actividad = input("Ingrese el nombre de su actividad\n ")
                print(f"{actividad}")
                #me gustaria saber sobre arrays para poder guardar estas
                tiempo_actividad = int(input("Ingrese el tiempo que se demora en completar dicha actividad (en minutos)\n "))
                numero_actividades += 1
                tiempo_total = tiempo_total + tiempo_actividad
        else:
            print("Numero de actividades inadecuada")
    elif seleccion == 2:
        print(f"\nSu tiempo total gastado en actividades fue de {tiempo_total}m")
        tiempo_total_en_horas = tiempo_total / 60
        print(f"Su tiempo total gastado en horas fue de ~{round(tiempo_total_en_horas)}h")
        if tiempo_total > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")
    elif seleccion == 3:
        print("\nFin de registro")
        salir = True
        #podria usar un break aca tambn pero asi queda mas bonito :3

