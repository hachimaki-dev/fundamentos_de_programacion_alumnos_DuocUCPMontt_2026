precio_autos = 1500
precio_camiones = 3500
precio_motos= 500

contador_autos = 0
contador_camiones = 0
contador_motos = 0
dinero_recaudado = 0

def limpiarConsola():
    print("\033[H\033[J", end="") # Limpia la consola con códigos de escape

while True:
    tipo_vehiculo = input('\nIngrese el tipo de vehículo cobrado. "A" para auto, "C" para camión y "M" para moto. Para salir del programa, escriba "SALIR".\n')
    tipo_vehiculo = tipo_vehiculo.lower()

    if tipo_vehiculo == "a" or tipo_vehiculo == "auto":
        contador_autos += 1
        dinero_recaudado += precio_autos
        limpiarConsola()
        print(f"Auto cobrado. Ganancia: ${precio_autos}    Ganancia total hasta ahora: ${dinero_recaudado}")
    
    elif tipo_vehiculo == "c" or tipo_vehiculo == "camion":
        contador_camiones += 1
        dinero_recaudado += precio_camiones
        limpiarConsola()
        print(f"Camión cobrado. Ganancia: ${precio_camiones}    Ganancia total hasta ahora: ${dinero_recaudado}")
    
    elif tipo_vehiculo == "m" or tipo_vehiculo == "moto":
        contador_motos += 1
        dinero_recaudado += precio_motos
        limpiarConsola()
        print(f"Moto cobrada. Ganancia: ${precio_motos}    Ganancia total hasta ahora: ${dinero_recaudado}")

    elif tipo_vehiculo == "salir":
        limpiarConsola()
        print("\n/// CIERRE DE CAJA ///")
        print(f"Ganancia total: ${dinero_recaudado}")
        print(f"Autos cobrados: {contador_autos}    Camiones cobrados: {contador_camiones}    Motos cobradas: {contador_motos}")

        if contador_autos > contador_camiones and contador_autos > contador_motos: # Si pasaron más autos
            print("Los autos fueron los vehículos que más pasaron en el día.")
        elif contador_camiones > contador_autos and contador_camiones > contador_motos: # Si pasaron más camiones
            print("Los camiones fueron los vehículos que más pasaron en el día.")
        elif contador_motos > contador_autos and contador_motos > contador_camiones: # Si pasaron más motos
            print("Las motos fueron los vehículos que más pasaron en el día.")
        elif contador_autos < contador_camiones and contador_autos < contador_motos: # Si pasaron más camiones y motos
            print("Los camiones y las motos fueron los vehículos que más pasaron en el día.")
        elif contador_camiones < contador_autos and contador_camiones < contador_motos: # Si pasaron más autos y motos
            print("Los autos y las motos fueron los vehículos que más pasaron en el día.")
        elif contador_motos < contador_autos and contador_motos < contador_camiones: # Si pasaron más autos y camiones
            print("Los autos y los camiones fueron los vehículos que más pasaron en el día.")
        else: # Si todos los vehículos pasaron en la misma cantidad
            print("Todos los vehículos pasaron en la misma cantidad.")

        break

    else:
        limpiarConsola()
        print("ERROR: Tipo de vehículo inválido.")
