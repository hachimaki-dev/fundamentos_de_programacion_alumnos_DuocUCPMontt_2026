tipo_vehiculo = "Camion"
velocidad = 95 
if tipo_vehiculo == "Auto" and velocidad > 120:
    print("Multa Gravisima")
elif tipo_vehiculo == "Camion" and velocidad > 80:
    print("Multa Grave Camion")
elif(tipo_vehiculo == "Auto" and velocidad <= 120) or (tipo_vehiculo == "Camion" and velocidad <= 80):
    print("No hay multa")