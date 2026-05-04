bitcoin_comprada = 0.05
precio_btc_compra = 50000
precio_btc_hoy =  62000
dolar = 900
precio_1 = 0
precio_2 = 0

print(f"Compraste {bitcoin_comprada} BTC, en ese tiempo una BTC tenia el precio de ${precio_btc_compra}USD")
precio_1 = precio_btc_compra * bitcoin_comprada
print(f"El precio que te salio fue de ${precio_1}USD, unos ${precio_1 * 900}CLP")

print(f"Hoy en dia un BTC cuesta ${precio_btc_hoy}CLP")
precio_2 = precio_btc_hoy * bitcoin_comprada
print(f"Es decir que mi {bitcoin_comprada} BTC ahora cuesta un total de ${precio_2}USD, unos ${precio_2 * 900} CLP")
print(f"En total he ganado ${precio_2 - precio_1}USD, unos ${(precio_2 - precio_1) * 900}CLP")