print("Bienvenido al local de hamburguesas")
cantidad_de_platos = int(input(f"ingrese la cantidad de platos: " ))

contador = 0
sub_total = 0

while contador < cantidad_de_platos:
    contador += 1

    precio = int(input(f"ingrese el precio del plato: " ))
    sub_total += precio

print ("Pedido")

if sub_total > 15000:
    descuento = sub_total * 0.10
    total = sub_total - descuento
    print(f"Total a pagar:{total} ")
else:
    envio = 2000
    total = sub_total + envio
    print(f"total a pagar mas envio de 2000: {total}.")


