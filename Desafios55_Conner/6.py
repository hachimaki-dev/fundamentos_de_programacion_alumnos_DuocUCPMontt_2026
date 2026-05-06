#Ejercicio 6: Ganancia en Criptomonedas (Binance)
#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares.
#Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC.
#Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.

mis_bitcoins=0.05
valor_btc=50000
actual_btc=62000
dolar=900

btc_dlr=mis_bitcoins*valor_btc
print(btc_dlr)
btc_clp=btc_dlr*0.9
print(btc_clp)

ganancia_btc=actual_btc-valor_btc
ganancia_dlr=ganancia_btc*mis_bitcoins
ganancia_clp=ganancia_dlr*dolar
print(ganancia_clp)