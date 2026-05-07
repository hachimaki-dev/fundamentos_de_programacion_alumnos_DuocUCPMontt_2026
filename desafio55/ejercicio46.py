ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}

total_ventas = 0

for i in ventas.values():
    total_ventas += i
    print(f"Sumando {i}, llevas {total_ventas}")

print(f"En total se vendio {total_ventas}")