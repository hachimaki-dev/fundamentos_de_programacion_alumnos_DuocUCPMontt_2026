tipo_de_vehiculo1 = "camion"
tipo_de_vehiculo2 = "auto"
velocidad_limite_camion = 80
velocidad_limite_auto = 120
velocidad_camion = 95
velocidad_auto = 0
if (tipo_de_vehiculo1 == "camion" and velocidad_limite_camion < velocidad_camion) or (tipo_de_vehiculo2 == "auto" and velocidad_limite_auto < velocidad_auto):
    if tipo_de_vehiculo1 == "camion":
        print("--Multa grave camion--")
    elif tipo_de_vehiculo2 == "auto":
        print("--multa gravisima--")



