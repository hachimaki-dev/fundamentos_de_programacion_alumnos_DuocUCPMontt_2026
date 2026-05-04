bitcoin_comprados = 0.05
precio_anterior = 50000 #dolares
precio_actual = 62000 #dolares
precio_dolar = 900 #pesos chilenos

diferencia_precio = precio_actual - precio_anterior
ganado_dolares = diferencia_precio * bitcoin_comprados

ganado_pesos = ganado_dolares * precio_dolar

print(ganado_pesos)