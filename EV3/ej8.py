classification = {
    "high": 0,
    "mid": 0,
    "low": 0
}

total = 0

for i in range(6):
    while True:
        try:
            sale = int(input(f"Ingrese el monto de la venta {i + 1}: $"))
            break
        except ValueError:
            print("Error: Ingrese un número entero positivo")

    total += sale

    if sale > 50000:
        classification["high"] += 1
    elif sale >= 10000 and sale <= 50000:
        classification["mid"] += 1
    else:
        classification["low"] += 1

print(f"Cantidad de ventas mayores: {classification.get("high")}")
print(f"Cantidad de ventas medias: {classification.get("mid")}")
print(f"Cantidad de ventas menores: {classification.get("low")}")
print(f"Total recaudado: ${total}")