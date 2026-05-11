carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
monto_final = 0
descuento = 0
monto_final_real = 0
for producto in carrito:
    subtotal = producto["qty"] * producto["precio"]
    monto_final += subtotal
    if monto_final > 50000:
        descuento = monto_final * 0.10
        monto_final_real = monto_final - descuento

print(f"El total de la compra de {producto["item"]} y {producto["item"]} es de {monto_final_real}")