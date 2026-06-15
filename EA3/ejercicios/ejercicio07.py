#Crea calcular_propina(total, porcentaje=10) que retorne el monto de la propina. El porcentaje por defecto es 10%.

def calculador_propina(total, porcentaje=10):
    
    propina= total*(porcentaje/100)
    return propina

resultado= calculador_propina(15000)

print(resultado)