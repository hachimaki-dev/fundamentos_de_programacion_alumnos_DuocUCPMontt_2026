def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia
a = calcular_multa(10)
b = calcular_multa(5,500)
print(a)
print(b)