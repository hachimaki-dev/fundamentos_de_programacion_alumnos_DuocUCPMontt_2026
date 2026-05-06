meta = 300
calorias_quemadas = 0
minutos = 0

while calorias_quemadas < meta:
    minutos += 1
    if minutos < 11:
        calorias_quemadas += 20
    else:
        calorias_quemadas += 10

print(minutos)