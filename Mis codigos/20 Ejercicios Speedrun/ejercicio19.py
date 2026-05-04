# Ejercicio 19: Carrito con descuento
# Define compras = ['espada', 'pocion', 'espada'] y precios = {'espada': 100, 'pocion': 50}. 
# Calcula el subtotal de la compra. Si el subtotal es mayor que 200, aplica un descuento del 10% y guarda el valor final en una variable llamada total_final. 
# Imprime el resultado.

compras = ['espada', 'pocion', 'espada']
precios = {'espada': 100, 'pocion': 50}
subtotal = 0
total_final = 0

for producto in compras:
    if producto == "espada":
        subtotal = precios["espada"]
    elif producto == "pocion":
        subtotal = precios["pocion"]
    total_final += subtotal

print(total_final)
