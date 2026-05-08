carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
total = 0
 
for producto in carrito:
    total += producto['qty'] * producto['precio']
 
if total > 50000:
    descuento = total * 0.10
    total = total - descuento
 
print(total)