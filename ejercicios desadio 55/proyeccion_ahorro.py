valor_auto = 5000000
ahorrado = 1500000
ahorro_del_mes = 150000
dinero_faltante = valor_auto - ahorrado
print(f"te falta {dinero_faltante} por ahorrar")
meses_para_comprar = dinero_faltante // ahorro_del_mes
print(f"podras comprar el auto en {meses_para_comprar} meses")