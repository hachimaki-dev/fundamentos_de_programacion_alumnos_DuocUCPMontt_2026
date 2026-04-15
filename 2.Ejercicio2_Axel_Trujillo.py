print("Registro de actividades diarias")

registrar_actividades = 1
mostrar_analisis_del_tiempo = 2
salir = 3
Cantidad_de_Actividades_diarias = 0
Horas_de_actividad_diaria= 0

opcion_elegida = int(input("elija una de las opciones \n 1. Registrar actividades \n 2. mostrar análisis del tiempo \n 3. salir\n"))

while opcion_elegida:
    #-------------------Registro De las Actividades-------------------
    if opcion_elegida == 1 :
        Cantidad_de_actividades = int(input("¿Cuanta es la cantidad de actividad a registrar?\n"))
        Horas_de_actividad = int(input("Ingrese cuantos minutos realiza de actividad:\n"))
        Nombre_Actividad = input("Nombre de la actividad:\n")
        if Cantidad_de_actividades >=3:
            Cantidad_de_Actividades_diarias = Cantidad_de_Actividades_diarias + Cantidad_de_actividades
            print(f"Las activididades diarias realizadas son {Cantidad_de_Actividades_diarias}")
            Horas_de_actividad_diaria = Horas_de_actividad_diaria + Horas_de_actividad
            print(f"Los minutos de actividad realizados son {Horas_de_actividad_diaria}")
            opcion_elegida = int(input("elija una de las opciones \n 1. Registrar actividades \n 2. mostrar análisis del tiempo \n 3. salir\n"))
        elif Cantidad_de_actividades <3:
            print("Numero ingresado no valido, por favor ingrese otro numero")
            opcion_elegida = int(input("elija una de las opciones \n 1. Registrar actividades \n 2. mostrar análisis del tiempo \n 3. salir\n"))
    #-------------------Análisis de tiempo-------------------
    elif opcion_elegida == 2: 
            print(f"Ultima actividad registrada {Nombre_Actividad}")
            print("tiempo acumulado de las actividades realizadas")
            print (Horas_de_actividad_diaria)
            if Horas_de_actividad_diaria > 180:
                print("Tiempo diario maximo excedido")
            elif Horas_de_actividad_diaria <180:
                print("Tiempo diario adecuado")
            opcion_elegida = int(input("elija una de las opciones \n 1. Registrar actividades \n 2. mostrar análisis del tiempo \n 3. salir\n"))
    #-------------------Salida del programa-------------------
    elif opcion_elegida == 3:
        print("Fin del registro")
        break 
    #-------------------Número invalido-------------------
    else: 
        print("Opcion no valida, intente nuevamente")
        opcion_elegida = int(input("elija una de las opciones \n 1. Registrar actividades \n 2. mostrar análisis del tiempo \n 3. salir\n"))
    