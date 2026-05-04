# Ganancia en Criptomonedas (Binance)
compre_BTC1 = 0.05
compre_BTC2 = 1 * 50000 # El valor del BTC
valor_actual_BTC = 62000 
dolar_peso_chileno = 900  
diferencia_de_precio = valor_actual_BTC - compre_BTC2
ganancia_total_BTC = diferencia_de_precio * compre_BTC1
ganancia_final = ganancia_total_BTC * dolar_peso_chileno
print('Gabnancia total por pesos es:', ganancia_final)