compra_btc = 0.05
precio_antiguo = 50000
precio_actual = 62000
dolar = 900

diferencia_btc = (precio_actual - precio_antiguo)
diferencia_dolar = (diferencia_btc * compra_btc)
total_peso_chl = (diferencia_dolar * dolar)

print(total_peso_chl)
