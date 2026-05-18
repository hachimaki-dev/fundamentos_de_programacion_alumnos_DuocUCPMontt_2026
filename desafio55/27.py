ventas_del_dia = [1500, -200, 5000, 0, 100]
variable_total = 0
for venta in ventas_del_dia:
    if venta <= 0:
        continue
    variable_total += venta
print(variable_total)
    