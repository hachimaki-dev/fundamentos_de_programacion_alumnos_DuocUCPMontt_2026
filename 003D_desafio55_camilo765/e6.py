btc = 0.05
precio_compra = 50000
precio_actual = 62000
dolar_clp = 900
gan_por_btc = precio_actual - precio_compra
gan_usd = gan_por_btc * btc
gan_clp = gan_usd * dolar_clp

print(int(gan_clp))