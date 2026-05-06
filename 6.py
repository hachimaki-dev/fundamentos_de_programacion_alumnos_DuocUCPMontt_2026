BTC_comprados = 0.05
Bitcoin_actual = 62000
un_dolar_en_chile = 900
bitcoin_anterior = 50000

diferencia = Bitcoin_actual - bitcoin_anterior

bitcoins_ganados = diferencia * BTC_comprados

en_peso_chileno = bitcoins_ganados * un_dolar_en_chile

print(f"ganancia total de {en_peso_chileno}")
