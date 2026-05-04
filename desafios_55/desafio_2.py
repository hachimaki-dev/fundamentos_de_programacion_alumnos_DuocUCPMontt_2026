precio_auto = 5000000
dinero_ahorrado = 1500000
ahorro_mensual = 150000

dinero_faltante = precio_auto - dinero_ahorrado
meses_totales = dinero_faltante // ahorro_mensual

print(f"El dindero que falta para comprar el auto son ${dinero_faltante} y el total de meses para juntar el dinero y comprar el auto son de {meses_totales} meses")