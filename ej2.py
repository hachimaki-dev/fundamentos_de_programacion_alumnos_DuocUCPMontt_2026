total = 0
cantidad_de_productos = 0


print("Si quiere dejar de agregar productos ingrese número (0)")

precio_ingresado = int(input("¿Qué valor tiene lo que lleva? "))

while precio_ingresado > 0:
    total = total + precio_ingresado
    cantidad_de_productos = cantidad_de_productos + 1
 
    precio_ingresado = int(input("¿Qué valor tiene lo que lleva? "))


if precio_ingresado == 0 and cantidad_de_productos >= 3:
    print("¡Se le ha aplicado un descuento del 10%!")
    print(f"Lleva {cantidad_de_productos} productos, y su total a pagar es de {total * 0.9}")


elif precio_ingresado == 0 and cantidad_de_productos < 3:
    print(f"Lleva {cantidad_de_productos} productos, y su total a pagar es de {total}.")