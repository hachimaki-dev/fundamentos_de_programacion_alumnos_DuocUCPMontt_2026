cantidad_platos = int(input("¿Cuantos platos quiere pedir?: "))
subtotal = 0
total = 0
descuento = 0
envio = 2000
contador = 0

while contador < cantidad_platos:
    subtotal += int(input(f"Ingrese el precio del plato {contador + 1}: "))
    contador += 1

if subtotal > 15000:
    descuento = subtotal*0.1
    total = subtotal - descuento
    print(f"Subtotal: ${subtotal}\nDescuento: ${descuento}\nTotal a pagar: ${total}")
else:
    total = subtotal + envio
    print(f"Subtotal: ${subtotal}\nEnvío: ${envio}\nTotal a pagar: ${total}")