precio_auto = 1500
precio_moto = 500
precio_camion = 3500

cant_autos = 0
cant_motos = 0
cant_camiones = 0

total_dinero = 0

while True:
    tipo_vehiculo = input("Tipo de vehículo: ").lower()

    match tipo_vehiculo:
        case "auto":
            cant_autos += 1
            total_dinero += precio_auto
        case "moto":
            cant_motos += 1
            total_dinero += precio_moto
        case "camion":
            cant_camiones += 1
            total_dinero += precio_camion
        case "salir":
            break
        case _:
            print("Ingrese una opción válida")

total_vehiculos = cant_autos + cant_motos + cant_camiones

print(f"Ganancias totales: ${total_dinero}\n% de vehículos transitados:")
print(f"Autos: {(cant_autos/total_vehiculos)*100}%")
print(f"Motos: {(cant_motos/total_vehiculos)*100}%")
print(f"Camiones: {(cant_camiones/total_vehiculos)*100}%")