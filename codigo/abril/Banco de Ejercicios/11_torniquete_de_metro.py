valor_pasaje_regular = 800
valor_pasaje_estudiante= 250
total_recaudado = 0

contador_pasaje_regular = 0
contador_pasaje_estudiante = 0

while True:
    pasajero = input('Ingrese el tipo de pasaje a cobrar: "R" para pasaje regular y "E" para estudiante.            ')
    pasajero = str.lower(pasajero)

    if pasajero == "r":
        contador_pasaje_regular += 1
        total_recaudado += valor_pasaje_regular
        print(f"Pasaje regular cobrado: ${valor_pasaje_regular}")
    elif pasajero == "e":
        contador_pasaje_estudiante += 1
        total_recaudado += valor_pasaje_estudiante
        print(f"Pasaje estudiante cobrado: ${valor_pasaje_estudiante}")
    elif pasajero == "corte":
        break
    else:
        print("Opción inválida")

print(f"Pasajeros regulares: {contador_pasaje_regular}\nEstudiantes: {contador_pasaje_estudiante}\nTotal dinero en caja: ${total_recaudado}")
