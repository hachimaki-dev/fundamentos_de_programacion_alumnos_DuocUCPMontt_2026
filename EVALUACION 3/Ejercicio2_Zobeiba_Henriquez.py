#Primero damos la bienvenida al usuario
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")

#Determinamos las variables del ejercicio
capacidad_max = 50
habitaciones_disponibles = 50
historial  = 0

menu = ["1", "2", "3", "4", "5"]

#Menu del programa, va dentr del while, para que se vea con cada repetición
while True:
    print(""" \n=== MENÚ PRINCIPAL ===
 1. Habitaciones disponibles
 2. Realizar check-in
 3. Realizar check-out
 4. Historial de ocupaciones
 5. Salir""")
    
#input para que el usuario escoja su opción 
    while True:
        opcion = input("Ingresa el número de la opción: ")
        if opcion in menu:
            break
        else:
            print("Error: ingresa una opción válida.")
            
#Mensaje de salida, lo coloco altiro, porque why not?    
    if opcion == "5":
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        break

#Visualización de habitaciones disponibles :p
    elif opcion == "1":
        print(f"\nHay {habitaciones_disponibles} habitaciones disponibles")

#Check in de las habitaciones, aquidebemos sumar al historial y restar en las habitaciones disponibles
    elif opcion == "2":
        while True:
            try: 
                check_in = int(input("\nCantidad de check-in: "))
                if check_in <= 0:
                    print("Error: la cantidad ingresada debe ser mayor a 0.")
                elif check_in > habitaciones_disponibles:
                    print("Error: no puedes asignar más habitaciones que las disponibles.")
                else:
                    habitaciones_disponibles -= check_in
                    historial += check_in
                    if habitaciones_disponibles == capacidad_max:
                        print("Capacidad máxima alcanzada.")
                    print(f"Se han ocupado {check_in} habitaciones.")
                    print(f"Actualmente hay: {habitaciones_disponibles} habitaciones disponibles")
                    break
            except ValueError:
                print("Ingrese la cantidad de habitaciones ocupadas en formato numérico.")
                    
#Check-out de las habitaciones del hotel, resta al historal y suma en las habitaciones disponibles
    elif opcion == "3":
        while True:
            try:
                check_out = int(input("\nCantidad de check-out: "))
                if check_out <= 0:
                    print("Error: la cantidad ingresada debe ser mayor a 0.")
                elif check_out > historial:
                    print("Error: No puedes devolver más habitaciones que las ocupadas")
                else:
                    habitaciones_disponibles += check_out
                    historial -= check_out
                    print(f"Se han liberado {check_out} habitaciones.")
                    print(f"Actualmente hay: {habitaciones_disponibles} habitaciones disponibles")
                    break
            except ValueError:
                print("Ingrese la cantidad de habitaciones recién disponibles en formato numérico.")

#Historial de habitacioes utilizadas x.x      
    elif opcion == "4":
        print(f"\nHan sido ocupadas {historial} habitaciones.")