btc_comprado = 0.05
valor_btc_antes = 50000
valor_btc_actual = 62000
valor_dolar = 900

diferencia = (valor_btc_actual - valor_btc_antes)

total_dolares = diferencia * btc_comprado
ganancia_pesos_chilenos = (total_dolares * valor_dolar)


print(f"Ganaste {ganancia_pesos_chilenos} en pesos chilenos. ")