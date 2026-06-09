carrito = [{"item":"Mouse", "qty":2, "precio":15000}, {"item":"Teclado", "qty":1, "precio":30000}]
total = 0
for producto in carrito:
    total += producto["qty"]*producto["precio"]

descuento = 0.10 * total
if total > 50000:
    total -= descuento
    print(total)