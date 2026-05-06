#jercicio 10: Estacionamiento Aeropuerto
#as a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

#atos Iniciales: Estacionar la primera hora cuesta 1200. 
# Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.

#eglas de Negocio: La primera hora se cobra a 1200. 
# Las 2 horas que sobran equivalen a 4 bloques de media hora extra.

#estricciones: Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.

#esultado esperado en consola:
#3200


estacionamiento_por_hora = 1200
media_hora_exta_estacionamiento = 500
total_hora_estacionado = 3
bloque_por_hora = 4


total_estacionamiento = estacionamiento_por_hora +(bloque_por_hora*media_hora_exta_estacionamiento)
print(total_estacionamiento)