cantidad_de_platos_de_user = int(input("¿Cuantos platos desea pedir? "))
contador_de_platos_de_user = 1
total = 0
while cantidad_de_platos_de_user >= contador_de_platos_de_user:
    precio_plato = int(input(f"¿Cual es el precio del plato numero {contador_de_platos_de_user}? "))
    if precio_plato >= 1:
        total = total + precio_plato
        contador_de_platos_de_user = contador_de_platos_de_user + 1
    else:
        print("Ese no es un valor valido")
if total > 15000:
    vbruto = total
    total = total * 0.90
    print(f"Subtotal: {vbruto} \nDescuento: {vbruto - total} \nTotal pagar: {total}")
elif total < 15000:
    vbruto = total
    envio = 2000
    print(f"Subtotal: {vbruto} \nEnvío: {envio} \nTotal pagar: {vbruto + envio}")