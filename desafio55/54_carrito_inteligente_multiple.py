# Ejercicio 54: Carrito Inteligente Múltiple (Amazon)
# Calcula el cobro final de un carrito de compras que tiene cantidades y precios separados.

# Datos Iniciales: Tu carrito es una lista de diccionarios:
#  `[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]`.

# Reglas de Negocio: Tienes que multiplicar la cantidad (`qty`) por el `precio` de cada cosa para saber cuánto vale cada paquete. 
# Suma todo. Si el monto final es mayor a 50000, le haces un descuento del 10% automático.

# Restricciones: Usa un `for` para recorrer el carrito y hacer la matemática. Recuerda usar corchetes (ej. `producto['qty']`) para sacar los datos. 
# Aplica el descuento si corresponde e imprime solo el precio que debe pagar.

carrito = [{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]
monto_total = 0
descuento = 10/100

for producto in carrito:
    monto_total += (producto['qty'] * producto['precio'])

if monto_total > 50000:
    monto_total -= monto_total * descuento

print(monto_total)