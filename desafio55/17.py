tipo_vehiculo = "camion"

tipo_vehiculo1 = "auto"
tipo_vehiculo2 = "camion"

velocidad = 95

regla_camion = 80

regla_auto = 120

if tipo_vehiculo == tipo_vehiculo1 and velocidad > 120:
    print("Multa Grave")
elif tipo_vehiculo == tipo_vehiculo2 and velocidad > 80:
    print("Multa Grave Camión")
else:
    print("Velocidad adecuada, no hay multa")