cantidad_btc = 0.05
precio_antiguo = 50000
precio_actual = 62000
valor_dolar = 900


diferencia_por_btc = precio_actual - precio_antiguo

ganancia_usd = diferencia_por_btc * cantidad_btc

ganancia_clp = ganancia_usd * valor_dolar


print(f"Esta es la ganancia total. \n: {ganancia_clp}")