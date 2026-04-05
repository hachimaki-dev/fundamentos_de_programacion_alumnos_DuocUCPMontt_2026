# Supermercado Mayorista
# Objetivo: Sistema de cobro que evalúe promociones por mayor.

# 1. Pide registrar un único producto estrella.
# 2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
# 3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
# 4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó ("¡Felicidades obtuvo el X% descuento! Su total es...").
# 5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".

print(" BIENVENIDO AL SUPER ".center(40, "-"))

producto_estrella = input("NOMBRE DEL PRODUCTO ESTRELLA: ")
precio_producto_estrella = int(input("PRECIO DEL PRODUCTO ESTRELLA: "))
unidades_de_compra = int(input("UNIDADES DE COMPRA DEL PRODUCTO ESTRELLA: "))
subtotal = 0
total_a_pagar = 0
descuento = 0

if unidades_de_compra >= 5 and unidades_de_compra <= 10:
    subtotal = precio_producto_estrella * unidades_de_compra
    descuento = subtotal * 0.10
    total_a_pagar = subtotal - descuento
    print("-"*20)
    print(f"Detalle de la venta: \nProducto: {producto_estrella}\nPrecio Unitario: {precio_producto_estrella}\nUnidades: {unidades_de_compra}")
    print(f"¡Felicidades obtuvo el 10% descuento! Su total a pagar es: ${total_a_pagar}")
elif unidades_de_compra > 10:
    subtotal = precio_producto_estrella * unidades_de_compra
    descuento = subtotal * 0.20
    total_a_pagar = subtotal - descuento
    print("-"*20)
    print(f"Detalle de la venta: \nProducto: {producto_estrella}\nPrecio Unitario: {precio_producto_estrella}\nUnidades: {unidades_de_compra}")
    print(f"¡Felicidades obtuvo el 20% descuento! Su total a pagar es: ${total_a_pagar}")
elif unidades_de_compra < 5:
    subtotal = precio_producto_estrella * unidades_de_compra
    total_a_pagar = subtotal
    print("-"*20)
    print(f"Detalle de la venta: \nProducto: {producto_estrella}\nPrecio Unitario: {precio_producto_estrella}\nUnidades: {unidades_de_compra}")
    print(f"Total a pagar: ${total_a_pagar}")