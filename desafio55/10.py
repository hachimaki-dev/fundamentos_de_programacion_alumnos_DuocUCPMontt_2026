"""
Ejercicio 10: Estacionamiento Aeropuerto
Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

Datos Iniciales: Estacionar la primera hora cuesta 1200. Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.

Reglas de Negocio: La primera hora se cobra a 1200. Las 2 horas que sobran equivalen a 4 bloques de media hora extra.

Restricciones: Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.
"""

tiempo_en_estacionamiento = 3
valor_total_estacionamiento = 0

#Transformar el tiempo en horas en bloques de 30 MIN

tiempo_en_estacionamiento *= 2

if tiempo_en_estacionamiento >= 2:
    valor_total_estacionamiento += 1200
    tiempo_en_estacionamiento -= 2
    if tiempo_en_estacionamiento > 2:
        cobro_extra = tiempo_en_estacionamiento * 500
        valor_total_estacionamiento += cobro_extra

print(f"El total es de {valor_total_estacionamiento}")