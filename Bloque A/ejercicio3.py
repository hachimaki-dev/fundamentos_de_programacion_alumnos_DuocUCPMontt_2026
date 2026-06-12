def calcularMulta(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia

multa_persona1 = calcularMulta(10)
multa_persona2 = calcularMulta(2)
multa_persona3 = calcularMulta(5)

print(f"El total de la persona 1 es de {multa_persona1}")
print(f"El total de la persona 2 es de {multa_persona2}")
print(f"El total de la persona 3 es de {multa_persona3}")