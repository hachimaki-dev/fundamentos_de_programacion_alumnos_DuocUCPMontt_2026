contador = 1
subtotal = 0
envio = 2000

platos_desea_pedir = int(input(" ¿Cuantos platos Desea Pedir? :   "))

while contador <= platos_desea_pedir:
    Precio_por_plato = float(input(f"Precio del plato N°{contador}:  "))
    subtotal += Precio_por_plato
    contador += 1 


if subtotal > 15000:
    descuento = subtotal * 0.10
    total_a_pagar = subtotal - descuento
    print(f"Subtotal: {subtotal}\nDescuento: {descuento}\nTotal a Pagar: {total_a_pagar} ")
elif subtotal < 15000:
    total_a_pagar = subtotal + envio
    print(f"Subtotal: {subtotal}\nEnvio: {envio}\nTotal a pagar:{total_a_pagar}")
    

