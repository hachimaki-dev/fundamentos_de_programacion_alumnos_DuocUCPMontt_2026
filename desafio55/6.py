btc_comprado = 0.05

valor_antiguo_btc = 50000

valor_nuevo_btc = 62000

valor_dolar_clp = 900

#_____________________________________


ganancia_btc = valor_nuevo_btc - valor_antiguo_btc

ganancia_btc = ganancia_btc * btc_comprado

ganancia_btc = ganancia_btc * valor_dolar_clp

#_______________________________________

print(ganancia_btc)
