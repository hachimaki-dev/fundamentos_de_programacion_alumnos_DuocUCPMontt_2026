
cantidad = int(input("¿Cuántos platos desea pedir?: "))

contador = 1
subtotal = 0

while contador <= cantidad:
    precio = int(input(f"Ingrese el precio del plato {contador}: "))
    
    subtotal += precio
    
    contador += 1

print("\n======= RESUMEN =======")

if subtotal > 15000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento (10%): ${descuento:.0f}")
    print(f"Total a pagar: ${total:.0f}")
else:
    print(f"Subtotal: ${subtotal}")
    print("No aplica descuento.")
    print(f"Total a pagar: ${subtotal}")