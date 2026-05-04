limite_velocidad = 120 # km/h
limite_velocidad_camiones = 80

tipo_vehiculo = "Camion"
velocidad_vehiculo = 95

if velocidad_vehiculo > limite_velocidad:
    print("Multa Gravísima")
elif tipo_vehiculo == "Camion" and velocidad_vehiculo > limite_velocidad_camiones:
    print("Multa Grave Camión")
else:
    print("Sin Multa")
