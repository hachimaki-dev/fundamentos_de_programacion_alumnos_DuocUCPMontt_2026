btc_comprado = 0.05
precio_btc_al_comprar = 50000
precio_btc_hoy = 62000
dolar = 900
valor_btc_comprado = btc_comprado * precio_btc_al_comprar
valor_btc_comprado_hoy = btc_comprado * precio_btc_hoy
ganancia_total = valor_btc_comprado_hoy - valor_btc_comprado
valor_pesos = ganancia_total * dolar
print(valor_pesos)