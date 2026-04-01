#1. Pide registrar un único producto estrella.
#2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
#3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento. Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
#4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó ("¡Felicidades obtuvo el X% descuento! Su total es...").
#5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".
print(f"Promocion especial, si lleva entre 5 y 10 productos iguales, usted obtendra un 10% de descuento. pero si lleva MAS de 10 productos iguales, usted obtendra un 20% de descuento")
producto_estrella = input("registre el producto: ")
costo_producto_estrella = int(input("ingrese el costo del producto: "))
unidades_producto_estrella = int(input("ingrese la cantidad de unidades del producto: "))
costo_total = 0
descuento = 0
if unidades_producto_estrella >= 5 and unidades_producto_estrella <= 10:
    costo_total = costo_producto_estrella * unidades_producto_estrella
    descuento = costo_total * 0.10
    costo_total = costo_total - descuento
    print(f"felicidades obtubo un 10% de descuento su total es de ${costo_total}")
elif unidades_producto_estrella >= 10:
    costo_total = costo_producto_estrella * unidades_producto_estrella
    descuento = costo_total * 0.20
    costo_total = costo_total - descuento
    print(f"felicidades obtubo un 20% de descuento, su total es de ${costo_total}")
elif unidades_producto_estrella < 5:
    costo_total = costo_producto_estrella * unidades_producto_estrella
    print(f"su total es de ${costo_total}")