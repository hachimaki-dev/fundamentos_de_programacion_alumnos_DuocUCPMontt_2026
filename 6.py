cantidad_btc = 0.05 
precio_compra_btc = 50000
valor_actual_btc = 62000 
valor_dolar_peso_chileno = 900

diferencia_por_btc = valor_actual_btc - precio_compra_btc

ganancia_usd = diferencia_por_btc * cantidad_btc        
ganacia_clp = valor_dolar_peso_chileno * ganancia_usd

print(ganacia_clp)

