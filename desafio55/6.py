compra_btc = 0.05
un_btc_antes = 50000
un_btc_ahora = 62000
dolar = 900
diferencia_btc = un_btc_ahora - un_btc_antes
ganancia_usd = diferencia_btc*compra_btc
ganancia_clp = ganancia_usd*dolar
print(ganancia_clp)