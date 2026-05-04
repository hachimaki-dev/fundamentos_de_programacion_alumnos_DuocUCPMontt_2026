#Rango: Inofensivo
#Ejercicio 6: Ganancia en Criptomonedas (Binance)
#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.

valor_btc_comprado = 50000
valor_btc_hoy = 62000
valor_dolar = 900
cantidad_comprada = 0.05

print(f"Cuando compraste 0,05 de bitcoin, la unidad de éste estaba a {valor_btc_comprado} dolares por lo que fue una inversión de $", valor_btc_comprado * cantidad_comprada * valor_dolar ," pesos")
inversión = valor_btc_comprado * cantidad_comprada * valor_dolar
print(f"Pero hoy el bitcoin vale {valor_btc_hoy} dolares, aumentó, por lo que tu inversión te trajo un profit de: $", valor_btc_hoy * cantidad_comprada * valor_dolar - inversión ," pesos chilenos.")