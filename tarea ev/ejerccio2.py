Precio_Total = 0
Productos = 0 
while True :
    Precio_Suplemento = int(input("Precio del Producto: "))
    Productos += 1
    Precio_Total = Precio_Total + Precio_Suplemento
    
    if Precio_Suplemento == 0 :
        break
print(f"Total a pagar:{Precio_Total}")
print(f"Total de productos:{Productos}")