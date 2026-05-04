bitcoin_comprado = 0.05
precio_bitcoin_antes = 50000
precio_bitcoin_ahora = 62000
precio_dolar = 900

ganancia = precio_bitcoin_ahora - precio_bitcoin_antes

ganancia *= bitcoin_comprado

ganancia *= precio_dolar

print(ganancia)