"""
Ejercicio 6: Ganancia en Criptomonedas (Binance)
Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. 
Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para 
saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. 
Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia 
total en pesos.

Resultado esperado en consola:
540000.0
"""

compra = 0.05 

btc_antiguo = 50000
btc_actual = 62000
dolar_a_peso_chileno = 900


# Calcula la diferencia entre el precio actual y el antiguo
diferencia = btc_actual - btc_antiguo
# Multiplica eso por la cantidad de BTC que tienes.
ganado_dolares = diferencia * compra
# Finalmente, conviértelo a pesos chilenos.
ganado = ganado_dolares * dolar_a_peso_chileno

print(f"El total de tu ganancia es de: ${ganado:,}")