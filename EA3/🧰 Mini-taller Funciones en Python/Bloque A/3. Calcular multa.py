#def calcular_multa(dias_atraso=100, valor_por_dia):
#Genera un error en python debido a que los parametros fijos deben ir despues de los parametros por opcionales
def calculcar_multa(dias_atraso, valor_por_dia = 100):
    total_multa = dias_atraso * valor_por_dia
    return total_multa


print(calculcar_multa(19))

print(calculcar_multa(19, 20))

#aqui se expecifica el valor a modificar
print(calculcar_multa(valor_por_dia=20, dias_atraso=10))

