valor_auto = 5000000
ahorro_inicio = 1500000
ahorro_mensual = 150000
meses_de_ahorro = 0
dinero_faltante = valor_auto - ahorro_inicio

meses_de_ahorro = dinero_faltante // ahorro_mensual
print(f"faltan {dinero_faltante}")
print(f"Faltan {meses_de_ahorro} meses para obtener el total del pago")