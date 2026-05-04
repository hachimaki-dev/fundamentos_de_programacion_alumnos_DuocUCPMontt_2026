valor_auto = 5000000
ahorro = 1500000

dinero_faltante = valor_auto - ahorro
print(f"Te faltan {dinero_faltante}CLP")

ahorro_mensual = 150000

contador_pago_mensual = 0
while ahorro < valor_auto:
    if ahorro >= valor_auto:
        break
    ahorro = ahorro + ahorro_mensual
    contador_pago_mensual = contador_pago_mensual + 1
print("")
print(f"Necesita ahorrar {ahorro_mensual}CLP eso equivale a {contador_pago_mensual} meses ")
print("")