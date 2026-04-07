#Tienda de Suplementos (Con Ciclos)

total = 0
productos = 0
while True:
    precio = int (input ("ingrese el precio del suplemento a agregar "))
    if precio == 0:
     break
    total += precio
    productos += 1 
if productos >= 3:
    total = int(total*0.9)
    print ("por la compra de 3 productos o mas se te descuenta el 10% total el cual es :", total, "y la cantidad de productos que compraste fue de ", productos)
else: 
    print ("el valor de la compra total es de: ",total, "y la cantidad de productos es de: ",productos)