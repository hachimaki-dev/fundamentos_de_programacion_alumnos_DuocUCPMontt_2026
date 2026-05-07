meta_kcal = 300
minutos = 0
calorías_quemadas = 0
while calorías_quemadas <= 300:
    if minutos <= 10:
        calorías_quemadas = calorías_quemadas + 20
        minutos += 1
    else:
        calorías_quemadas = calorías_quemadas + 10
        minutos += 1
print(minutos)