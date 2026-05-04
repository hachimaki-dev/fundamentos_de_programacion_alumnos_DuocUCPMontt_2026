#🟡 Rango: Cuidado
#Ejercicio 10: Estacionamiento Aeropuerto
#Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

#Datos Iniciales: Estacionar la primera hora cuesta 1200. Después de eso, cada media hora extra cuesta 500. Estuviste estacionado 3 horas en total.

#Reglas de Negocio: La primera hora se cobra a 1200. Las 2 horas que sobran equivalen a 4 bloques de media hora extra.

#Restricciones: Calcula el total sumando el precio de la primera hora más los bloques extra multiplicados por su valor. Imprime el costo total.

precio_hora_inicial = 1200
precio_media_hora = 500
cantidad_medias_horas = 4

print(f"El valor final de tu tarifa por estacionar en el aeropuerto por 3 horas sería de: $", precio_hora_inicial + precio_media_hora * cantidad_medias_horas ," pesos")