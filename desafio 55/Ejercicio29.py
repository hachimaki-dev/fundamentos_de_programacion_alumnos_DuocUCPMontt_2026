meta = 300
total = 0
minutos = 0
while True:
    minutos = minutos + 1
    if minutos <= 10:
        total = total + 20
    else:
        total = total + 10

    print(f"Llevas {minutos} minuto/s, y has quemado {total} Kcal")

    if total >= meta:
        break

print(f"Has llegado a tu meta, en total has quemado {total} Kcal")