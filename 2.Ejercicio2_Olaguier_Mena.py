contador = 0
minutos = 0

print("***REGISTRO DE ACTIVIDADES DIARIAS***")

while True:
    print("Que desea hacer?")
    print("1. Registrar actividades.")
    print("2. Mostrar análisis del tiempo.")
    print("3. Salir.")
    opcion_elegida = int(input("Elija su opción: "))
    if opcion_elegida ==1:
        numero_actividad = int(input("Cuantas actividades quiere registrar? "))
        if numero_actividad >=3:
            print(f"Su numero de actividades es {numero_actividad}.")
            while contador < numero_actividad:
                actividades = input("Cual actividad fue:  ")
                minutos_actividad = int(input("Cuantos minutos le tomo hacerla: "))
                minutos = minutos + minutos_actividad
                contador = contador +1
        elif numero_actividad < 3:
                print("Flojo, has mas ejercicio.")
    if opcion_elegida ==2:
        print(f"El tiempo total de las actividades registradas es de {minutos} minutos.")
        if minutos > 180:
            print("Tiempo diario excesivo.")
        elif minutos < 180:
            print("Tiempo diario adecuado.")
            print("Volviendo al menu principal.")
    if opcion_elegida ==3:
        print("Fin del registro.")
        break
