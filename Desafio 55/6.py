dolar_a_peso_chileno = 900

precio_btc_antes = 50000
precio_btc_ahora = 62000

btc_comprados =  0.05

diferencia_precio_btc = precio_btc_ahora - precio_btc_antes

total_ganado_en_dolares = diferencia_precio_btc * btc_comprados
total_ganado_en_pesos_chilenos = total_ganado_en_dolares * dolar_a_peso_chileno

print(total_ganado_en_pesos_chilenos)