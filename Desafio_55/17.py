camion = "camion"
auto = "auto"

velocidad_vehiculo = 95

velocidaad_maxima_autos = 120
velocidad_maxima_camion = 80

if velocidad_vehiculo > velocidad_maxima_camion:
    print("Multa grave camion")
elif velocidad_vehiculo > velocidaad_maxima_autos:
    print("multa gravisima")


