habitaciones_disponibles = 50
cantidad_de_habitaciones = 0





while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")
    opcion = input("Elija la opcion que desee: ")
    
    if opcion == "1":
        print(f"Actualmente hay {habitaciones_disponibles} habitaciones disponibles")
        
    if opcion == "2":
        while True:
                try:    
                    int(input("¿Cuantas habitaciones desea reservar?"))
                    break
                except ValueError:
                     print("Ingrese una cantidad valida")
                     
        
        if habitaciones_disponibles > 0 and cantidad_de_habitaciones <= habitaciones_disponibles:
            habitaciones_disponibles -= cantidad_de_habitaciones
            
            #esta variable es para abastecer a la opcion 4
            habitaciones_ocupadas += cantidad_de_habitaciones
            
            
            print(f"Check-in realizado. Se reservaron {cantidad_de_habitaciones} habitaciones")
        else:
            print("HAGALO BIEN")
        
        
        
    if opcion == "3":
        while True:
                try:    
                    int(input("¿Cuantas habitaciones desea liberar?"))
                    break
                except ValueError:
                     print("Ingrese una cantidad valida")
                     
        
        if habitaciones_ocupadas > 0 and cantidad_de_habitaciones <= habitaciones_ocupadas:
            habitaciones_disponibles += cantidad_de_habitaciones
            
            #esta variable es para abastecer a la opcion 4
            habitaciones_ocupadas += cantidad_de_habitaciones
            
            
            print(f"Check-in realizado. Se reservaron {cantidad_de_habitaciones} habitaciones")
        else:
            print("HAGALO BIEN")
        
        
        
    if opcion == "4":
        
        

        print