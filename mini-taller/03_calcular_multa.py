def calcular_multa(dias_atraso, valor_por_dia=100):
    return valor_por_dia * dias_atraso 
resultado = calcular_multa(12)
print(resultado)