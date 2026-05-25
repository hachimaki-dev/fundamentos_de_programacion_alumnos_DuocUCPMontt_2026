ventas_bugeadas = [1500, -200, 5000, 0, 100]
total_ventas_registradas = 0
for venta in ventas_bugeadas:
    if venta <= 0:
        continue
    else:
        total_ventas_registradas += venta
print(total_ventas_registradas)