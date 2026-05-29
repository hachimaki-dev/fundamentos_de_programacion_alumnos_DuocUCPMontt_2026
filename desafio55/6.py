compra_BTC = 0.05
valor_al_comprar = 50000 #1 BTC
valor_hoy = 62000
dolar_a_peso = 900
diferencia_precios = valor_hoy - valor_al_comprar
total_dolares = diferencia_precios * compra_BTC
total_pesos = total_dolares * dolar_a_peso
print(total_pesos)