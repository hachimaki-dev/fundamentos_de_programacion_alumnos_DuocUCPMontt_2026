ventas = {
    'LocalA' : 150,
    'LocalB' : 300,
    'LocalC' : 100
}

total= 0

for valores in ventas.values():
    total = total + valores

print(total)