#Ejercicio 10: Estacionamiento Aeropuerto
#Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

#Datos Iniciales: Estacionar la primera hora cuesta 1200. Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.

#Reglas de Negocio: La primera hora se cobra a 1200. Las 2 horas que sobran equivalen a 4 bloques de media hora extra.

#Restricciones: Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.

"costo por estacionamiento"

#por una hora de estacionamiento



horas_estacionadoo = 3
hora = 1200
cada_media_hora_despues_de_la_hora = 500


costo_por_estacionamiento = hora + cada_media_hora_despues_de_la_hora * 4 

horas_estacionadoo = costo_por_estacionamiento
print(f"el costo total por estacionamiento es: {costo_por_estacionamiento}")
 
 