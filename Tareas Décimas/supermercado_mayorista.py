'''
1. Pide registrar un único producto estrella.
2. Pregunta el precio unitario del producto y cuántas unidades está comprando el cliente.
3. La promoción dice: "Si lleva entre 5 y 10 productos iguales, tiene 10% de descuento.
    Si lleva MÁS de 10 productos iguales, tiene 20% descuento". (Si lleva menos de 5, no hay descuento).
4. El programa debe determinar el precio total a pagar, indicando de cuánto fue el porcentaje de descuento que se aplicó
    ("¡Felicidades obtuvo el X% descuento! Su total es...").
5. Ojo: un IF anidado y estructurar bien lo que es "desarrollo matemático".

    2000 -> 100%
      ?  -> 20%

    ? = (20 * 2000) / 100
'''

print("¡PROMOCIÓN!")
print("Si llevas entre 5 y 10 productos iguales, obtienes un 10% de descuento.")
print("¡Si llevas MÁS de 10 productos iguales, obtienes un 20% de descuento!\n")

precio_producto = int (input("Ingrese el precio del producto: "))
cantidad_unidades = int (input("Ingrese cuántas unidades quiere del producto: "))

if cantidad_unidades >= 5 and cantidad_unidades <= 10 :
    porcentaje_descuento = 10
elif cantidad_unidades > 10 :
    porcentaje_descuento = 20
else : 
    porcentaje_descuento = 0

precio_total = (precio_producto * cantidad_unidades)
valor_descontado = (porcentaje_descuento * precio_total) / 100
precio_total_con_descuento = int (precio_total - valor_descontado)

if porcentaje_descuento > 0 :
    print(f"¡Felicidades! Obtuvo el {porcentaje_descuento}% de descuento! Su total es {precio_total_con_descuento}.")
else :
    print(f"El total a pagar es {precio_total_con_descuento}.")