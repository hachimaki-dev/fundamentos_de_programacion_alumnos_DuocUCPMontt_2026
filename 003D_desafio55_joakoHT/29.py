calorias = 0
minutos = 0

while calorias < 300:
    minutos += 1

    if minutos <= 10:
        calorias += 20
    else:
        calorias += 10

print(minutos)