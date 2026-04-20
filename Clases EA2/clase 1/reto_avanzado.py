vengadores = []

while True:
    print("\n1-Agregar Avenger")
    print("2-Mostrar Base y Modificar")
    print("3-Salir")
    opcion = int(input("\nIngresa el número de la acción a realizar: "))
    
    if opcion == 3:
        print("Saliste del programa")
        break
    
    elif opcion == 1:
        hero = input("Ingresa un héroe: ")
        vengadores.append(hero)
        print(f"Ingresaste a: {hero}")
        print(f"Lista actual: {vengadores}")
    
    elif opcion == 2:
        contador = 0
        for i in range(len(vengadores)):
            contador += 1
            vengadores[i] = vengadores[i].upper()
            print(f"{contador}) {vengadores[i]}")
            
    else:
        print("Ingresa una opción válida")
