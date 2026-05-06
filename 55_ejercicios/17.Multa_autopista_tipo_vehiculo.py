vehiculo = "Camion"
velocidad_vehiculo = 95

if vehiculo == "Camion":
    if velocidad_vehiculo > 80:
        print("Multa Grave Camión")
    elif velocidad_vehiculo <= 80:
        print("No hay multa")
elif vehiculo == "Auto":
    if velocidad_vehiculo > 120:
        print("Multa Gravísima")
    elif velocidad_vehiculo <= 120:
        print("No hay multa")