meta = 300 #kcal
minuto = 0
kcal_quemadas = 0
while kcal_quemadas < meta:
    minuto += 1
    if minuto <= 10:
        kcal_quemadas += 20
    else:
        kcal_quemadas += 10
        
print(f"Minutos en alcanzar la meta: {minuto}")