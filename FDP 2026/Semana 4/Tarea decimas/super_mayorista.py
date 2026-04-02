precio_unitario = int(input("Precio unitario del producto: $"))

unidades = int(input("Unidades del producto: "))

descuento = 0
total = precio_unitario * unidades

if unidades >= 5 and unidades <= 10:
    descuento = 0.1
    print(f"¡Felicidades!, obtuviste un {100*descuento}% de descuento")
elif unidades > 10:
    descuento = 0.2
    print(f"¡Felicidades!, obtuviste un {100*descuento}% de descuento")

print(f"Su total a pagar es: ${total - (total * descuento)}")