meta = 300
minuto = 0
quemado = 0

while quemado < meta :
    minuto += 1
    if minuto <= 10 :
        quemado += 20

    elif minuto > 10 :
        quemado += 10

print(minuto)