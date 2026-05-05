valor_auto = 5000000
ahorro_actual = 1500000
ahorro_mes = 150000
#valor faltante
valor_faltante = (valor_auto - ahorro_actual)
#meses para ahorrar
meses = (valor_faltante // ahorro_mes)
print(f"Los meses que me faltan son {meses}")