vehículo = "Camión"
velocidad_vehículo = 95 #Km/h
lim_autos = 120 #Km/h
lim_camiones = 80 #Km/h
if vehículo == "Camión" and velocidad_vehículo > lim_camiones:
    print("Multa Grave Camión")
elif vehículo != "Camión" and velocidad_vehículo > lim_autos:
    print("Multa Gravísima")
else:
    print("Velocidad adecuada")