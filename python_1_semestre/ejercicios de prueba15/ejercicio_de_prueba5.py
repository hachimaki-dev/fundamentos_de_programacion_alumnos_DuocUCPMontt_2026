"""Objetivo: Gestionar la venta de N entradas en una sala de cine.

1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
2. Usa un ciclo while para procesar CADA entrada.
3. Para cada entrada, pregunta la EDAD de la persona.
- Si es menor de 12 años, su entrada cuesta $3.000.
- Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
- Si es adulto mayor (65 o más), la entrada cuesta $4.000.
4. Usa un acumulador para sumar el precio de todas las entradas.
5. Imprime al final el gran total recaudado en esa transacción.  >) y menor que (< {} """
entradas = 0
edad = 0
valor = 0





while entradas  <= 0:
    entradas = int(input("cuantas entradas se van a comprar en total en esta transsacion?: "))
    
    edad = int(input("que edad tienes: ? "))
    if edad  < 12:
        valor = 3000
    
    elif edad >= 12 and edad <= 64:
        valor = 6000
    
    elif edad >= 65:
        valor = 4000
    entradas = entradas * valor 
    print(f"Precio total de las entradas: {entradas}")
        

