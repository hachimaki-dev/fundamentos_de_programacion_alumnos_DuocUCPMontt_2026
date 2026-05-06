venta_dia = [1500, -200, 5000, 0, 100]
total = 0 
for ventas in venta_dia:
    if ventas >= 0:
        total += ventas
print(total)