velocidad = 95
vehiculo = "camion"
if vehiculo == "auto" and velocidad >= 120:
    print("multa gravisima")
elif vehiculo == "camion" and velocidad >= 80:
    print("multa grave camion")
else:
    print("normal")