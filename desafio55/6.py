saldo_BTC = 0.05
valor_BTC = 50000
valor_BTC_actual = 62000
valor_dolar = 900
diferencia_precios_BTC = valor_BTC_actual - valor_BTC
mi_BTC = diferencia_precios_BTC * saldo_BTC
mi_saldo_actual = mi_BTC * 900
print(f"Actualmente tu BTC vale {mi_saldo_actual}")
