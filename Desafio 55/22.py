alcancia_inicial = 0
ahorro_mensual = 80000
costo_consola = 450000
contador_meses = 0

while alcancia_inicial < costo_consola :
    alcancia_inicial += ahorro_mensual
    contador_meses += 1

print(contador_meses)