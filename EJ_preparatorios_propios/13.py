equipo_obsoleto = 0
equipo_vigente = 0
id_equipos = []


while True:
    try:
        equipos_ingresados = int(input("Ingrese cuantos equipos van a ingresar:  "))
        if equipos_ingresados < 0:
            print("Los equipos ingresados no pueden ser menores que 0 deben de ser mayores")
            continue
        else:
            break
    except ValueError:
        print("ingrese una opcion valida")
        continue

for i in range(equipos_ingresados):
    print()
    while True:
        codigo_equipo = input("Ingrese el codigo de su equipo:  ")
        if len(codigo_equipo) < 6 or " " in codigo_equipo:
            print("ingrese un codigo de 6 caracteres minimo y que no contenga espacios")
            continue
        else:
            id_equipos.append(codigo_equipo)
            break
    
    while True:
        try:
            año_fabricacion = int(input("Ingrese el año de fabricacion del equipo :  "))
            if año_fabricacion < 1990 or año_fabricacion > 2026:
                print("El rango de el año de fabricacion es de entre 1990 a 2026") 
                continue
            else:
                break
        except ValueError:
            print("ingrese una opcion valida")
            continue
          
    
    if año_fabricacion < 2018 :
        equipo_obsoleto += 1
    else:
        equipo_vigente += 1



print()
print(f"Equipos Obsoletos : {equipo_obsoleto}")
print(f"Equipos Vigentes : {equipo_vigente}")
print(f"Id de cada equipo Registrado  : {id_equipos}")
