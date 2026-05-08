carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
total = 0

for i in carrito:
    paquetes = i["qty"] * i["precio"]
    total += paquetes
if total >= 50000:
    descuento = 0.10
    total = total - (total * descuento)

print(total)