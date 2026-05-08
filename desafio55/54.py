carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
descuento = 0.10
total = 0
for i in carrito:
    total += i['qty'] * i['precio']
if total > 50000:
    precio_descuento = total * descuento
    total = total - precio_descuento
print(total)