print("=== Bienvenidos sean ===")

print("Tienda de Suplementos")

total = 0
contador = 0

precio = int(input("Ingrese el precio del suplemento (0 para terminar): "))

while precio > 0:
    
    total = total + precio
    contador = contador + 1
    
    precio = int(input("Ingrese el precio del suplemento (0 para terminar): "))

if contador >= 3:
    total = total * 0.9
    print("Se aplicó un descuento del 10%")

print("Cantidad de productos comprados:", contador)
print("Total a pagar:", total)