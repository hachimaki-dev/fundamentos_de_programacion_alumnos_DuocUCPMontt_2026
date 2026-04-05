#inicialización de contadores 
autos = 0
camiones = 0 
motos = 0 
total = 0

while True:
    tipo = input("Ingrese el tipo de vehículo (auto, camión, moto) o 'salir' para terminar: ")

    if tipo == "SALIR":
        break
    elif tipo == "AUTO":
        autos += 1
        total += 1500
    elif tipo == "CAMIÓN":
        camiones += 1
        total += 3500
    elif tipo == "MOTO":
        motos += 1
        total += 500

    else:
        print("Tipo de vehículo no válido. Intente nuevamente.")
    #cierre de caja
total_vehiculos = autos + camiones + motos
print("\n---Cierre de caja---")               
print(f"Total de autos: {autos}")
print(f"Total de camiones: {camiones}")
print(f"Total de motos: {motos}")
print(f"Ganancia total: ${total}")

#determinar el vehículo más frecuente
if total_vehiculos > 0:
    if autos >= camiones and autos >= motos:
        GANADOR = "Auto"
        porcentaje = (autos / total_vehiculos) * 100
        print("El vehículo más frecuente fue: Auto")
    elif camiones >= autos and camiones >= motos:
        GANADOR = "Camión" 
        porcentaje = (camiones / total_vehiculos) * 100
        print("El vehículo más frecuente fue: Camión")
    else:
        GANADOR = "Moto"
        porcentaje = (motos / total_vehiculos) * 100
        print("El vehículo más frecuente fue: Moto")

else:    
    ganador = "empate!"
    porcentaje = 0
    print("No se registraron vehículos.")