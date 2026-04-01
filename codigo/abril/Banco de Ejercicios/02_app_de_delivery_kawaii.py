contador = 1
subtotal = 0
porcentaje_descuento = 10
costo_fijo_envio = 2000

cantidad_de_platos = int(input("¿Cuántos platos desea pedir?: "))

while contador <= cantidad_de_platos:
    subtotal += int(input(f"Ingresa el precio del plato {contador}: "))
    print(f"Subtotal actual: ${subtotal}")
    contador += 1

if subtotal > 15000:
    descuento = int(subtotal / 100 * porcentaje_descuento) # Calculo de porcentaje
    subtotal_con_descuento = subtotal - descuento
    print(f"\nSubtotal: ${subtotal}, Descuento: ${descuento}, Total a pagar: ${subtotal_con_descuento}")
else:
    subtotal_mas_envio = subtotal + costo_fijo_envio
    print(f"\nSubtotal: ${subtotal}, Envío: ${costo_fijo_envio}, Total a pagar: ${subtotal_mas_envio}")
