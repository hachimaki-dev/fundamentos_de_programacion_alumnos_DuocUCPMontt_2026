compra_BTC = 0.05
valor_BTC_antes = 50000
valor_BTC_ahora = 62000
peso_chileno = 900

ganancia_por_BTC = valor_BTC_ahora - valor_BTC_antes
ganancia = ganancia_por_BTC
total_a_peso_chileno = ganancia * compra_BTC
total_final =  total_a_peso_chileno * peso_chileno

print (f"total de ganancia en pesos: {total_final}")