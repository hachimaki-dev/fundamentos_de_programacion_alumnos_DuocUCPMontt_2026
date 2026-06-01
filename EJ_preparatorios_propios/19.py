camion_pesado = 0
camion_liviano = 0

while True:
    try:
        vehiculos_registrados = int(input("Cuantos Vehiculos se Registran :   "))
        if vehiculos_registrados <= 0:
            print("El umero ingresado debe de ser un numero entero positivo") 
        else:
            break
    except ValueError:
        print("ingrese una opcion valida")
        


for a in range(vehiculos_registrados):
    print()
    while True:
        patente_del_auto = input("Ingrese la patente del auto :   ")
        
        if len(patente_del_auto) < 6 or " " in patente_del_auto:
            print("La patente ingresada debe de contener 6 caracteres minimo y sin espacios")
        else:
            break
    
    while True:
        try:
            capacidad_toneladas = int(input("Ingrese la capacidad de carga en toneladas :  "))

            if capacidad_toneladas < 0 :
                print("Ingrese una cantidad entera positiva")
            elif capacidad_toneladas  > 15 :
                camion_pesado += 1
                break
            else:
                camion_liviano += 1
                break
        except ValueError:
            print("ingrese una opcion valida")


print(f"La Flota cuenta con {vehiculos_registrados} Camiones Registrados los cuales son :")
print()
print(f"Camiones Pesados : {camion_pesado} \nCamiones Livianos : {camion_liviano}")