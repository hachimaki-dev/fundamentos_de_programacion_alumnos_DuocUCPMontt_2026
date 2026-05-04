btc_comprado = 0.05
precio_compra = 50000
precio_actual = 62000
dolar_pesos = 900

ganancia_por_btc = precio_actual - precio_compra
ganancia_dolares = ganancia_por_btc * btc_comprado
ganancia_pesos = ganancia_dolares * dolar_pesos
print(ganancia_pesos)