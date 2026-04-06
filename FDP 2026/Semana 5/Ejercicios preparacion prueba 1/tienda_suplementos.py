total = 0
cant_productos = 0

while True:
    precio_suplemento = int(input("Ingrese el precio del suplemento (-1 para finalizar): $"))

    if precio_suplemento == -1:
        break

    total += precio_suplemento
    cant_productos += 1

if cant_productos >= 3:
    total -= total*0.1

print(f"Total a pagar: ${total}\nCantidad de productos: {cant_productos}")