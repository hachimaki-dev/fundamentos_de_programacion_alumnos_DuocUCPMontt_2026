minutos = 0 
kcal = 300
kcal_quemadas = 0

while kcal_quemadas < kcal:
    minutos += 1
    if minutos <=10:
        kcal_quemadas += 20 
    else: 
        kcal_quemadas += 10 
    print(minutos)