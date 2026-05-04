#Quieres saber cuánta plata ganaste invirtiendo en Bitcoin.
#Datos Iniciales: Compraste 0.05 BTC. Cuando compraste, 1 BTC valía 50000 dólares. Hoy, 1 BTC vale 62000 dólares. El dólar está a 900 pesos chilenos.
#Reglas de Negocio: Calcula la diferencia entre el precio actual y el antiguo para saber cuánto ganaste por cada BTC. Multiplica eso por la cantidad de BTC que tienes. Ese será tu total ganado en dólares. Finalmente, conviértelo a pesos chilenos.
#Restricciones: Haz los cálculos paso a paso usando variables. Imprime sólo la ganancia total en pesos.
bitcoin_comprado = 0.05
precio_antiguo = 50000
precio_nuevo = 62000
dolar = 900
ganancia = precio_nuevo - precio_antiguo
ganancia_usd = ganancia * bitcoin_comprado
ganancia_clp = ganancia_usd * dolar 

print(f"tu ganancia es de: {ganancia_clp}")