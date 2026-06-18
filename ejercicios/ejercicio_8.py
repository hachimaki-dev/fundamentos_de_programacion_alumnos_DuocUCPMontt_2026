# Ejercicio 8 — Clasificación de ventas de un local

ventas_mayores = 0
ventas_medias = 0
ventas_menores = 0

total_recaudado = 0

for i in range(6):

    venta = int(input(f"Ingrese el monto de la venta {i + 1}: "))

    total_recaudado += venta

    if venta > 50000:
        print("Venta mayor")
        ventas_mayores += 1

    elif venta >= 10000:
        print("Venta media")
        ventas_medias += 1

    else:
        print("Venta menor")
        ventas_menores += 1

print()
print(f"Ventas mayores: {ventas_mayores}")
print(f"Ventas medias: {ventas_medias}")
print(f"Ventas menores: {ventas_menores}")
print(f"Total recaudado: ${total_recaudado}")