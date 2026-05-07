ventas = {'LocalA': 150,
          'LocalB': 300,
          'LocalC': 100}

venta_total = 0

for venta in ventas.values() :
    venta_total += venta

print(venta_total)