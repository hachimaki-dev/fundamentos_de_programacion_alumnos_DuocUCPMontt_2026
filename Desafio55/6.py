compra_btc = 0.05
valor_btc_antes = 50000
valor_btc_ahora = 62000
valor_dolar = 900
dierencia_entre_btc = valor_btc_ahora - valor_btc_antes
total_en_dolares = dierencia_entre_btc * compra_btc
total_chileno = total_en_dolares * valor_dolar
print(total_chileno)