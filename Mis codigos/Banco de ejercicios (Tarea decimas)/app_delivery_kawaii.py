# App de Delivery Kawaii
# Objetivo: Calcular el total a pagar de un pedido de comida, con descuentos.

# 1. Pregunta al usuario cuántos platos desea pedir (cantidad).
# 2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
# 3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
# 4. Una vez terminado el ciclo, evalúa el subtotal con un if:
# - Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
# - Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".

print(" BIENVENIDO A DELIVERY KAWAII ".center(40, "-"))

total = 0
subtotal = 0
descuento = 0
costo_envio = 2000
numeracion_plato = 1

cantidad_platos = int(input("¿Cuantos platos desea? "))

if cantidad_platos == 0:
    print(f"Total a pagar: ${total}")
else:
    while cantidad_platos != 0:
        cada_plato = int(input(f"Ingrese el precio del plato {numeracion_plato}: "))
        subtotal = subtotal + cada_plato
        cantidad_platos = cantidad_platos - 1
        numeracion_plato = numeracion_plato + 1

    if subtotal > 15000:
        descuento = (0.10)*subtotal
        total = subtotal - descuento
        print(f"Subtotal: ${subtotal}, Descuento: ${descuento}, Total pagar: ${total}")

    if subtotal <= 15000:
        total = subtotal + costo_envio 
        print(f"Subtotal: ${subtotal}, Envio: ${costo_envio}, Total pagar: ${total}")


