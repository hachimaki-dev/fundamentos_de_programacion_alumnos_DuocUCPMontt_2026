""" Objetivo: Sistema de cobro que evalúe promociones por mayor.

1. Pide registrar un único producto estrella.
2. Pregunta el precio unitario del producto 
y cuántas unidades está comprando el cliente.

3. La promoción dice: "Si lleva entre 5 y 10 productos iguales,
 tiene 10% de descuento. Si lleva MÁS de 10 productos iguales,
 tiene 20% descuento". (Si lleva menos de 5, no hay descuento).

4. El programa debe determinar el precio total a pagar, 
indicando de cuánto fue el porcentaje de descuento que se aplicó 
("¡Felicidades obtuvo el X% descuento! Su total es...").

5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático"."""

producto = input("ingresa un producto: ")
precio = int(input("cual es el precio del producto?: "))
unidades = int(input("cuantas unidades son ?:"))
total = 0

if unidades < 5:
    total = unidades * precio
    print(f"su total es de {total}")

elif unidades >= 5 and unidades <= 10:
    total = unidades * precio 
    total = total - (total * 0.10) 
    print(f"felicidades tuvo el 10 porciento de descuento, su total es {total}")

elif unidades > 10:
    total = unidades * precio 
    total = total - (total * 0.20)
    print(f"felicidades tuvo el 20 porciento de descuento , su total es {total}")