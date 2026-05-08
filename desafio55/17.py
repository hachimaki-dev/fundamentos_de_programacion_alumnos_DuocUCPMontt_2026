"""
🟡 Rango: Cuidado
Ejercicio 17: Multa Autopista por Tipo de Vehículo
Programa la cámara de la carretera para sacar multas según el vehículo.

Datos Iniciales: Pasó un 'Camion' a 95 km/h.

Reglas de Negocio: Los autos no pueden pasar de 120 km/h (si se pasan, es 
'Multa Gravísima'). Los camiones son más pesados y no pueden pasar de 80 km/h 
(si se pasan, es 'Multa Grave Camión'). Si van bajo sus límites, no hay multa.

Restricciones: Usa `if/elif` evaluando ambas cosas (el tipo de vehículo y la velocidad) 
en la misma línea con un `and`. Imprime la multa correspondiente para el camión.

Resultado esperado en consola:
Multa Grave Camión
"""

kilometraje_camion = 95

tipo_1 = "camion"
tipo_2 = "Auto"
maximo_autos = 120
maximo_camiones = 80