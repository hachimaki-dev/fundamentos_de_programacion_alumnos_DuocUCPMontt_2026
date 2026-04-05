#registro del producto 
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

#calculo del total a pagar
total = precio * cantidad 
descuento = 0 

#aplicar promociones (if anidados)
if cantidad >= 5:
    if cantidad < 10:
        descuento = 0.10 
    else:
        descuento = 0.20 
#calculo final 
monto_descuento = total * descuento
total_final = total - monto_descuento 

#mostrar el resultado 
if descuento > 0:
    print(f"iFelicidades! obtuvo el {int(descuento*100)}% de descuento!") 
else: (print(f"no obtuvo descuento en esta compra."))

print(f"Total a pagar por {producto}: ${total_final:}") 
               