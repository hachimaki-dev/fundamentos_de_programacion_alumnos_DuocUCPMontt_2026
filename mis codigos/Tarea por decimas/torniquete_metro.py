dinero_reunido = 0
contador_estudiantes = 0
contador_normales = 0

while True:
    print("~~~Bienvenido! Este programa te ayudará a calcular el costo de tu viaje~~~") #puse el while desde esta linea suponiendo que es necesario mostrarlo desde aqui a cada pasajero que pase
    print("PRECIOS: \nNormal: $800 \nEstudiante: $250")
    tipo_pasajero = input("¿Qué tipo de pasajero es? Elija entre: \nN - Normal \nE - Estudiante \nCORTE para salir \n")

    if tipo_pasajero == "N":
        print("El costo de su viaje es de $800")
        dinero_reunido += 800
        contador_normales += 1

    elif tipo_pasajero == "E":
        print("El costo de su viaje es de $250")
        dinero_reunido += 250
        contador_estudiantes += 1
    elif tipo_pasajero == "CORTE":
       print(f"Pasajeros normales: {contador_normales} \nPasajeros estudiantes: {contador_estudiantes} \nTotal dinero en caja: ${dinero_reunido}")
       break
    else:    
        print("Opción no válida. Por favor, elija entre [N - Normal] [E - Estudiante.] o [CORTE para salir]")