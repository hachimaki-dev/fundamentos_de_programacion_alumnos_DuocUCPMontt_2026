"""
Ejercicio 6: Ganancia en Criptomonedas (Binance)
Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.
"""

valor_antiguo_BTC = 50000 # 50,000
valor_actual_BTC = 62000 # 62,000 
billetera_BTC = 0.05

diferencia_BTC = valor_actual_BTC - valor_antiguo_BTC
ganancia = billetera_BTC * diferencia_BTC
ganancia_en_pesos_chilenos = billetera_BTC * 900

print(f"La ganancia total fue de ${ganancia_en_pesos_chilenos}")