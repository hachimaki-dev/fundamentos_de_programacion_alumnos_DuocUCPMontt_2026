btc = 0.05
antes_btc = 50000
btc_hoy = 62000

diferencia_btc = btc_hoy - antes_btc

calculo = diferencia_btc * btc

pesos_chilenos = calculo * 900


print(f"La ganancia total es {pesos_chilenos}")