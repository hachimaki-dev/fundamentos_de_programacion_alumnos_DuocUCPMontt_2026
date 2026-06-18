auto = 5000000
ahorro = 1500000
ahorro_mensual = 150000

dinero_faltante = auto - ahorro
meses = dinero_faltante // ahorro_mensual

print(f"Cantidad de meses a juntar: {meses}")