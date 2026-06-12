def calcular_multa(dias_atraso, valor_por_dia=100):
   return dias_atraso * valor_por_dia

resultado_uno = calcular_multa(5)
print(resultado_uno) # imprime: 500

resultado_dos = calcular_multa(5, 150)
print(resultado_dos) # imprime: 750