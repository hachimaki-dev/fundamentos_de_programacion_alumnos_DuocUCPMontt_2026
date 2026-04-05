print("^.^.^.^.^.^.^.^.^.^.^ APP KAWAII ^.^.^.^.^.^.^.^.^.^.^")

cantidad = int(input("¿Cuantos platos desea pedir? "))

subtotal = 0
contador = 0

while contador < cantidad:
    precio = float(input(f"Ingrese el precio del plato {contador + 1}: "))
    subtotal += precio
    contador += 1

if subtotal > 15000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print(f"Subtotal: ${subtotal}, Descuento ${descuento}, Total a pagar: ${total}")

else:
    envio = 2000
    total = subtotal + envio
    print(f"Subtotal: ${subtotal}, Envío: ${envio}, Total a pagar: ${total}")