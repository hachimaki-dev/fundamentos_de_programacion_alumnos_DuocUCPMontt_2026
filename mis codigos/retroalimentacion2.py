habitaciones_totales = 50
historial_del_usuario = 0

while True:
    try:
        print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
        print("=== MENÚ PRINCIPAL ===")
        print("1. Habitaciones disponibles")
        print("2. Realizar check-in")
        print("3. Realizar check-out")
        print("4. Historial de ocupaciones")
        print("5. Salir")
        
        opcion_elegida = int(input("que opcion quiere elegir?: "))
        
        if opcion_elegida == 1:
            print(f"las habitaciones disponibles son {habitaciones_totales}")
            
        elif opcion_elegida == 2:
            habitaciones_por_reservar = int(input("cuantas habitaciones quieres reservar?: "))
            if habitaciones_por_reservar < 0:
                print("tiene que ser un numero postivo")
            elif habitaciones_por_reservar > habitaciones_totales:
                print("no puedes reversar mas habitaciones de las que hay") 
            else:
                habitaciones_totales -= habitaciones_por_reservar
                historial_del_usuario += habitaciones_por_reservar
                print(f"haz reservado {habitaciones_por_reservar} habitaciones")
                
        elif opcion_elegida == 3:
            habitacionesPorDevoler = int(input("cuantas habitaciones quieres devolver?: "))
            if habitacionesPorDevoler < 0:
                print("no puedes poner numeros negativos")
            elif habitaciones_totales + habitacionesPorDevoler > 50 or habitacionesPorDevoler > historial_del_usuario:
                print("no puedes devolver mas habitaciones de las que hay totales o de las que reservaste") 
            else:
                habitaciones_totales += habitacionesPorDevoler
                historial_del_usuario -= habitacionesPorDevoler 
                print(f"devolviste {habitacionesPorDevoler} habitaciones")
                
        elif opcion_elegida == 4:
            if historial_del_usuario == 0:
                print("no tienes historial")
            else: 
                print(f"tu historial es de {historial_del_usuario} habitaciones")
                
        elif opcion_elegida == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
            
    except ValueError:
        print("solo se puede escribir el numero elegido")