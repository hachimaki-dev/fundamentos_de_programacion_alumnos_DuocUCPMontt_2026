
tipo_vehiculo = "Camion"
velocidad = 95


if tipo_vehiculo == "Auto" and velocidad > 120:
    print("Multa Gravísima")
elif tipo_vehiculo == "Camion" and velocidad > 80:
    print("Multa Grave Camión")
else:
    print("Sin multa")
