btc_comprados = 0.05
precio_antiguo = 50000
precio_nuevo = 62000
dolar_precio = 900
diferencia_precios = precio_nuevo - precio_antiguo
ganancia = diferencia_precios * btc_comprados
ganancia_final = ganancia * dolar_precio
print(f"La ganancia es de: {ganancia_final}")