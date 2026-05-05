tengo_btc = 0.05
precio_antiguo_btc = 50000
precio_actual_btc = 62000
valor_dolar_a_chileno = 900

diferencia_precio_btc = precio_actual_btc - precio_antiguo_btc

ganancias = tengo_btc * diferencia_precio_btc

ganancias_total = ganancias * valor_dolar_a_chileno

print("ganancias totales por vender BTC:", ganancias_total)
