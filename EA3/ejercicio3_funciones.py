def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso *valor_por_dia

resultado = calcular_multa(10)
print(resultado)