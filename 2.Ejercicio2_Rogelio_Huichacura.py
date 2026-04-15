



actividades_registradas = 0
tiempo_total = 0

while True:
    
    print("registro de actividades diarias")
    print(f"menu de opciones\n 1)Registrar actividad \n 2)mostrar analisis del tiempo\n 3)Salir")
    opcion_del_usuario = int(input("Seleccione una opcion:"))
    if opcion_del_usuario == 1:
        actividades = int(input("cantidad de activadad a registrar\n :"))
        actividades_registradas += actividades
        contador_actividad_registradas = 0
        while contador_actividad_registradas < actividades :
            if actividades >= 3:
                nombre_de_la_actividad = input("ingrese el nombre de la actividad")
                tiempo_de_la_actividad = int(input("cuanto tiempo toma dicha actividad(en minutos)"))
                tiempo_total += tiempo_de_la_actividad

                print(f"se registro {actividades_registradas} actividades con un total de tiempo {tiempo_total} minutos")
                contador_actividad_registradas += 1
            else :
                print("ingrese un numero mayor o igual a 3")
                break
        
    elif opcion_del_usuario == 2 :
        print(f"tiene registrado {actividades_registradas} actividades \n su tiempo total es {tiempo_total}")
        if tiempo_total > 180 :
            print("tiempo diario excesivo")
        else:
            print("tiempo adecuado")
    elif opcion_del_usuario == 3 :
        print("fin del registro")
        break
print(f"\n actividades registradas {actividades_registradas} \n tiempo total {tiempo_total}")
