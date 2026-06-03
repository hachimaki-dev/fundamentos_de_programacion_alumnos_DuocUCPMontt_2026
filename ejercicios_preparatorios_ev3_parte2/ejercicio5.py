capacidad_maxima_biblioteca = 30
libros_disponibles = 30
libros_prestados = 0

while True:
    print("--- BIBLIOTECA ---")
    print("1. Libros disponibles")
    print("2. Prestamo")
    print("3. Devolucion")
    print("4. Resumen")
    print("5. Salir")

    opcion_elegida = int(input("Seleccione su opcion (1-5): "))

    if opcion_elegida == 1:
        print(f"Los libros disponibles en este momento son: {libros_disponibles}")

    elif opcion_elegida == 2:
        while True:
            try:
                prestar_libros = int(input("¡Cuantos libros desea prestar?: "))
                if prestar_libros <= 0:
                    print("Ingrese un numero positivo")
                elif prestar_libros > libros_disponibles:
                    print(f"No hay suficientes libros. Solo quedan {libros_disponibles} disponibles.")
                    break
                else:
                    libros_disponibles -= prestar_libros
                    libros_prestados += prestar_libros
                    print(f"Se ha prestado la cantidad de {prestar_libros} exitosamente.")
                    break
            except ValueError:
                print("Dato invalido: Ingrese un numero positivo")
    
    elif opcion_elegida == 3:
        while True:
            try:
                devolver_libro = int(input("¡Cuantos libros desea devolver?: "))
                if devolver_libro <= 0:
                    print("Ingrese un numero positivo")
                elif libros_disponibles + devolver_libro > capacidad_maxima_biblioteca:
                    print(f"No hay suficientes libros. Solo quedan {libros_disponibles} disponibles.")
                    break
                else:
                    libros_disponibles += devolver_libro
                    libros_prestados -= devolver_libro
                    print(f"Se ha prestado la cantidad de {prestar_libros} exitosamente.")
                    break
            except ValueError:
                print("Dato invalido: Ingrese un numero positivo")

    elif opcion_elegida == 4:
        print(f"Los libros totales prestados son: {libros_prestados}")

    elif opcion_elegida == 5:
        print("Gracias por usar el sistema de la biblioteca. ¡Hasta pronto!")
        break

    else:
        print("Error: Solo se puede ingresar las opciones desde el 1 al 5.")