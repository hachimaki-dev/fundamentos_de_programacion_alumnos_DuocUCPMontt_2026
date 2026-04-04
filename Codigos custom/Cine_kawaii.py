"""
Objetivo: Gestionar la venta de N entradas en una sala de cine.

1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
2. Usa un ciclo while para procesar CADA entrada.
3. Para cada entrada, pregunta la EDAD de la persona.
- Si es menor de 12 años, su entrada cuesta $3.000.
- Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
- Si es adulto mayor (65 o más), la entrada cuesta $4.000.
4. Usa un acumulador para sumar el precio de todas las entradas.
5. Imprime al final el gran total recaudado en esa transacción.
"""
Total = 0
numero = 1
entradas_totales = int(input("Cuantas entradas se van a comprar en total en esta transaccion? "))
while entradas_totales > 0:
    edad = int(input(f"Cual es la edad de la persona {numero}? "))
    if edad < 12:
        print(f"Cuesta $3000 para la persona {numero}")
        Total = Total = 3000
        entradas_totales = entradas_totales - 1
        numero = numero + 1
    elif edad >= 12 and edad <= 64:
        print(f"Cuesta $6000 para la persona {numero}")
        Total = Total + 6000
        entradas_totales = entradas_totales - 1
        numero = numero + 1
    else:
        print(f"Cuesta $4000 para la persona {numero}")
        Total = Total + 4000
        entradas_totales = entradas_totales - 1
        numero = numero + 1
print(f"En total se recaudo ${Total}")
