btc_cantidad = 0.05
precio_compra = 50000
precio_actual = 62000
tipo_cambio = 900

ganancia_por_btc = precio_actual - precio_compra
total_ganado_usd = ganancia_por_btc * btc_cantidad
total_ganado_clp = total_ganado_usd * tipo_cambio

print(f"${total_ganado_clp}, CLP")