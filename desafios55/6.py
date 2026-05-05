cantidad_btc = 0.05
precio_compra = 50000
precio_actual = 62000
valor_dolar = 900

diferencia_por_btc = precio_actual - precio_compra

ganancia_usd = diferencia_por_btc * cantidad_btc

ganancia_clp = ganancia_usd * valor_dolar

print(ganancia_clp)