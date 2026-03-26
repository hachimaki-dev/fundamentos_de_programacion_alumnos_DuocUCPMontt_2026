def menu_principal():
    print("\n--- menú pricipal ---")
    print("1. saludar")
    print("2. Contar una historia")
    print("3. Salir")

while True:
    print("mostrar_menu")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Hola como estas")
    elif opcion == "2":
        print("al final aprendiste a programar y te fue bien")
    elif opcion == "3":
        print("Salir")
        break  
    else:
        print("Opción no válida, intente de nuevo.")
