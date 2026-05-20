ventas_del_dia = [1500, -200, 5000, 0, 100]
total = 0
for venta in ventas_del_dia:
    if venta <= 0:
        continue
    total += venta
print(total)