""" Ejercicio 17: Multa Autopista por Tipo de Vehículo
Programa la cámara de la carretera para sacar multas según el vehículo.

Datos Iniciales: Pasó un 'Camion' a 95 km/h.

Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima'). Los camiones son más pesados y 
no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

Restricciones: Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) en la misma línea con un `and`. 
Imprime la multa correspondiente para el camión."""


camion_de_paso = 95
auto = 0
if auto > 120:
    print("munta gravisima")
elif camion_de_paso > 80:
    print("multa grave camion")
elif camion_de_paso <= 80:
    print("no hay multa")
