def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia


respuesta = calcular_multa(4)
print(respuesta)