#Objetivo: Gestionar la venta de N entradas en una sala de cine.

#1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
#2. Usa un ciclo while para procesar CADA entrada.
#3. Para cada entrada, pregunta la EDAD de la persona.
#- Si es menor de 12 años, su entrada cuesta $3.000.
#- Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
#- Si es adulto mayor (65 o más), la entrada cuesta $4.000.
#4. Usa un acumulador para sumar el precio de todas las entradas.
#5. Imprime al final el gran total recaudado en esa transacción

print("Bienvenido a Cine Kawaii")

print("\nPorfavor ingrese la cantidad de entradas")

cantidadentradas = int(input())
contador = 0
edad =  0
subtotal = 0

while contador < cantidadentradas:
    print("\n¿Cuantos años tiene la persona registrada con esta entrada?")
    edad = int(input())
    if edad < 12: 
        subtotal = subtotal + 3000
        print ("\nAñadida una entrada de niño por $3000")
    elif edad > 64:
        subtotal = subtotal + 4000
        print ("\nAñadida una entrada de adulto mayor por $4000")
    else:
        subtotal = subtotal + 6000
        print ("\nAñadida una entrada de publico general por $6000")
    
    print (f"\nValor de las entradas hasta el momento: \n${subtotal}")
    contador += 1

total = subtotal

print(f"El total de sus entradas es ${total}")

