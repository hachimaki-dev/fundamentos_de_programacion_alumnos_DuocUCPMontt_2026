vehiculo = "Camion"
velocidad = 95

if vehiculo == "Auto" and velocidad > 120:
    print("Multa Gravisima")
elif vehiculo == "Camion" and velocidad > 80:
    print("Multa Grave Camion")
else:
    print("Sin multa")