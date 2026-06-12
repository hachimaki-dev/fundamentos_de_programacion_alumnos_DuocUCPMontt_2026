def calcular_multa(dias_atraso, valor_por_dia = 100):
    total = dias_atraso * valor_por_dia
    return total

multa1 = calcular_multa(5)
print(f"${multa1}") #Resultado con 1 argumento

multa2 = calcular_multa(5, 500)
print(f"${multa2}") #Resultado con 2 argumentos, el segundo número remplaza al 100 (que es el valor por dia)

