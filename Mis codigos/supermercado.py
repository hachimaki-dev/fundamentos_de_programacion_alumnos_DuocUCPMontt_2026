
producto = input("Ingrese el nombre del producto estrella: ")

precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

subtotal = precio_unitario * cantidad

if cantidad >= 5:
    if cantidad <= 10:
        descuento = 0.10
    else:
        descuento = 0.20
else:
    descuento = 0

monto_descuento = subtotal * descuento
total = subtotal - monto_descuento

print("\n======= BOLETA =======")
print(f"Producto: {producto}")
print(f"Subtotal: ${subtotal:.0f}")

if descuento > 0:
    print(f"¡Felicidades! Obtuvo un {int(descuento*100)}% de descuento")
    print(f"Descuento: ${monto_descuento:.0f}")
else:
    print("No se aplicó descuento.")

print(f"Total a pagar: ${total:.0f}")