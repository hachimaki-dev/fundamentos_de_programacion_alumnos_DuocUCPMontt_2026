compra_BTC = 0.05
valor_BTC_antes = 50000 
valor_BTC_ahora = 62000 
valor_dolar = 900

diferencia_precio = valor_BTC_ahora - valor_BTC_antes
total_ganado_dolares = diferencia_precio * compra_BTC
conversion_pesochileno = total_ganado_dolares * valor_dolar
print(conversion_pesochileno)