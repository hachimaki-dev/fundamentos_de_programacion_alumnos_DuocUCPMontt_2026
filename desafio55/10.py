"""
🟡 Rango: Cuidado
Ejercicio 10: Estacionamiento Aeropuerto
Vas a calcular cuánto te van a cobrar por dejar el auto en el aeropuerto.

Datos Iniciales: Estacionar la primera hora cuesta 1200. Después de eso, cada media 
hora extra cuesta 500. Estuviste estacionado 3 horas en total.

Reglas de Negocio: La primera hora se cobra a 1200. Las 2 horas que sobran equivalen 
a 4 bloques de media hora extra.

Restricciones: Calcula el total sumando el precio de la primera hora más los bloques 
extra multiplicados por su valor. Imprime el costo total.

Resultado esperado en consola:
3200
"""

valor_hora = 1200
valor_media_hora = 500
bloques = 4

# suma el precio de la primera hora más los bloques extra multiplicados por su valor
# Primero vamos a sacar cuanto cuesta las 2 horas x media hora equivalente a 4 bloques
valor_media_hora = valor_media_hora * bloques

# Ahora sumamos el monto de la media hora con la de una hora
total = valor_media_hora + valor_hora

print(f"El total por las 3 horas es de: ${total}")