total = 0
ventas_del_dia = [ 1500, -200, 5000, 0, 100 ]

for venta in ventas_del_dia:
    if venta < 0:
        continue
    else:
        total = total + venta

print(total)
