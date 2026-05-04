
valor_un_btc_principio = 50000
btc_comprado = 0.05 
btc_comprado_dolares = 50000 * btc_comprado


valor_un_btc_final = 62000

diferencia_btc = valor_un_btc_final - valor_un_btc_principio
total_ganancia_dolares = diferencia_btc * 0.05
total_ganancia_clp = total_ganancia_dolares * 900

print(total_ganancia_clp)