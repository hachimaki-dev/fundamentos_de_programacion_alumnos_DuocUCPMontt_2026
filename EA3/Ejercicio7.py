def calcular_propina(total, porcentaje=10):
    propina = total*(porcentaje/100)
    return propina

resultado = calcular_propina(25000)
print(resultado)