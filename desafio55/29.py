meta = 300
minuto = 0
quemado = 0
while quemado <= meta:
    if minuto <= 10:
        minuto += 1
        quemado += 20
    else:
        minuto += 1
        quemado += 10
print(minuto)
