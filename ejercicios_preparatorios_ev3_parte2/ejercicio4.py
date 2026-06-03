total = 0

while True:
    print("\n=== CALCULADORA ===")
    print("1. Sumar número al total")
    print("2. Ver total acumulado")
    print("3. Reiniciar total")
    print("4. Salir")

    opcion_elegida = int(input("Elige una opcion (1-4): "))

    if opcion_elegida == 1:
        while True:
            try:
                numero_al_total = int(input("Digite un numero para sumarlo al total: "))
                numero_al_total += total
                break
            except ValueError:
                print("Entrada inválida. Debe ser un entero.")
    
    elif opcion_elegida == 2:
        print(f"El total acumulado es de {total}")
    
    elif opcion_elegida == 3:
        total = 0
        print(f"El total se ha reiniciado, su nuevo valor ahora es de: {total}")
    
    elif opcion_elegida == 4:
        print("Saliendo del programa, gracias por utilizarlo :)")
        break
    
    else:
        print("Dato invalido: Solo se permiten las opciones del 1 al 4.")