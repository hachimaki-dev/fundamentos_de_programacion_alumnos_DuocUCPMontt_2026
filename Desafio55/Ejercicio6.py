"""Ejercicio 6: Ganancia en Criptomonedas (Binance)
Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. 

Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos."""

BTC_ANTIGUO = 50000 #Dolares

BTC_ACTUAL = 62000 #Dolares

TU_BTC = 0.05 #Cantidad de BTC

Pesos_CHILENOS = 900 #Pesos chilenos

Diferencia = BTC_ACTUAL - BTC_ANTIGUO

Diferencia = Diferencia * TU_BTC

Diferencia = Diferencia * Pesos_CHILENOS

print(Diferencia)