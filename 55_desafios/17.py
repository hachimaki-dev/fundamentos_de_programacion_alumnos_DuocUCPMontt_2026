#Programa la cámara de la carretera para sacar multas según el vehículo.

#Datos Iniciales: Pasó un 'Camion' a 95 km/h.

#Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima'). Los camiones son más pesados y no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

#Restricciones: Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) en la misma línea con un `and`. Imprime la multa correspondiente para el camión.

vehiculo = "Camión"
velocidad = 95

if vehiculo == "auto" and velocidad >= 120:
    print("Multa Gravisima")
elif vehiculo == "Camión" and velocidad >= 80:
    print("Multa Grave Camión")