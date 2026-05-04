bitcoin = 0.05
precio_compra = 50000
precio_hoy = 62000
dolar = 900

ganancia_usd = (precio_hoy - precio_compra) * bitcoin
ganancia_pesos = ganancia_usd * dolar

print(f"dinero ganado en pesos chilenos invirtiendo en Bitcoin: {ganancia_pesos}")