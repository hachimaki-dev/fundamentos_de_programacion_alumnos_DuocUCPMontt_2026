btc_comprados = 0.05
precio_antiguo = 50000
precio_actual = 62000
valor_del_dolar = 900

diferencia = precio_actual - precio_antiguo
ganancia_dolar = diferencia * btc_comprados

ganancia_clp = ganancia_dolar * valor_del_dolar

print(ganancia_clp)