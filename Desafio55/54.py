carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
total = 0

for item in carrito:
    total += item.get("qty") * item.get("precio")

if total > 50000:
    total -= total * .1

print(total)