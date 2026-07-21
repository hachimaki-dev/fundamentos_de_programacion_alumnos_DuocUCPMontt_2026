# Supermercado Mayorista
# Objetivo: Sistema de cobro que evalúe promociones por mayor.

# 1. Pide registrar un único producto estrella.
# 2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
# 3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
# 4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó ("¡Felicidades obtuvo el X% descuento! Su total es...").
# 5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".

print("***Supermercado Mayorista****")

precio_unitario = int(input("¿Cual es el precio unitario del producto?: "))
unidades = int(input("¿Cuantas unidades estás comprando?: "))

if unidades >= 5 and unidades <= 10:
    total = precio_unitario - (precio_unitario * 0.1)
    print(f"¡Felicidades obtuvo el 10% descuento! Su total es ${total}")

elif unidades > 10:
    total = precio_unitario - (precio_unitario * 0.2)
    print(f"¡Felicidades obtuvo el 20% descuento! Su total es ${total}")
else:
    print(f"Su total es ${precio_unitario}")


