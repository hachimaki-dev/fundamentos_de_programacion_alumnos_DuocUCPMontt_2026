

#variables y datos
opcion = 0
#contador
actividades = 0
#acumulador
tiempo_total = 0



#inicio del programa

while True:
    print("\n ## BIENVENIDO AL MENU DEL PROGRAMA ##")
    print("1- Registrar actividades")
    print("2- Mostrar análisis del tiempo")
    print("3- Salir")

    opcion = int(input("Porfavor, ingrese una opcion   (1/3: "))

#opcion 1
    if opcion == 1: 
        print("\n ####### REGISTRAR ACTIVIDADES ######")   

        int(input("Ingrese el numero de actividades: "))

        if actividades >= 3:
            print("\n rango de actividades normal, bien hecho")

        else:
            print("\n rango de actividades aceptable!")

        actividades = input("\n porfavor ingrese que actividades realizo, usando comas: ")
        print(f"las actividades son {actividades}.")

        tiempo_total= int(input("Ingrese el tiempo que realizo la actividad en minutos: "))
        print(f"\n el tiempo que ingreso es: {tiempo_total}")
#opcion 2  

    elif opcion == 2:
            print("\n ############# ANALISIS DEL TIEMPO #############")

            print(f"****El tiempo total es de {tiempo_total}****")

            if tiempo_total >= 180:
                print("\n Tiempo diario excesivo")

            else:
                print("\n Tiempo diario normal")

#opcion 3
    if opcion == 3:
        print("\n ### FIN DEL REGISTRO ###")
        break