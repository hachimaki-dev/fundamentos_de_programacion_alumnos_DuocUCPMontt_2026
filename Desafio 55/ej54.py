#Ejercicio 54: Carrito Inteligente Múltiple (Amazon)
#Calcula el cobro final de un carrito de compras que tiene cantidades y precios separados.

#Datos Iniciales: Tu carrito es una lista de diccionarios: `[{'item': 'Mouse', 'qty': 2, 'precio': 15000}, {'item': 'Teclado', 'qty': 1, 'precio': 30000}]`.

#Reglas de Negocio: Tienes que multiplicar la cantidad (`qty`) por el `precio` de cada cosa para saber cuánto vale cada paquete. Suma todo. Si el monto final es mayor a 50000, le haces un descuento del 10% automático.

#Restricciones: Usa un `for` para recorrer el carrito y hacer la matemática. Recuerda usar corchetes (ej. `producto['qty']`) para sacar los datos. Aplica el descuento si corresponde e imprime solo el precio que debe pagar.

carrito = [{
        'item':'Mouse',
        'qty':2,
        'precio':15000
    },
    {
        'item':'Teclado',
        'qty':1,
        'precio':30000
    }]
total = 0

for periferico in carrito:
    total_item = periferico['precio'] * periferico['qty']
    total += total_item
    
    if total > 50000:
        total -= (total * 0.1)

print(int(total))