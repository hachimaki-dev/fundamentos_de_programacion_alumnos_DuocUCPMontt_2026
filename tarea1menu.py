while True:
    print("*** Menu ***")
    print("1. Saludar")
    print("2. Contar una historia")
    print("3. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"Hola, {nombre}! Bienvenid@ a mi primer programa en Python 😊")
    
    elif opcion == "2":
        print("Había una vez una niña que quieria estudiar Informática, pero eligió un camino diferente...")
        print("Ahora está aprendiendo a programar con Python...")
        print("Cada día mejoraba más sus habilidades...")
        print("Hasta que aprendió a crear programas que cambiaron el Mundo... 🌎")
        print("La historia continúa... 🤩")

    elif opcion == "3":
        print("Saliendo del programa... ¡Nos vemos en la próxima!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")