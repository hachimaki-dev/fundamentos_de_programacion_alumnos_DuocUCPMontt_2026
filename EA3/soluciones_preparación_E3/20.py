# Configuración inicial del sistema
CAPACIDAD_MAXIMA = 60
equipos_disponibles = 60

print("=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")

while True:

    prestamos_activos = CAPACIDAD_MAXIMA - equipos_disponibles
    
    
    print("\n1. Ver equipos disponibles")
    print("2. Prestar equipo(s)")
    print("3. Recibir devolución")
    print("4. Ver historial de préstamos activos")
    print("5. Salir")
    
    opcion = input("\nSeleccione una opción (1-5): ")
    
    if opcion == "1":
        print(f"\nEquipos disponibles para préstamo: {equipos_disponibles}")
        
    elif opcion == "2":
        cantidad = int(input("\n¿Cuántos equipos desea prestar?: "))
        
        
        if cantidad > 0:
            if cantidad <= equipos_disponibles:
                equipos_disponibles -= cantidad
                print(f"Éxito: Se han prestado {cantidad} equipos.")
            else:
                print(f"Error: No hay suficiente stock. Solo quedan {equipos_disponibles} disponibles.")
        else:
            print("Error: La cantidad a prestar debe ser un número positivo.")
            
    elif opcion == "3":
        cantidad = int(input("\n¿Cuántos equipos se van a devolver?: "))
        
       
        if cantidad > 0:
            if cantidad <= prestamos_activos:
                equipos_disponibles += cantidad
                print(f"Éxito: Se han recibido {cantidad} equipos en devolución.")
            else:
                print(f"Error: No se pueden devolver más equipos de los prestados. Préstamos activos actuales: {prestamos_activos}")
        else:
            print("Error: La cantidad a devolver debe ser un número positivo.")
            
    elif opcion == "4":
        print(f"\nHistorial de préstamos activos: {prestamos_activos} equipos afuera.")
        
    elif opcion == "5":
        print("\nGracias por utilizar el sistema. Hasta pronto.")
        break  
        
    else:
        print("\nOpción no válida. Por favor, intente de nuevo con un número del 1 al 5.")