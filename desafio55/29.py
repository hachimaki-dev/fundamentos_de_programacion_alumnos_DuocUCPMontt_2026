meta = 300
minutos = 0
calorias_quemada = 0
while calorias_quemada < meta:
    minutos += 1
    if minutos <= 10:
        calorias_quemada += 20
    else:
        calorias_quemada += 10
print(minutos)

