total = 0
contador = 0

precio = int(input("ingresa el precio de un pote de proteina"))
while precio > 0:
    total = total + precio
    contador += 1
    
    precio = int(input("ingresa el precio de un pote de proteina"))

if contador >= 3:
    total = total*0.9
    print("Total a pagar:", total)   