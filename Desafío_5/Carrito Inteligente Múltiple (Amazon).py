carrito = [
    {'item': 'Mouse', 'qty': 2, 'precio': 15000},
    {'item': 'Teclado', 'qty': 1, 'precio': 30000}
]

total = 0

for producto in carrito:

    subtotal = producto['qty'] * producto['precio']

    total += subtotal

if total > 50000:

    descuento = total * 0.10

    total -= descuento

print(total)