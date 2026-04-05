cantidad = int(input("Ingrese la cantidad de entradas vendidas: "))

contador = 0
t0tal = 0 

#procesar cada entrada
while contador < cantidad: 
    edad = int(input("Ingrese la edad del cliente: "))
    if edad < 12:
        precio = 3000
    elif 12 <= edad < 64:
        precio = 6000
    else:
        precio = 4000

    t0tal += precio
    contador += 1
#mostrar el total
print("\nEl total a pagar es: $", t0tal) 