"""
Objetivo: Sistema de cobro que evalúe promociones por mayor.

1. Pide registrar un único producto estrella.
2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó ("¡Felicidades obtuvo el X% descuento! Su total es...").
5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".
"""

producto = input("Registra un producto estrella ")
precio = int(input("Cual es el precio de este producto? "))
unidades = int(input("Cuantas unidades esta comprando el cliente? "))

print("Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento")
if unidades >= 5 and unidades <= 10:
    Total = precio * unidades * 0.9
    print(f"¡Felicidades obtuvo el 10% descuento! Su total es {Total}")
elif unidades > 10:
    Total = precio * unidades * 0.8
    print(f"¡Felicidades obtuvo el 20% descuento! Su total es {Total}")
else:
    Total = precio * unidades
    print(f"Su total es {Total}")