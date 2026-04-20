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
        for i in range(len(vengadores)):
            vengadores[i] = vengadores[i].upper()
            print(f"{contador}) {vengadores[i]}")
            
        change = input("\nIngresa la palabra sereta para comunicar que un héroe está fuera de base: ")
        
        if change == "SACRIFICAR":
                heroe = int(input("\nIngresa el NÚMERO del vengador que deseas eliminar: "))
                eliminado = vengadores.pop(i)
                vengadores.pop(heroe)
                print(f"Eliminaste a {heroe} de la lista")
        else:
                print("No se realizaron cambios ")
    else:
        print("Ingresa una opción válida")
