def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia
print(calcular_multa(5))
print(calcular_multa(5, 70))