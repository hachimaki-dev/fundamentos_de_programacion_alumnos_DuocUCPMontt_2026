cantidad_btc = 0.05
precio_compra = 50000
precio_actual = 62000
valor_dolarsh = 900

diferencia_usd = precio_actual - precio_compra
ganancia_usd = diferencia_usd * cantidad_btc
ganancia_clp = ganancia_usd * valor_dolarsh
print("La ganancia total el pesos es: ", ganancia_clp)



