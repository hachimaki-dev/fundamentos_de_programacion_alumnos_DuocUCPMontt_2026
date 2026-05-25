cuenta = {
    'Papas' : 5000,
    'Pizza' : 10000
}
total = 0

for nombre, precio in cuenta.items():
    total += precio
total = total * 1.10
print(f"Total final: {total}")