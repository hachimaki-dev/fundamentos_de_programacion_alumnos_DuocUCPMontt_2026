"""bjetivo: Calcular el total a pagar de un pedido de comida, con descuentos.

1. Pregunta al usuario cuántos platos desea pedir (cantidad).
2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
4. Una vez terminado el ciclo, evalúa el subtotal con un if:
- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".     >) y menor que (< {}   """  

platos_pedidos = int(input("cuantos platos desea pedir?: "))
envio = 2000
contador = 0
while True:
    contador = int(input("cual es el precio de cada plato?: "))
    contador = platos_pedidos * contador
    subtotal = contador
    if subtotal > 15000:
        descuento = (subtotal * 10) // 100
        int(print(f"subtotal:{contador}  , descuento: {descuento }  y total pagar seria: {subtotal - ((subtotal * 10) // 100)}"  ))
    
    elif subtotal  < 15000:
        envio = 2000
        subtotal_mas_envio = subtotal + envio
        int(print(f"subtotal:{subtotal}, envio: 2000 , total pagar: {subtotal_mas_envio} "))
