'''Ejercicio 54: Carrito Inteligente Múltiple (Amazon)
Calcula el cobro final de un carrito de compras que tiene cantidades y precios separados.

Datos Iniciales: Tu carrito es una lista de diccionarios: `[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]`.

Reglas de Negocio: Tienes que multiplicar la cantidad (`qty`) por el `precio` de cada cosa para saber cuánto vale cada paquete. 

Suma todo. Si el monto final es mayor a 50000, le haces un descuento del 10% automático.

Restricciones: Usa un `for` para recorrer el carrito y hacer la matemática. 

Recuerda usar corchetes (ej. `producto['qty']`) para sacar los datos. Aplica el descuento si corresponde e imprime solo el precio que debe pagar.'''

Carrito = [

    {'item': 'Mouse', 'qty': 2, 'precio': 15000}, 
    
    {'item': 'Teclado', 'qty': 1, 'precio': 30000}
    
            ]

Total_Total = 0

Total = 0

for Dicc in Carrito:

    Total = Dicc['qty'] * Dicc['precio']

    Total_Total += Total

    print(f'Item: {Dicc['item']}, {Total}$')

if Total_Total > 50000:
    Total_Total *= 0.9

print(f'Tu total sera de : {Total_Total}')