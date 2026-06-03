capacidad_maxima_estacionamiento = 20
espacios_disponibles = 20
historial_autos = 0

while True:
    print("\n=== PANEL DE CONTROL ===")
    print("1. Espacios disponibles")
    print("2. Registrar entrada de vehículo")
    print("3. Registrar salida de vehículo")
    print("4. Resumen de la jornada")
    print("5. Salir")

    opcion_elegida = int(input("Seleccione una opcion (1-5): "))

    if opcion_elegida == 1:
        print(f"Los espacios disponibles actualmente son de {espacios_disponibles}")

    elif opcion_elegida == 2:
        while True:
            try:
                entrada_autos = int(input("¡Cuantos autos van a entrar?: "))
                if entrada_autos <= 0:
                    print("Ingrese un numero positivo")
                elif entrada_autos > capacidad_maxima_estacionamiento:
                    print("No se puede superar la capacidad maxima del estacionamiento.")
                    break
                else:
                    espacios_disponibles -= entrada_autos
                    historial_autos += entrada_autos
                    print(f"Los autos registrados a entrar fueron de {entrada_autos}")
                    break
            except ValueError:
                print("Dato invalido: Ingrese un numero positivo")

    elif opcion_elegida == 3:
        while True:
            try:
                salida_autos = int(input("¡Cuantos autos van a entrar?: "))
                if salida_autos <= 0:
                    print("Ingrese un numero positivo")
                elif espacios_disponibles + salida_autos > capacidad_maxima_estacionamiento:
                    print("No se puede superar la capacidad maxima del estacionamiento.")
                    break
                else:
                    espacios_disponibles += salida_autos
                    historial_autos -= salida_autos
                    print(f"Los autos registrados a entrar fueron de {entrada_autos}")
                    break
            except ValueError:
                print("Dato invalido: Ingrese un numero positivo")
    
    elif opcion_elegida == 4:
        print(f"El total de autos que han entrado son: {historial_autos}")
    
    elif opcion_elegida == 5:
        print(f"Saliendo del sistema del estacionamiento")
        break
    else:
        print("Error: Solo se puede ingresar las opciones desde el 1 al 5.")