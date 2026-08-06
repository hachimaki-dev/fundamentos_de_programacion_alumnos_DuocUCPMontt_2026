bichos = []

while True:
    print("=== BIENVENIDO A EL SISTEMA CAZABICHOS ===")
    print("\nMENÚ PRINCIPAL")
    print("1.- AGREGAR BICHO")
    print("2.- BUSCAR BICHO")
    print("3.- ELIMINAR BICHO")
    print("4.- ACTUALIZAR ESTADOS")
    print("5.- MOSTRAR BICHOS")
    print("6.- SALIR")if opcion_elegida <= 0:
    print("ERROR, ingrese un numero mayor que 0")

    try:
        opcion_elegida = int(input("Seleccione una opción: "))

        if opcion_elegida <= 0:
            print("ERROR, ingrese un numero mayor que 0")

    except ValueError:
        print("ERROR, ingrese un numero entero positivo")

    if opcion_elegida == 1:
        nombre_bicho = input("Ingrese el nombre de el bicho a agregar: ").strip()

    elif opcion_elegida == 2:

    
    elif opcion_elegida == 3:

    
    elif opcion_elegida == 4:

    
    elif opcion_elegida == 5:

    
    elif opcion_elegida == 6:
        break

print("=== HASTA PRONTO ===")