carrito = [{"item": "Mouse", "qty": 2, "precio": 15000}, {"item": "Teclado", "qty": 1, "precio": 30000}]
monto_final= 0
for producto in carrito:
    valor_por_paquete = producto["qty"] * producto["precio"]
    monto_final += valor_por_paquete

if monto_final > 50000:
    descuento = monto_final * 0.10
    monto_final -= descuento
    
print(monto_final)