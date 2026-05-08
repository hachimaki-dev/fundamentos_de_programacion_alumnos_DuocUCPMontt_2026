meta = 300
calorias = 0
minutos = 0

while calorias < meta:
    minutos += 1
    if minutos <= 10:
        calorias += 20
    else:
        calorias += 10

print(minutos)