print("BIENVENIDO A LA APP DE DELIVERY KAWAIII")
print("Realiza tu pedido :)")
Cantidad_de_platos = 0 
Subtotal = 0 
contador = 0
precio_de_cada_plato = 0

Cantidad_de_platos = int(input("Cuantos platos deseas pedir?: "))
while contador < Cantidad_de_platos:
    precio_de_cada_plato = int(input("Ingresa el precio del plato: "))
    Subtotal = Subtotal + precio_de_cada_plato
    contador = contador + 1
if Subtotal > 15000:
    descuento = Subtotal * 0.10
    total = Subtotal - descuento
    print(f"Subtotal:{Subtotal}")
    print(f"Descuento:{descuento}")
    print(f"Total a pagar:{total}")
else:
    costo_envio = 2000
    total = Subtotal + costo_envio
    print(f"Subtotal:{Subtotal}")
    print(f"Envio:{costo_envio}")
    print(f"Total a pagar:{total}")  
#1. Pregunta al usuario cuántos platos desea pedir (cantidad).
#2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
#3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
#4. Una vez terminado el ciclo, evalúa el subtotal con un if:
#- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
#- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".