dinero_en_alcancia = 0
ahorro_mensual = 80000
precio_consola = 450000
contador = 0

while dinero_en_alcancia < precio_consola:
    dinero_en_alcancia = dinero_en_alcancia + ahorro_mensual
    contador = contador + 1

print(contador)
