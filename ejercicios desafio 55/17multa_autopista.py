tipo_de_auto = "camion"
velocidad_kmh = 95
if tipo_de_auto == "auto" and velocidad_kmh > 120:
    print("multa gravisima")
elif tipo_de_auto == "camion" and velocidad_kmh > 80:
    print("multa grave camion")
else:
    print("sin multa")