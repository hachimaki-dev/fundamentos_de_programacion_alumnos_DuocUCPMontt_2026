comprado = 0.05 #bitcoin
valor_bitcoin = 50000
valor_btc_hoy = 62000
valor_dolar = 900

diferencia_precios = valor_btc_hoy - valor_bitcoin


total_dolares_en_btc = diferencia_precios * comprado * valor_dolar
print(f"tienes un total de {total_dolares_en_btc} dolares")

