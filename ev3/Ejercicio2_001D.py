habitaciones_disponibles = 50

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Habitaciones disponibles")
    print("2. Realizar check-in")
    print("3. Realizar check-out")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    opcion_user = input("Por favor, elija una opcion: ")

    if opcion_user == "1":
        print(f"Actualmente hay {habitaciones_disponibles} habitaciones disponibles")
    
    elif opcion_user == "2":
        