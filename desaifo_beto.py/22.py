alcancia = 0
ahorro_mensual = 80000
valor_consola = 450000

contador_de_meses = 1
while alcancia < valor_consola :
    alcancia += ahorro_mensual
    print(f"valor de la consola es {valor_consola} y llevo ahorrdo {alcancia} y voy en el mes {contador_de_meses}")
    contador_de_meses += 1
    
print("logrado")