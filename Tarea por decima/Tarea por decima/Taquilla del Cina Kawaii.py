# Taquilla del Cine Kawaii
# Objetivo: Gestionar la venta de N entradas en una sala de cine.

# 1. Pregunta cuántas entradas se van a comprar en total en esta transacción.
# 2. Usa un ciclo while para procesar CADA entrada.
# 3. Para cada entrada, pregunta la EDAD de la persona.
# - Si es menor de 12 años, su entrada cuesta $3.000.
# - Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
# - Si es adulto mayor (65 o más), la entrada cuesta $4.000.
# 4. Usa un acumulador para sumar el precio de todas las entradas.
# 5. Imprime al final el gran total recaudado en esa transacción.

print("****Bienvenidos al cine****")

numero_de_entradas = int(input("¿Cuántas entradas se van a comprar?: "))
contador = 0
acumulador = 0
total_precio_entradas = 0

while numero_de_entradas > contador:
    edad = int(input(f"¿Cuál es la edad de la persona: "))
    if edad < 12:
        total_precio_entradas += acumulador + 3000
    elif edad >= 12 and edad <= 64:
        total_precio_entradas += acumulador + 6000
    else:
        edad > 65
        total_precio_entradas += acumulador + 4000
    contador += 1

print(f"El valor total de la entrada es ${total_precio_entradas}")
print("Fin del programa")