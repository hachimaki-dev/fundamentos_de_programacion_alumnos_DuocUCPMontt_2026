vehiculo = "Camion"
velocidad = 95
resultado = "Sin multa"
if vehiculo == "Auto" and velocidad >120:
    resultado = "multa Gravisima"
elif  vehiculo == "Camion" and velocidad >80:
    resultado = "Multa grave Camion"
print(resultado)