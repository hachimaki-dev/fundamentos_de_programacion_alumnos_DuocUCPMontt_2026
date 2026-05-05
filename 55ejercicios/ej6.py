# Ejercicio 6: Ganancia en Criptomonedas (Binance)

print("==============================")
print("Cálculo de ganancia en Bitcoin")
print("==============================")

btc_comprado = 0.05
precio_antiguo = 50000
precio_actual = 62000
valor_dolar = 900

ganancia_por_btc = precio_actual - precio_antiguo

ganancia_dolares = ganancia_por_btc * btc_comprado

ganancia_pesos = ganancia_dolares * valor_dolar

print(ganancia_pesos)