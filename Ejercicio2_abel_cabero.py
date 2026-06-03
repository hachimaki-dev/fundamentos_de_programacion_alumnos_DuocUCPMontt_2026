print("================================================================================")
print("===== ¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar! =====")
print("================================================================================\n")

maximo_de_habitaciones = 50
habitaciones_disponibles = 50
habitaciones_ocupadas = 0

while True:
    try:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Habitaciones disponibles")
        print("2. Realizar check-in")
        print("3. Realizar check-out")
        print("4. Historial de ocupaciones")
        print("5. Salir\n")
    
        opcion_usuario = int(input("Seleccione una opcion (1-5): "))
    
    
        if opcion_usuario == 1:
            print(f"Las habitaciones disponibles actualmente son: {habitaciones_disponibles}.")
        
        
        elif opcion_usuario == 2:
            if habitaciones_disponibles == 0 :
                print("Error: no se puede realizar ninguna reservacion, estan todas las habitaciones ocupadas.")
            else:
                while True:
                    try:
                        reservacion_habitacion = int(input("¿Cuantas habitaciones desea reservar?: "))
                        if reservacion_habitacion <= 0:
                            print("Valor invalido: Solamente se puede digitar numeros enteros positivos.")
                            break
                        elif reservacion_habitacion > habitaciones_disponibles:
                            print(f"Error: No se puede realizar la operacion debido a que excedes a las habitaciones disponibles. Solo quedan {habitaciones_disponibles}.")
                            break
                        elif reservacion_habitacion > maximo_de_habitaciones:
                            print("Error: No se puede realizar la operacion debido a que excedes la capicidad maxia del hotel (50 habitaciones).")
                            break
                        else:
                            habitaciones_disponibles -= reservacion_habitacion
                            habitaciones_ocupadas += reservacion_habitacion
                            print(f"Se reservo exitosamente la cantidad de {reservacion_habitacion} habitaciones.")
                            print(f"Las habitaciones disponibles actualmente son: {habitaciones_disponibles}.")
                            break
                    except ValueError:
                        print("Dato invalido: Solo se permiten numeros enteros positivos.")
        
        elif opcion_usuario == 3:
            if habitaciones_ocupadas == 0:
                print("Error: No se puede liberar ninguna habitacion, ya que estan todas liberadas.")
            else:
                while True:
                    try:
                        liberar_habitaciones = int(input("¿Cuantas habitaciones desea liberar?: "))
                        if liberar_habitaciones <= 0:
                            print("Valor invalido: Solamente se puede digitar numeros enteros positivos.")
                            break
                        elif liberar_habitaciones > maximo_de_habitaciones:
                            print("Error: No se puede realizar la operacion debido a que intentas excederte de la capacidad maxima del hotel (50 habitaciones).")
                            break
                        elif liberar_habitaciones > habitaciones_ocupadas:
                            print(f"Error: No se puede liberar mas de las habitaciones ya ocupadas. Superarias la capacidad maxima del hotel (50 habitaciones).")
                            break
                        else:
                            habitaciones_disponibles += liberar_habitaciones
                            habitaciones_ocupadas -= liberar_habitaciones
                            print(f"Se libero exitosamente la cantidad de {liberar_habitaciones} habitaciones.")
                            print(f"Las habitaciones disponibles actualmente son: {habitaciones_disponibles}.")
                            break
                    except ValueError:
                        print("Dato invalido: Solo se permiten numeros enteros positivos.")
        
        elif opcion_usuario == 4:
            print(f"El historial de habitaciones ocupadas son: {habitaciones_ocupadas}.")
        
        elif opcion_usuario == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
        
        else:
            print("Error: Solo se permiten las opciones del 1 al 5.")
            
    except ValueError:
        print("Dato invalido: Solo se permiten numeros enteros positivos")