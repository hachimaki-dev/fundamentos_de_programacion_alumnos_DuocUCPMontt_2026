ventas_dia = [1500, -200, 5000, 0, 100]
total = 0

for precios in ventas_dia:
    if precios <= 0:
        print("No se pueden sumar montos negativos.")
    elif precios > 0:
        total += precios
        print(f"En total se gano ${total}")

