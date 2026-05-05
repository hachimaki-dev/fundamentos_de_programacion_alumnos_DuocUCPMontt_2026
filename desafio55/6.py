#Ejercicio 6: Ganancia en Criptomonedas (Binance)
#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.

#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.

#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.

#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.

#Resultado esperado en consola:
#540000.0


un_bitcoin = 50000
precio_hoy_bitcoin = 62000
precio_dolar = 900
compra_inicial = 0.05

diferencia_precios = precio_hoy_bitcoin - un_bitcoin 

ganancia = diferencia_precios * compra_inicial

ganancia_clp = ganancia * precio_dolar

print(ganancia_clp)
