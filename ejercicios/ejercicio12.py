ventas = {"taza": 500, "plato": 1200, "vaso": 300}
total_ventas = 0
for producto in ventas:
    total_ventas += ventas[producto]
print(total_ventas)