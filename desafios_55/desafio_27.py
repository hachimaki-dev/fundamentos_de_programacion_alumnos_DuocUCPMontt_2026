ventas_dia = [1500, -200, 5000, 0, 100]
total = 0

for venta in ventas_dia:
    if venta in [-200, 0]:
        continue
    else:
        total += venta
print(f"el total de ventas fueron de: {total}")