ventas_dia = [1500, -2000, 5000, 0, 100]
total = 0
for venta in ventas_dia:
    if venta > 0:
        total += venta
print(total)