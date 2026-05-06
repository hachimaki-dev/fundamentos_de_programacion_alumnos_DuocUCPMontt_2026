vehiculo = "camion"
velocidad = 95
if vehiculo == "auto" and velocidad > 120:
    print("multa gravisima")
elif vehiculo == "camion" and velocidad > 80:
    print("multa grave camion")
else: 
    print("sin multa")