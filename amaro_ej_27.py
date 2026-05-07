ventas_dia = [1500, -200, 5000, 0, 100]
total = 0

for cantidad in ventas_dia:
    if cantidad <= 0:
        continue
    total += cantidad
    print(cantidad)
print(f"Total limpia: ${total}")