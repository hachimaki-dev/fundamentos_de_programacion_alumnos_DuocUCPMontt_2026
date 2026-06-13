tipo_vehiculo = int(input("Ingrese el tipo de vehículo: 1. Auto\n2.Camion\n"))
velocidad = int(input("Ingrese la velocidad del vehículo: "))
limite_auto = 120
limite_camion = 80
if tipo_vehiculo == 1:
    if velocidad > limite_auto:
        print("Multa Gravísima")
    else:
        print("Sin Multa.")
elif tipo_vehiculo == 2:
    if velocidad > limite_camion:
        print("Multa Grave Camión")
    else:
        print("Sin multa.")