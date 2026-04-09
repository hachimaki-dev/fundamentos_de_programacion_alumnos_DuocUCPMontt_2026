def calc_trayecto(precio_viaje, tipo_viaje, cant_pasajes, descuento):
    total_viaje = precio_viaje * cant_pasajes

    if tipo_viaje == 1:
        if total_viaje > 10000:
            total_viaje -= total_viaje * descuento
            return total_viaje
        else:
            return total_viaje
    else:
        total_viaje *= 2
        if total_viaje > 10000:
            total_viaje -= total_viaje * descuento
            return total_viaje
        else:
            return total_viaje


destino = 0
tipo_viaje = 0
cant_pasajes = 0

precio_1 = 3000
precio_2 = 5000
precio_3 = 7000

descuento = 0.1

total_diario = 0

print("----- Bienvenido a la boletería de Cruz del Sur -----\n")

while destino != 1 and destino != 2 and destino != 3:
    print("1) Puerto Varas ($3000)\n2) Frutillar ($5000)\n3) Osorno ($7000)")
    destino = int(input("Ingrese su destino: "))

    if destino != 1 and destino != 2 and destino != 3:
        print("Opción inválida")

while tipo_viaje != 1 and tipo_viaje != 2:
    print("\n1) Ida\n2) Ida y vuelta")

    tipo_viaje = int(input("Ingrese su tipo de viaje: "))

    if tipo_viaje != 1 and tipo_viaje != 2:
        print("Opción inválida")

while cant_pasajes < 1:
    cant_pasajes = int(input("Ingrese la cantidad de pasajes: "))

    if cant_pasajes < 1:
        print("Cantidad de pasajes inválida")

match destino:
    case 1:
        calc_trayecto(precio_1, tipo_viaje, cant_pasajes, descuento)
    case 2:
        calc_trayecto(precio_2, tipo_viaje, cant_pasajes, descuento)
    case 3:
        calc_trayecto(precio_3, tipo_viaje, cant_pasajes, descuento)
    case _:
        print("Error")

