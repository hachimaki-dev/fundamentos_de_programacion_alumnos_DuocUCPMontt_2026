billetera_de_btc = 0.05
dia_de_compra_btc = 50000
hoy_en_dia_btc = 62000
dolar = 900

diferencia = hoy_en_dia_btc - dia_de_compra_btc
ganancia = diferencia * billetera_de_btc
ganancia_en_dolares = ganancia *dolar
print(f"ganancia en pesos es {ganancia_en_dolares}")