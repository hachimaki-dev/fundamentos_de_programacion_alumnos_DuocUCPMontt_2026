ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}
total_ventas = 0
for venta in ventas.values():
    total_ventas += venta
print(total_ventas)