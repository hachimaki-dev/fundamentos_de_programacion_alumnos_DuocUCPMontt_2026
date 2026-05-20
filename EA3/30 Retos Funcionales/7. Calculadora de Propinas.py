#Crea calcular_propina(total, porcentaje=10) que retorne el monto de la propina. El porcentaje por defecto es 10%.

def calcular_propina(total, porcentaje=10):
    propina = total * (porcentaje / 100)
    return propina

print(calcular_propina(2000, 20))