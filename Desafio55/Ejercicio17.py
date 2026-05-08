"""Ejercicio 17: Multa Autopista por Tipo de Vehículo
Programa la cámara de la carretera para sacar multas según el vehículo.

Datos Iniciales: Pasó un 'Camion' a 95 km/h.

Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima'). 

Los camiones son más pesados y no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

Restricciones: Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) en la misma línea con un `and`. 

Imprime la multa correspondiente para el camión."""
Tipo_vehiculo = "Camion"

Velocidad_Camion = 95

Velocidad_Auto = 0

Velocidad_Maxima_Camion = 80

Velocidad_Maxima_Auto = 120

if Velocidad_Auto > Velocidad_Maxima_Auto and Tipo_vehiculo == "Auto":
    print("Multa gravisima")
elif Velocidad_Camion > Velocidad_Maxima_Camion and Tipo_vehiculo == "Camion":
    print("Multa grave Camion")
else:
    print("No hay multa")