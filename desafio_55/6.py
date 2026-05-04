#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.
btc_comprado = 0.05
btc_valia = 50000
valor_de_btc = 62000
dolar = 900
diferencia_de_valor = valor_de_btc - btc_valia
cantidad_de_btc_comprado = diferencia_de_valor * btc_comprado
total_en_chileno = cantidad_de_btc_comprado * dolar
print(f"la diferencia de btc con el de antes en dolares es :{diferencia_de_valor}")
print(f"cantidad de btc ganado en dolares es : {cantidad_de_btc_comprado}")
print(f"el total de btc en pesos chileno es: {total_en_chileno}")



