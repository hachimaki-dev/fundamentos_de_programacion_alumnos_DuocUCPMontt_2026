#Ejercicio 6: Ganancia en Criptomonedas (Binance)

compra =  0.05
valor_btc_ayer = 50000
valor_btc_hoy = 62000
peso_clp = 900



total = (valor_btc_hoy - valor_btc_ayer) * compra
precio_clp = total * peso_clp

print(precio_clp)
