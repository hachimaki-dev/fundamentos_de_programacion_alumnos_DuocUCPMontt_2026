carrito = [
    {'item': 'Mouse', 'qty': 2, 'precio': 15000}, 
    {'item': 'Teclado', 'qty': 1, 'precio': 30000}
]
total_compra = 0
for producto in carrito:
    subtotal = producto['qty'] * producto['precio']
    total_compra += subtotal
    if total_compra > 50000:
        total_compra = total_compra * 0.90
print(total_compra)