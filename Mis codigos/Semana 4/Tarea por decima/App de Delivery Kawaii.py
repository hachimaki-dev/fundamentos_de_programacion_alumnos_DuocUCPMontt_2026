# App de Delivery Kawaii
# Objetivo: Calcular el total a pagar de un pedido de comida, con descuentos.

# 1. Pregunta al usuario cuántos platos desea pedir (cantidad).
# 2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
# 3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
# 4. Una vez terminado el ciclo, evalúa el subtotal con un if:
# - Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
# - Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".

cantidad_platos = 0
contador = 0
acumulador = 0
subtotal = 0


print("****Bienvenidos a la App de Delivery Kawaii .-.*****")
cantidad_platos = int(input("¿Cuántos platos deseas pedir?: "))

while cantidad_platos > contador:
    acumulador = int(input("Precio del Plato: "))
    subtotal += acumulador 
    contador += 1
    if cantidad_platos == contador:
        break

if subtotal > 15000:
    descuento = subtotal * 0.1
    print(f"Subtotal: ${subtotal}, Descuento: ${descuento}, Total ${subtotal - descuento}")
    print("Su pedido llegará en 20 años, 3 meses y 8 días.")
elif subtotal <= 15000 and subtotal > 0:
    envio = 2000
    print(f"Subtotal: ${subtotal}, Envío: ${envio}, Total a pagar: ${subtotal + envio}")
    print("Su pedido llegará en 20 años, 3 meses y 8 días.")
else:
    subtotal <= 0
    print("Error 404 :(")

print("Fin del programa")