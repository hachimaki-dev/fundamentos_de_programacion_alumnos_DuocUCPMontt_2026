ventas = {"taza": 500, "plato": 1200, "vaso": 300}
total_ventas = 0
for venta in ventas:
    total_ventas += ventas[venta]
print(total_ventas)