cont_normal = 0
cont_estudiante = 0

precio_normal = 800
precio_estudiante = 250

total = 0

while True:
    tipo_pasajero = input("Tipo de pasajero (N: Normal, E: Estudiante, CORTE): ")

    match tipo_pasajero.lower():
        case "n":
            cont_normal += 1
            total += precio_normal
        case "e":
            cont_estudiante += 1
            total += precio_estudiante
        case "corte":
            break
        case _:
            print("Ingrese una opción válida\n")

print(f"Pasajeros normales: {cont_normal}\nPasajeros estudiantes: {cont_estudiante}\nTotal recaudado: ${total}")