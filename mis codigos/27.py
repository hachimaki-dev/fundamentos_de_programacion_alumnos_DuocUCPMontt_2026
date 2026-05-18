Ventas_del_dia = [1500, -200, 5000, 0, 100]

total = 0

for venta in Ventas_del_dia:

    if venta > 0:
        total += venta

print(f"Total de ventas positivas: {total}")