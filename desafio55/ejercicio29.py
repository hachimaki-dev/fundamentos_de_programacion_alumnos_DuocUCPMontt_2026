meta_kcal = 300
kcal_quemadas = 0
minutos = 0
while True:
    if kcal_quemadas >= meta_kcal:
        minutos = minutos + 1
        break
    elif minutos < 11:
        kcal_quemadas = kcal_quemadas + 20
        minutos = minutos + 1
    elif minutos >= 11:
        kcal_quemadas = kcal_quemadas + 10
        minutos = minutos + 1
print(minutos)


