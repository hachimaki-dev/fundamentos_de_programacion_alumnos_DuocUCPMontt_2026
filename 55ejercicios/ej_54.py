# Ejercicio 54: Carrito Inteligente Múltiple (Amazon)

print("============================")
print("Calculando total del carrito")
print("============================")

carrito = [
    {'item': 'Mouse', 'qty': 2, 'precio': 15000},
    {'item': 'Teclado', 'qty': 1, 'precio': 30000}
]

total = 0

for producto in carrito:
    total = total + (producto['qty'] * producto['precio'])

if total > 50000:
    total = total * 0.9

print(total)