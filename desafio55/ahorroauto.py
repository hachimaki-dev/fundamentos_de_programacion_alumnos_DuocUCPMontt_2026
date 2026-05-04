costo_auto = 5000000
ahorro_actual = 1500000
ahorro_mensual = 150000
total = costo_auto - ahorro_actual
print(f"el auto que quieres vale {costo_auto} y hasta el momento tienes {ahorro_actual} eso te lo deja en {total} ")
dinero_faltante = costo_auto - ahorro_actual
meses_necesarios = dinero_faltante // ahorro_mensual

print(meses_necesarios)