#Ejercicio 17: Multa Autopista por Tipo de Vehículo.


tipo_vehiculo =  "Camión"
velocidadv_vehiculo = 95



if tipo_vehiculo == "Camión" and velocidadv_vehiculo > 80:
    print("Multa grave camión")
elif tipo_vehiculo == "Camión" and velocidadv_vehiculo <= 80:
    print("Limite de velocidad adecuado")

if tipo_vehiculo == "auto" and velocidadv_vehiculo > 120:
    print("Multa grave auto")
if tipo_vehiculo == "auto" and velocidadv_vehiculo <= 120: 
    print("Velocidad adecuada")
