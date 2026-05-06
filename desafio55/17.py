velocidad_camion= 95 #Km
velocidad_maxima_camion= 80
velocidad_maxima_auto= 120
tipo_vehiculo= "camion"

if tipo_vehiculo == "camion" and velocidad_camion > velocidad_maxima_camion:
    print("Multa Grave Camion")
else:
    print("No hay multa")