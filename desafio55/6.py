btc_antes= 50000
btc_ahora= 62000
#el dolar vale 900 CLP
diferencia= btc_ahora - btc_antes

ganancia= diferencia * 0.05

ganancia_clp= ganancia * 900

print(f"Tu ganancia en CLP es de {ganancia_clp}")