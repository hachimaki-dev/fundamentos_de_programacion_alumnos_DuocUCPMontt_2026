# Ejercicio 54: Carrito Inteligente Múltiple (Amazon)
# Calcula el cobro final de un carrito de compras que tiene cantidades y precios separados.

# Datos Iniciales: Tu carrito es una lista de diccionarios: `[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]`.

# Reglas de Negocio: Tienes que multiplicar la cantidad (`qty`) por el `precio` de cada cosa para saber cuánto vale cada paquete. Suma todo. Si el monto final es mayor a 50000, le haces un descuento del 10% automático.

# Restricciones: Usa un `for` para recorrer el carrito y hacer la matemática. Recuerda usar corchetes (ej. `producto['qty']`) para sacar los datos. Aplica el descuento si corresponde e imprime solo el precio que debe pagar.

mi_carrito = [{"item": "mouse", "qty": 2, "precio": 15000}, {"item": "teclado", "qty": 1, "precio": 30000}]
acumulador = 0

for producto in mi_carrito:
    acumulador += producto["qty"] * producto["precio"]

if acumulador > 50000:
    total = acumulador * 0.90

else:
    total = acumulador

print(total)