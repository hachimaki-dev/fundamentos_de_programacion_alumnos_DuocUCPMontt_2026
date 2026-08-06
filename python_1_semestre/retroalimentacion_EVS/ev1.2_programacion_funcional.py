
contador = 0
tiempo_total = 0
def menu():
    while True:
        print("")
        print(" Registro de actividades diarias ")
        print("")
        print("Menú de opciones")
        print(" 1.Registrar Actividades")
        print(" 2.Mostrar Analisis del tiempo")
        print(" 3.Salir")
        menu_de_opciones = int(input("seleciona una opcion : "))
        if menu_de_opciones == 1:
            registro_de_actitividades()
        elif menu_de_opciones == 2:
            analisis_del_tiempo()
        elif menu_de_opciones == 3:
            cierre_menu()
            break
        else:
            print("ingresa un numero acorde al menu del 1 al 3")
            print("")
        

def registro_de_actitividades():
    while True:
        actividades_registro = int(input("ingresa la cantidad de actividades a registrar : "))
        if actividades_registro >= 3:
            contador = 0
            tiempo_total = 0

            while contador <= actividades_registro:
                global nombre_actividad 
                nombre_actividad = input(f"ingresa el nombre de la actividad {contador + 1} : ")
                contador +=1
                
                global tiempo_actividad    
                tiempo_actividad = int(input("cuanto tiempo toma la actividad en minutos? : "))
                tiempo_total += tiempo_actividad
                if contador == actividades_registro:
                    break
            break
        else:
            print("la cantidad de actividades a registrar tiene que ser mayor o igual que 3")

    
def analisis_del_tiempo():
    print(f"el tiempo total acumulado de las actividades registradas es : {tiempo_total}")
    if tiempo_total > 180:
        print("Tiempo diario excesivo")
    else:
        print("Tiempo diario adecuado")

def cierre_menu():
    print("Fin del registro")
    
menu()    

    