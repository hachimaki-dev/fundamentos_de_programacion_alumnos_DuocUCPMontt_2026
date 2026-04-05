# Taquilla del Cine Kawaii
# Objetivo: Gestionar la venta de N entradas en una sala de cine.

# 1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
# 2. Usa un ciclo while para procesar CADA entrada.
# 3. Para cada entrada, pregunta la EDAD de la persona.
#     - Si es menor de 12 años, su entrada cuesta $3.000.
#     - Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
#     - Si es adulto mayor (65 o más), la entrada cuesta $4.000.
# 4. Usa un acumulador para sumar el precio de todas las entradas.
# 5. Imprime al final el gran total recaudado en esa transacción.

total_recaudado = 0
precio_entrada = 0
numero_entrada = 1

print(" BIENVENIDO AL CINE KAWAII ".center(60,"-"))
cantidad_entradas = int(input("¿Cuantas entradas desea comprar? "))

while cantidad_entradas > 0:
    edad_usuario = int(input(f"Entrada {numero_entrada}: ¿Que edad tiene? "))

    while edad_usuario < 0:
        print("Error: Valor no puede ser negativo")
        edad_usuario = int(input(f"Entrada {numero_entrada}: ¿Que edad tiene? "))
        
    if edad_usuario < 12:
        precio_entrada = 3000
    elif edad_usuario >= 12 and edad_usuario < 65:
        precio_entrada = 6000
    else:
        precio_entrada = 4000
    total_recaudado = total_recaudado + precio_entrada
    cantidad_entradas -= 1
    numero_entrada += 1

if cantidad_entradas == 0:
    print(f"Total recaudado: ${total_recaudado}")

