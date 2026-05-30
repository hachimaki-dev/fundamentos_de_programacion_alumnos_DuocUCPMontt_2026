Id = []
asistencia_completa = 0
asistencia_parcial = 0

while True:
    try:
        cuantos_empleados = int(input("Cuantos empleados tiene :  "))
        if cuantos_empleados < 0 :
            print("ingrese una opcion valida")
            continue
        else:
            break
    except ValueError:
        print("ingrese una opcion valida ")
        continue

for x in range(cuantos_empleados):
    print()
    while True:
        id_del_trabajador = input("Ingrese su id de trabajador:  ")
        if len(id_del_trabajador) < 6 or " " in id_del_trabajador:
            print("Su id debe contener minimo 6 caracteres y sin espacios ")
        else:
            Id.append(id_del_trabajador)
            break

    while True:
        try :
            dias_trabajados = int(input("Ingrese los dias trabajados en el Mes :   ")) 
            if dias_trabajados < 0 or dias_trabajados > 23:
                print("Lo ingresado debe estar en un rango de 0 a 23 dias ")
                continue
            else:
                break
        except ValueError:
            print("ingrese una opcion valida")
            continue

    if dias_trabajados >= 20 :
        asistencia_completa += 1
    else:
        asistencia_parcial += 1


print()
print(f"Asistencia Complete : {asistencia_completa}")
print(f"Asistencia Parcial : {asistencia_parcial}")
print(f"Id de los Trabajadores : {Id}")