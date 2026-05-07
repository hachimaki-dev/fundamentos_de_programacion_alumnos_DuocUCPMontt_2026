ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}
total_venta = 0

for monto in ventas.values():
    total_venta += monto

print(total_venta)