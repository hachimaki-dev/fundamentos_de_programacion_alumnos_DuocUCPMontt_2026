#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.
#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.
#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC.
#Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.
#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.
compra_btc = 0.05 
BTC_pasado = 50000 
BTC_actual = 62000
dolar = 900
diferencia_BTC = BTC_actual - BTC_pasado
total_dolares = diferencia_BTC * compra_btc
total_chilenos = total_dolares * 900
print(total_chilenos)