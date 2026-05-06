Velocidad_camion = 95
Velocidad_vehiculo = 100
Vehiculo = input("Cual es tu vehiculo? ")
if Vehiculo == "Auto" and Velocidad_vehiculo <=120:
  print("No hay multa para auto.")
elif Vehiculo == "Camion" and Velocidad_camion > 80:
    print("Multa Grave Camion.")
