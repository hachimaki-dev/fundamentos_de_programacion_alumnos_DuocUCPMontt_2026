meta_kcal = 300
minuto = 0
calorias_quemadas = 0
while True:
    if minuto < 10:
        calorias_quemadas += 20
        minuto += 1
        if calorias_quemadas >= meta_kcal:
            print(minuto)
    else:
        calorias_quemadas += 10
        minuto += 1
        if calorias_quemadas >= 300:
            print(minuto)
            break