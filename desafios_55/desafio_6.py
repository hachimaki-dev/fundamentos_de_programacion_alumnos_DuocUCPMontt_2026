compra_bitcoin = 0.05
precio_bitcoin_antes = 50000
precio_bitcoin_actual = 62000
dolar = 900

diferencia_precio_bitcoin = precio_bitcoin_actual - precio_bitcoin_antes
total_ganado = compra_bitcoin * diferencia_precio_bitcoin
transformacion_clp = total_ganado * dolar

print(f"La ganancia total es de: ${transformacion_clp} CLP")