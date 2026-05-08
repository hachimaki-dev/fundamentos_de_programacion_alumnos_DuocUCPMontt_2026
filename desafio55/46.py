ventas = {
    "LocalA": 150,
    "LocalB": 300,
    "LocalC": 100
}
total = 0
for monto in ventas.values():
    total += monto
print(total)