def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia


multa = calcular_multa(5, 200)   
print(f"tu multa es de {multa}")