'''Ejercicio 17: Multa Autopista por Tipo de Vehículo
Programa la cámara de la carretera para sacar multas según el vehículo.

Datos Iniciales: Pasó un 'Camion' a 95 km/h.

Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima'). Los camiones son más pesados y no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

Restricciones: Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) en la misma línea con un `and`. Imprime la multa correspondiente para el camión.'''

limite_auto = 120
limite_camion = 80
tipo_vehiculo = "Camion"
velocidad_vehiculo = 95

if (tipo_vehiculo == "Auto" and velocidad_vehiculo > limite_auto ) or (tipo_vehiculo == "Camion" and velocidad_vehiculo > limite_camion):
    if tipo_vehiculo == "Auto":
        print("Multa Gravisima")
    else:
        print("Multa Grave Camion")
else:
    print("No hay multa")
