cantidad_de_platos= int(input("Ingrese la cantidad de platos que desea pedir: "))
subtotal=0
platos_pedidos=1
descuento=0
envío= 2000

while platos_pedidos<=cantidad_de_platos:
    precio_plato= int(input("Ingrese el precio del plato: "))
    subtotal+=precio_plato
    platos_pedidos+=1
if subtotal>15000:
    descuento= subtotal //10
    total_a_pagar= subtotal-descuento
    print(f"Subtotal:${subtotal} \nDescuento:${descuento} \nTotal a pagar: ${total_a_pagar}")
else:
    total_a_pagar= subtotal+envío
    print(f"Subtotal: ${subtotal} \nEnvío: ${envío} \nTotal a pagar: ${total_a_pagar}")