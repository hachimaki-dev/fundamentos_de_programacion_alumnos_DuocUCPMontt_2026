btc = 0.05
precio_btc_antes = 50000
precio_btc_actual = 62000
valor_dolar = 900

diferencia_btc = precio_btc_actual - precio_btc_antes

dolares_ganados = diferencia_btc * btc
dinero_a_pesos = dolares_ganados * valor_dolar
print(dinero_a_pesos)