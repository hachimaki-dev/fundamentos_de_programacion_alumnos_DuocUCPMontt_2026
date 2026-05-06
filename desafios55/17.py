tipo_vehiculo = "Camion"
velocidad = 95

limite_auto = 120
limite_camion = 80

if tipo_vehiculo == "Auto" and velocidad > limite_auto:
    print("Multa Gravísima")
elif tipo_vehiculo == "Camion" and velocidad > limite_camion:
    print("Multa Grave Camión")
else:
    print("Sin multa")