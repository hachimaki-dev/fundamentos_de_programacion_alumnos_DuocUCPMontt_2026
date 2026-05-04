btc = 0.05
precio_antiguo = 50000
precio_actual = 62000
dolar = 900

diferencia = precio_actual - precio_antiguo
ganancia_usd = diferencia * btc
ganancia_clp = ganancia_usd * dolar

print(ganancia_clp)