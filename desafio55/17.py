#Ejercicio 17: Multa Autopista por Tipo de Vehículo
#Programa la cámara de la carretera para sacar multas según el vehículo.

#Datos Iniciales: Pasó un 'Camion' a 95 km/h.

#Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 
# 'Multa Gravísima'). Los camiones son más pesados y no pueden pasar de 80 km/h 
# (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

#Restricciones: Usa `if/elif` evaluando ambas cosas 
# (el tipo de vehículo y la velocidad) en la misma línea con un `and`. 
# Imprime la multa correspondiente para el camión.

#Resultado esperado en consola:
#Multa Grave Camión

velocidad_camion_kmh = 95
velocidad_permitida_camion = 80
velocidad_permitida_autos = 120
tipo_vehiculo = "auto"
tipo_camion = "camion"

if tipo_camion== "auto" and velocidad_permitida_autos <= 120:
    print("no hay multa")


elif tipo_camion == "camion" and velocidad_permitida_camion >=80:
        print(f"multa grave {tipo_camion}")




