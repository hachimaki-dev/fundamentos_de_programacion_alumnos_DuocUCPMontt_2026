bitcoin_adquirido = 0.05

valor_bitcoin_antes_dolar = 50000

valor_bitcoin_hoy_dolar = 62000 

dolar = 900


#calculo de diferencia entre precio actual y el antiguo
diferencia_bitcoin_dolar = valor_bitcoin_hoy_dolar - valor_bitcoin_antes_dolar
"calculo de ganancia o perdida en dolar"
gananca_perdida_dolar = diferencia_bitcoin_dolar * bitcoin_adquirido
"calculo de ganancia o perdida en pesos"
ganancia_perdida_pesos = gananca_perdida_dolar * dolar 
print(F"la ganancia o perdida en pesos es: {ganancia_perdida_pesos}")

