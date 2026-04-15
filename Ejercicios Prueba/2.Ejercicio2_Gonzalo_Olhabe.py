#VARIABLES
contador = 0
acumalador_tiempo = 0
opciones = 0
actividad = ""
tiempo_actividad = 0
tiempo_total = 0
Programa = True
#INICIO PASO 1

print("“Registro de actividades diarias”")

#PASO 2 MENU DE OPCIONES
while Programa == True:
    print("\n")
    print("Elija una de las siguientes opciones: \n(Utilize 1-2-3 para elejir sus opciones) ")
    print("""\n1) Registrar actividades
2) Mostrar análisis del tiempo
3) Salir""")
    print("\n")
    opciones = int(input("Elija una opcion: "))

    
    
        #PASO 3
    if opciones == 1:
        contador = 0
        #añadi un reset del tiempo total al principio para poder repetir el ingreso de acticades en caso de que el usuario lo requiera.
        tiempo_total = 0
        while True:    
            print ("\n")
            #Mientras no se ingrese un numero valido de  activades, el programa repite constantemente la pregunta de las actividades
            while True:
                contador_actividades = int(input("Ingrese el numero de activades: (Deben ser 3 o más actividades) "))
            
                if contador_actividades >= 3:
                    while contador < contador_actividades:
                        contador += 1
                        actividad = input(f"\nIngrese el nombre de su activad numero {contador} ")
                        print(f"Ingrese el tiempo en minutos de su actividad “{actividad}”: ")
                        tiempo_actividad = int(input(""))
                        tiempo_total += tiempo_actividad
                        print (f"Actividad registrada")
                    break
                else:
                    print("Muy pocas actividades")    
            print("\nTodas las actividades registradas")
            
            print ("\nVolviendo al menu principal")
            break
            
        #PASO 4    
        #Si todavia no se ha registrado actividades, o el tiempo de las activades en negativo, no se realiza la evaluacion de tiempo.
    elif opciones == 2:
        if tiempo_total > 0:
            while True:
                print (f"\nSu tiempo en minutos de las actividades registradas es: {tiempo_total} minutos")
                print ("\nEvaluando")
                for i in ("..."):
                    print (i)
                if tiempo_total > 180:
                    print ("\nTiempo diario excesivo")
                else:
                    print ("\nTiempo diario adecuado")
                print ("\nVolviendo al menu principal")
                break 
        else:
            print("\nTiempo invalido, por favor registre actividades con la opción 1")
            print ("\nVolviendo al menu principal")           
        #PASO 5
    elif opciones == 3:
            print("\nFin del Registro")
            Programa = False
    else:
            print ("\nOpcion Invalida")
            