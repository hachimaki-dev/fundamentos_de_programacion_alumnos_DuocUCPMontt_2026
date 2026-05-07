carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]

total_acumulado = 0

for producto in carrito:
    subtotal_item = producto['qty'] * producto['precio']
    total_acumulado += subtotal_item

if total_acumulado > 50000:
    total_acumulado = total_acumulado * 0.9

print(total_acumulado)