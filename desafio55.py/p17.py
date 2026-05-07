vehiculo = "camion"
velocidad = 95
maximo_camion = 80
maximo_auto = 120

if vehiculo == "auto" and velocidad > maximo_auto:
    print("Multa gravisima")
elif vehiculo == "camion" and velocidad > maximo_camion:
    print("Multa grave camion")
else:
    print("Sin multa")