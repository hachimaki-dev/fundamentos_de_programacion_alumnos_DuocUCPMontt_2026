ventas_diarias = [1500, -200, 5000, 0, 100]
total = 0
for venta in ventas_diarias:
    if venta <= 0:
        continue
    total += venta
print(total)