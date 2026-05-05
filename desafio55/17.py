velocidad = 95
camion = "camion"
auto = 120
auto = "auto"
limite_camion = 80
limite_auto = 120

vehiculo = input("¿Que tipo de vehículo es?")
kmh = int(input("¿A cuanta velocidad pasó?"))

if vehiculo == camion and kmh >= limite_camion:
    print("Multa Grave Camión")

if vehiculo == auto and kmh >= limite_auto:
    print("Multa Gravísima")

else:
    kmh < limite_camion and kmh < limite_auto
    print("no hay multa.")



