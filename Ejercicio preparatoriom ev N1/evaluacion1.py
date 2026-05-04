opcion_eleigda = 0
actividad1 = 0
actividad2 = 0
actividad3 = 0
tiempo1 = 0
tiempo2 = 0
tiempo3 = 0
tiempo_total = 0
tiempo_maximo = 180
print("Hola usuario bienvenido a los registro de actividades diarias")

while True :
    print("1. Registrar actividades")
    print("2. Mostrar analisis de tiempo")
    print("3. Salir")
    opcion_eleigda = int(input("Eliga una de las opciones: "))

    if opcion_eleigda == 1:
        print((" ahora tienes que decirme tres actvidades productivas que hiciste hoy y su tiempo que tardaste haciendolas se asume que el tiempo tardado es en minutos solo tienes que poner el numero ejemplo si tardaste 20 min en x actividd solo pones 20"))
        actividad1 = input("cual fue tu actividad? : ")
        tiempo1 = int(input("¿cuanto minutos te tardo?"))
        actividad2 = input("cual fue tu actividad? : ")
        tiempo2 = int(input("¿cuanto minutos te tardo?"))
        actividad3 = input("cual fue tu actividad? : ")
        tiempo3 = int(input("¿cuanto minutos te tardo?"))
        tiempo_total = tiempo1 + tiempo2 + tiempo3
        print(f" tu tiempo total sumando las siguentes actividades {actividad1} , {actividad2}y{actividad3} es de {tiempo_total} minutos")
    
    elif opcion_eleigda == 2:
        print("ahora vamos a analizar tu tiempo recuerda que el tiempo maximo es de 180")
        if tiempo_total < tiempo_maximo:
            print("tiempo dario aceptado")
        elif tiempo_maximo < tiempo_total:
            print("Tiempo diario excesivo")
    
    elif opcion_eleigda == 3:
        print("fin del registro")
        break