btc_comprado = 0.05
valor_antes_btc = 50000
valor_ahora_btc = 62000
valor_dolar = 900
diferecia_precio = valor_ahora_btc - valor_antes_btc
total_ganado = diferecia_precio*btc_comprado
total_ganado = total_ganado*valor_dolar
print(f"has ganado un total de {total_ganado} pesos")