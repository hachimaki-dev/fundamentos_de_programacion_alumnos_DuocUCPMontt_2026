BTC_comprado = 0.05
PrimerValorBTC = 50000
SegundoValorBTC= 62000
valor_dolar_a_CLP = 900
btcdiff = (SegundoValorBTC - PrimerValorBTC)* BTC_comprado
dolares_a_CLP = btcdiff * 900

print(dolares_a_CLP)