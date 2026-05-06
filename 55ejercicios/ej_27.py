# Ejercicio 27: Saltar Errores del Sistema (Kiosko)

print("=============================")
print("Sistema de limpieza de ventas")
print("=============================")

ventas = [1500, -200, 5000, 0, 100]

total = 0

for venta in ventas:

    if venta <= 0:
        continue

    total = total + venta

print(total)