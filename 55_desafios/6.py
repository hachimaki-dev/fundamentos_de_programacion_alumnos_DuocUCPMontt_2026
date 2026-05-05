#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.
#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.

precio_btc_antes = 50000
precio_btc_ahora = 62000
btc_propios = 0.05
valor_btc_propio_antes = precio_btc_antes * 0.05
valor_btc_propio_ahora = precio_btc_ahora * 0.05

ganancia = valor_btc_propio_ahora - valor_btc_propio_antes
btc_pesos = ganancia * 900
print(f"{btc_pesos}")