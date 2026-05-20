#Crea calcular_propina(total, porcentaje=10) que retorne el monto de la propina. El porcentaje por defecto es 10%.
cuenta_cliente = int(input("Ingrese el total de la cuenta: $"))

def calcular_propina(total, propina = 10):
    monto_propina = cuenta_cliente * (propina / 100)
    return monto_propina

resultado = calcular_propina(cuenta_cliente)
print(f"Monto de la propina: ${int(resultado)}")
