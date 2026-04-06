total_entradas = int(input("¿Cuántas entradas desea comprar en esta transacción?: "))
total_recaudado = 0
contador = 0

while contador < total_entradas :
    edad = int(input(f"Ingrese la edad de la persona para la entrada {contador + 1}: "))

    if edad < 12 :
        precio = 3000
    elif 12 <= edad <= 64 :
        precio = 6000
    else:
        precio = 4000
    
    total_recaudado += precio
    contador += 1
print("El total recaudado en esta transacción es: $", total_recaudado)