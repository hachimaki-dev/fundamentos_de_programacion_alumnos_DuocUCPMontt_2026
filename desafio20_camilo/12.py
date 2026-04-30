ventas = {
    "Taza" : 500,
    "Plato" : 1200,
    "Vaso" : 300
}

total_ventas = 0

for valor in ventas.values() :
    total_ventas += valor

print(total_ventas)