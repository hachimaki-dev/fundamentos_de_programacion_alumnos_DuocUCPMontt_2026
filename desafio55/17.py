tipo_vehiculo = "camion"
velocidad = 95

if tipo_vehiculo == "auto" and velocidad > 120:
    print("Multa Grave")
elif tipo_vehiculo == "camion" and velocidad > 80:
    print("Multa Grave Camión")