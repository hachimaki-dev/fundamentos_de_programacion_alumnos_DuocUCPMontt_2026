ventas = {"LocalA": 150, "LocalB": 300, "LocalC": 100}

total = 0

for venta in ventas.values():
    total = total + venta

print(total)