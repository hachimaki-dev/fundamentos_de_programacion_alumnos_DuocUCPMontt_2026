#Objetivo: Calcular el total a pagar de un pedido de comida, con descuentos.

#1. Pregunta al usuario cuántos platos desea pedir (cantidad).
#2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
#3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
#4. Una vez terminado el ciclo, evalúa el subtotal con un if:
#- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
#- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".

print("Bienvenido a KAWAII Eats")

print("\nMenu del dia $5000")

print("\nIngrese cuantos platos desea pedir: ")

cantidadplatos= int(input())
contador = 0
subtotal = 0
total = 0

while contador < cantidadplatos :
   subtotal = subtotal + 5000
   contador += 1

descuento = 0
if subtotal > 15000:
    descuento = subtotal*0.1   
    total = subtotal - descuento
    print(f"\nSubtotal: ${int(subtotal)}\nDescuento: ${int(descuento)}\nTotal a pagar ${int(total)}")
else:
    total = subtotal + 2000
    print(f"\nSubtotal: ${int(subtotal)}\nEnvío: $2000\nTotal a pagar ${int(total)}")
