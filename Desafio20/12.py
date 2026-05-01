ventas={
    "taza":500,
    "plato":1200,
    "vaso":300
}
total_ventas=0

for valor in ventas:
    total_ventas=total_ventas+ventas[valor]

print(total_ventas)