preciototal = 0
precio_producto = int(input("Cual es el precio de este producto? "))
unidades = int(input("Cuantas unidades se llevará? "))

subtotal = precio_producto * unidades
if unidades >= 5 and unidades <= 10:
    descuento = 0.10
    preciototal = subtotal * round(1- descuento)
    print(f"Felicidades obtuvo un descuento de 10%, su precio a pagar es de {preciototal}.")
elif unidades > 10:
    descuento = 0.20
    preciototal = subtotal * round(1 - descuento)
    print(f"Felicidades obtuvo un descuento de 20%, su precio a pagar es de {preciototal}.")
else:
    preciototal = subtotal
    print(f"No obtuviste descuento, su precio total a pagar es de {preciototal}.")