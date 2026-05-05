#Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

#Datos Iniciales: Estacionar la primera hora cuesta 1200. Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.

#Reglas de Negocio: La primera hora se cobra a 1200. Las 2 horas que sobran equivalen a 4 bloques de media hora extra.

#Restricciones: Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.

costo_primera_hora = 1200
costo_horas_extras = 500
tiempo_extra = 4

total_a_pagar = costo_primera_hora + (costo_horas_extras * tiempo_extra)
print(f"Total a pagar {total_a_pagar}")