alcancia = 0
ahorro_mensual = 80000 
precio_consola = 450000
contador_de_meses = 0

while alcancia <= precio_consola:
    alcancia = alcancia + ahorro_mensual
    contador_de_meses += 1
    if alcancia >= precio_consola:
        print(contador_de_meses)
 