compra_btc = 0.05
btc_antigo = 50000 
btc_astual = 62000
peso_chileno = 900

bts_valor = btc_astual - btc_antigo
ganancia = bts_valor * compra_btc
ganancia_peso_chileno = ganancia * peso_chileno

print(f"estarias ganado de los btc :{ganancia_peso_chileno } en pesos chilenos")
