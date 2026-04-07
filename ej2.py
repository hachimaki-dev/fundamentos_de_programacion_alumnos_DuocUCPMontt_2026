total = 0
contador = 0

while True:
    precio = int(input("Ingrese precio del suplemento: $"))
    if precio == 0:
        break

    if precio > 0:
        contador += 1
        total += precio
        print(f"Llevas {contador} suplementos.\n Subtotal: ${total}")
    else:
        print("Monto inválido :(")

if contador >= 3:
    total = total * 0.9
    print("---Se aplicó un 10% dcto---")
    
print (f"Total de productos: {contador}")
print (f"Total: {int (total)}")
print("¡¡¡Gracias por su compra!!!! :D")
