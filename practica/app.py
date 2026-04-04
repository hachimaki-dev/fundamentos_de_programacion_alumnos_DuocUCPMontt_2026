# Pregunta al usuario cuántos platos desea pedir (cantidad).
#2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
#3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
#4. Una vez terminado el ciclo, evalúa el subtotal con un if:
#- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
#- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".

cantidad = 0
subtotal = 0
contador = int(input("cuantos platos desea pedir?"))
envio = 2000


while contador > 0:
    precio = int(input(f"ingrese el precio del plato a pedir :"))
    subtotal += precio
    contador -= 1
    print(subtotal)
if subtotal > 15000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print(f"subtotal: {subtotal}")
    print(f"descuento: {descuento}")
    print(f"total: {total}")
elif subtotal < 15000:
    total = subtotal + envio
    print(f"envio: {envio}")
    print(f"subtotal: {subtotal}")
    print(f"total: {total}")

 