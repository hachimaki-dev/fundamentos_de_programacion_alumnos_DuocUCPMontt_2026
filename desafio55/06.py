saldo_btc = 0.05
precio_btc_inicial = 50000 # USD
precio_btc_actual = 62000 # USD
precio_usd = 900 # CLP

diferencia_precios_btc = precio_btc_actual - precio_btc_inicial
ganancia_usd = diferencia_precios_btc * saldo_btc
ganancia_clp = ganancia_usd * precio_usd

print(ganancia_clp)
