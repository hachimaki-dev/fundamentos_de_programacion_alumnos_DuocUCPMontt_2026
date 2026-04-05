producto=input("Ingrese el producto que desea comprar: ")
precio=int(input("Ingrese el precio unitario del producto: "))
unidades=int(input("Ingrese la cantidad de unidades a comprar: "))
precio_total=precio*unidades

if unidades<5:
    print(f"No obtuvo ningun descuento. Su total es {precio_total}.")
elif 5<=unidades<=10:
    descuento= precio_total//10
    precio_total-= descuento
    print(f"¡Felicidades obtuvo el 10% de descuento!. Su total es de {precio_total}")
elif unidades>10:
    descuento= precio_total//20
    precio_total-=descuento
    print(f"¡Felicidades obtuvo el 20% de descuento!. Su total es de {precio_total}")