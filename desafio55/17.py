Velocidad_camion = 95
Velocidad_vehiculo = 100
Vehiculo = "Auto"
Camion = "Camion"
if Vehiculo == "Auto" and Velocidad_vehiculo <=120:
  print("No hay multa para auto.")
  if Camion == "Camion" and Velocidad_camion > 80:
    print("Multa Grave Camion.")
