# Objetivo: Gestionar la venta de N entradas en una sala de cine.
# Pregunta cuántas entradas se van a comprar en total en esta transacción.
cantidad_entradas = int(input("¿Cuántas entradas desea comprar? "))
# Usa un ciclo while para procesar CADA entrada.
contador = 0
total = 0
while contador < cantidad_entradas:
    # Para cada entrada, pregunta la EDAD de la persona.
    edad = int(input("Edad del comprador: "))
    if edad < 12: # Si es menor de 12 años, su entrada cuesta $3.000.
        total += 3000
    elif edad <= 64:
        total += 6000 # Si tiene entre 12 y 64 años, la entrada cuesta $6.000.
    elif edad >= 65:
        total += 4000 # Si es adulto mayor (65 o más), la entrada cuesta $4.000.
    contador += 1
    # Usa un acumulador para sumar el precio de todas las entradas.
print(f"Total a pagar: ${total}")