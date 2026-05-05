ventas = [1500, -200, 5000, 0, 100]
total = 0

for venta in ventas:
    if venta <= 0:
        continue
    else:
        total += venta

print(total)